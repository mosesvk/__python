# app/routes.py
from flask import Blueprint, jsonify, request
import app.data as data
from datetime import datetime, timezone

audit_bp = Blueprint("audit", __name__, url_prefix="/api")


@audit_bp.route("/clients/<int:client_id>/logs", methods=["GET"])
def get_logs_for_client(client_id):
    if client_id not in data.clients:
        return jsonify({"error": f"Client {client_id} not found"}), 404

    client_logs = [log for log in data.audit_logs if log["client_id"] == client_id]
    return jsonify(client_logs), 200


@audit_bp.route("/clients/<int:client_id>/logs", methods=["POST"])
def create_log_for_client(client_id):
    if client_id not in data.clients:
        return jsonify({"error": f"Client {client_id} not found"}), 404

    body = request.get_json()

    required = ["user_id", "action", "details"]
    for field in required:
        if field not in body:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    allowed_actions = ["VIEW", "EDIT", "EXPORT", "DELETE"]
    if body["action"] not in allowed_actions:
        return jsonify({"error": f"action must be one of {allowed_actions}"}), 400

    new_log = {
        "id": data.next_log_id,
        "client_id": client_id,
        "user_id": body["user_id"],
        "action": body["action"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "details": body["details"]
    }

    data.audit_logs.append(new_log)
    data.next_log_id += 1

    return jsonify(new_log), 201