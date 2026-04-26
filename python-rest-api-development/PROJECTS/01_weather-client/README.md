# 01 Weather Client

## Project Overview

This project is a small Python client that fetches air-quality station data from the MET Norway API and maps each station into a typed Python model.

At a high level, it demonstrates:
- Making HTTP requests with `requests`.
- Optionally disabling SSL certificate verification for local/testing scenarios.
- Converting API response dictionaries into structured `dataclass` objects.

## Project Structure

- `main.py` - entry point that calls the API in two modes (SSL verification on and off), then prints a quick summary of the results.
- `client.py` - lightweight API client wrapper with a `get()` method.
- `models.py` - `Station` dataclass and `from_dict()` mapper for station records.
- `requirements.txt` - pinned Python dependencies.

## Prerequisites

- Python 3.10+ (recommended).
- `pip` available in your environment.

## Environment Setup

From the `01_weather-client` folder:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you are on Windows (PowerShell), activate with:

```powershell
venv\Scripts\Activate.ps1
```

## Run the Project

With your virtual environment activated:

```bash
python main.py
```

You should see output for two request modes:
- `SSL ON (default)`
- `SSL OFF (verify=False)`

Each mode attempts to fetch stations and prints the station count plus a sample station name and city.

## Why SSL Is Important

Use SSL verification (`verify=True`, the default) for normal development and production use.

- It encrypts traffic between your client and the API.
- It verifies that your client is talking to the real server.
- It helps prevent man-in-the-middle attacks and response tampering.

The `SSL OFF (verify=False)` mode in this project is included only as a lesson/demo scenario. Keep SSL on unless you are troubleshooting in a controlled environment.

## Quick Start Checklist

1. Open terminal in `01_weather-client`.
2. Create and activate a virtual environment.
3. Install dependencies from `requirements.txt`.
4. Run `python main.py`.

## Notes

- This project is intended as a learning/example client for consuming a REST API.
- SSL verification should normally remain enabled in production use.
