# client.py
# Simulates a compliance script that pulls and writes audit logs
# This is the "consumer" side — it talks to your API using requests

import requests

BASE_URL = "http://localhost:5001"


def get_logs(client_id: int) -> list:
    """Pull all audit logs for a client — pre-audit review."""
    response = requests.get(f"{BASE_URL}/api/clients/{client_id}/logs")
    response.raise_for_status()
    return response.json()


def create_log(client_id: int, user_id: str, action: str, details: str) -> dict:
    """Record a new action against a client — called when user touches a record."""
    payload = {
        "user_id": user_id,
        "action": action,
        "details": details
    }
    response = requests.post(
        f"{BASE_URL}/api/clients/{client_id}/logs",
        json=payload        # requests serializes the dict AND sets Content-Type header
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print("=== Fetching logs for Client 1 (pre-quarter review) ===")
    logs = get_logs(client_id=1)
    for log in logs:
        print(f"  [{log['timestamp']}] {log['user_id']} → {log['action']} | {log['details']}")

    print("\n=== Recording new access event ===")
    new_log = create_log(
        client_id=1,
        user_id="msvk",
        action="VIEW",
        details="Partner review before Q2 close"
    )
    print(f"  Recorded: {new_log}")

    print("\n=== Verifying log was appended ===")
    logs = get_logs(client_id=1)
    print(f"  Total logs for client 1: {len(logs)}")