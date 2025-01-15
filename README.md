#Requirements to run
- Python
- Node

#Setting Up the Frontend
1. Run `npm install`.
2. Run `npm run dev` for development mode.

#Setting up the websocket server
1. Make sure the necessary dependencies are installed and that it has a venv.
2. Run test.py.

# How It Works
The websocket server is meant to forward the message from the mango factory to the other connected websocket clients(aka the frontend).
For a smooth run, make sure you start the websocket server first, then the frontend, then the mango factory.
