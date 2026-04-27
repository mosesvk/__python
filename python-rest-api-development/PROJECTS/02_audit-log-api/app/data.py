# app/data.py
# In-memory store — simulates what would be a real DB in production
# At an accounting firm, these would live in a secure, encrypted RDS instance

clients = {
    1: {"id": 1, "name": "Deloitte Client A", "entity_type": "Corporation"},
    2: {"id": 2, "name": "KPMG Client B", "entity_type": "Partnership"},
    3: {"id": 3, "name": "Internal - Firm Operations", "entity_type": "Internal"},
}

audit_logs = [
    {
        "id": 1,
        "client_id": 1,
        "user_id": "jsmith",
        "action": "VIEW",
        "timestamp": "2026-04-01T09:12:00",
        "details": "Quarterly review prep"
    },
    {
        "id": 2,
        "client_id": 1,
        "user_id": "aparker",
        "action": "EXPORT",
        "timestamp": "2026-04-01T14:30:00",
        "details": "SOC2 evidence pull"
    },
    {
        "id": 3,
        "client_id": 2,
        "user_id": "jsmith",
        "action": "EDIT",
        "timestamp": "2026-04-02T10:00:00",
        "details": "Updated engagement letter"
    },
]

# Auto-increment counter (like a DB sequence)
next_log_id = 4