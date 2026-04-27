# app/routes.py
from flask import Blueprint, jsonify
from app.data import clients, audit_logs

# Create the blueprint — "audit" is its internal name
audit_bp = Blueprint("audit", __name__, url_prefix="/api")


@audit_bp.route("/clients/<int:client_id>/logs", methods=["GET"])
def get_logs_for_client(client_id):
    """
    GET /api/clients/1/logs
    Returns all audit logs for a specific client.
    404 if the client doesn't exist.
    """

    # First — does this client exist?
    # This is the same check you'd do before querying a DB
    if client_id not in clients:
        return jsonify({"error": f"Client {client_id} not found"}), 404

    # Filter logs belonging to this client
    client_logs = [log for log in audit_logs if log["client_id"] == client_id]

    return jsonify(client_logs), 200
    