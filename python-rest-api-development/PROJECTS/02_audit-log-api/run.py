# run.py  ← this is your entry point, like index.js in Node
from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True gives you auto-reload when you save files
    # NEVER use debug=True in production
    app.run(debug=True, port=5001)