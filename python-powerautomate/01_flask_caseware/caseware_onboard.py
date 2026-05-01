"""
caseware_onboard.py
===================
The ??? node: A Flask app that Power Automate calls.
Handles the Caseware "check if exists, create if not" logic.

Flow:
  Power Automate POST /onboard-client
    → get_caseware_token()
    → check if entity exists (GET /api/v2/entities?search=...)
    → if not found: create entity (POST /api/v2/entities)
    → return result to Power Automate

Setup:
  1. pip install flask requests
  2. Fill in your FIRM, CLIENT_ID, CLIENT_SECRET below
  3. python caseware_onboard.py
  4. In another terminal: ngrok http 5000
  5. Copy the ngrok HTTPS URL → paste into Power Automate HTTP action
"""

import requests
from flask import Flask, request, jsonify
import os
import re
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ── CONFIG ─────────────────────────────────────────────────────────────────────
# Get CLIENT_ID and CLIENT_SECRET from:
# CaseWare Cloud → Firm Settings → Integration → API Clients
CASEWARE_DOMAIN = "us.casewarecloud.com"
FIRM_SHORT_NAME  = "criadvuat"   # test site for now "uat"
CLIENT_ID     = os.getenv("CASEWARE_CLIENTID")
CLIENT_SECRET = os.getenv("CASEWARE_SECRET")

BASE_URL = f"https://{CASEWARE_DOMAIN}/{FIRM_SHORT_NAME}/ms/caseware-cloud"
# ───────────────────────────────────────────────────────────────────────────────

def get_caseware_token() -> str:
    url = f"{BASE_URL}/api/v2/auth/token"
    payload = {
        "ClientId":     CLIENT_ID,
        "ClientSecret": CLIENT_SECRET
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    print(f"DEBUG auth response: {response.json()}")  # add this
    return response.json()["Token"]


def find_entity(token: str, client_name: str) -> dict | None:
    url = f"{BASE_URL}/api/v2/entities"
    headers = {"Authorization": f"Bearer {token}"}
    params  = {"pageSize": 50}  # get all, no search filter

    response = requests.get(url, headers=headers, params=params)
    print(f"DEBUG entities status: {response.status_code}")
    print(f"DEBUG entities response: {response.text[:500]}")
    response.raise_for_status()

    raw_results = response.json()
    # CaseWare may return either a direct list or a wrapped object.
    if isinstance(raw_results, list):
        entities = raw_results
    elif isinstance(raw_results, dict):
        entities = raw_results.get("items") or raw_results.get("data") or []
    else:
        entities = []

    for entity in entities:
        if entity.get("Name", "").lower() == client_name.lower():
            return entity
    return None


def create_entity(token: str, client_data: dict) -> dict:
    """
    Create a new client entity in CaseWare.
    POST /api/v2/entities
    Returns the created entity.
    """
    url = f"{BASE_URL}/api/v2/entities"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type":  "application/json"
    }

    raw_entity_no = (client_data.get("entity_no") or "").strip()
    if raw_entity_no:
        entity_no = raw_entity_no
    else:
        # Fall back to a deterministic value derived from client name.
        entity_no = re.sub(r"[^A-Za-z0-9]", "", client_data.get("client_name", ""))[:12].upper() or "NEWCLIENT"

    # Map incoming form fields to CaseWare entity schema
    payload = {
        "Name":         client_data.get("client_name"),
        "EntityNo":     entity_no,
        "Type":         "C",    # C = Client entity
        "EmailAddress": client_data.get("email", ""),
        # Add more fields as needed:
        # "StandardIndustryCode": client_data.get("industry_code"),
        # "Contact1FirstName":    client_data.get("contact_first_name"),
        # "Contact1LastName":     client_data.get("contact_last_name"),
        # "Contact1Email":        client_data.get("contact_email"),
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code >= 400:
        print(f"DEBUG create_entity status: {response.status_code}")
        print(f"DEBUG create_entity response: {response.text[:1000]}")
    response.raise_for_status()
    return response.json()


# ── ENDPOINT ───────────────────────────────────────────────────────────────────
@app.route("/onboard-client", methods=["POST"])
def onboard_client():
    """
    Power Automate calls this endpoint with client data from the SharePoint form.

    Expected JSON body from Power Automate:
    {
        "client_name": "Acme Corp",
        "email": "contact@acme.com"
    }

    Returns:
    {
        "status": "created" | "already_exists",
        "entity": { ...caseware entity fields... }
    }
    """
    data = request.get_json()

    if not data or not data.get("client_name"):
        return jsonify({"error": "client_name is required"}), 400

    client_name = data["client_name"]

    try:
        # Step 1: Authenticate
        token = get_caseware_token()

        # Step 2: Check if entity already exists
        existing = find_entity(token, client_name)

        if existing:
            return jsonify({
                "status": "already_exists",
                "entity": existing
            }), 200

        # Step 3: Create the entity if it doesn't exist
        new_entity = create_entity(token, data)

        return jsonify({
            "status": "created",
            "entity": new_entity
        }), 201

    except requests.HTTPError as e:
        return jsonify({
            "error": "Caseware API error",
            "detail": str(e),
            "response": e.response.text if e.response is not None else None
        }), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── HEALTH CHECK ───────────────────────────────────────────────────────────────
@app.route("/health", methods=["GET"])
def health():
    """Simple health check so you can confirm the server is running."""
    return jsonify({"status": "ok", "message": "CaseWare onboarding service is running"}), 200


if __name__ == "__main__":
    # debug=True so you can see errors in the terminal during practice
    # In production (Lambda/Azure Function), you'd remove this
    app.run(debug=True, port=5000)