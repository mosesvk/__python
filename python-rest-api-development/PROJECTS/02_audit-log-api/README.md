# 02 Audit Log API

## Project Overview

This project is a small Flask REST API that manages client audit logs in memory, plus a Python client script that consumes the API.

At a high level, it demonstrates:
- Building REST endpoints with Flask and Blueprints.
- Validating request input and returning appropriate HTTP status codes.
- Recording and retrieving audit trail entries for specific clients.
- Calling the API from another Python script with `requests`.

## Project Structure

- `run.py` - API entry point; starts the Flask app on port `5001`.
- `app/__init__.py` - app factory (`create_app`) and blueprint registration.
- `app/routes.py` - API endpoints for reading and creating audit logs.
- `app/data.py` - in-memory client and audit log data store.
- `client.py` - simple consumer script that reads logs, writes a new log, then verifies results.
- `requirements.txt` - pinned Python dependencies.

## Prerequisites

- Python 3.10+ (recommended).
- `pip` available in your environment.

## Environment Setup

From the `02_audit-log-api` folder:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you are on Windows (PowerShell), activate with:

```powershell
venv\Scripts\Activate.ps1
```

## Getting Started

### 1) Start the API server

With your virtual environment activated:

```bash
python run.py
```

The API starts on `http://localhost:5001`.

### 2) Run the client script (in another terminal)

Open a second terminal in the same project, activate the same virtual environment, then run:

```bash
python client.py
```

The client will:
- Fetch logs for client `1`.
- Create a new audit log entry.
- Fetch logs again to confirm the new entry was saved.

## API Endpoints

- `GET /api/clients/<client_id>/logs` - returns logs for the given client.
- `POST /api/clients/<client_id>/logs` - creates a new log for the client.

Example JSON body for `POST`:

```json
{
  "user_id": "msvk",
  "action": "VIEW",
  "details": "Partner review before Q2 close"
}
```

Allowed `action` values: `VIEW`, `EDIT`, `EXPORT`, `DELETE`.

## Security Note (SSL/HTTPS)

This project uses `http://localhost` for local development only. In production, audit log APIs should always run over HTTPS (SSL/TLS) to encrypt traffic, verify server identity, and reduce man-in-the-middle risk.

## Notes

- Data is stored in memory, so restarting the API resets all logs to the seed data in `app/data.py`.
- `debug=True` in `run.py` is convenient for development but should not be used in production.
