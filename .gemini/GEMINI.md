# Shipping Service API Context

## Project Overview
The Shipping Service API is a Python-based microservice designed for Acme Corp to manage package information. It provides a RESTful interface for creating, retrieving, updating, and deleting package details (dimensions, weight, handling instructions).

**Key Technologies:**
-   **Language:** Python 3.12+
-   **Web Framework:** Flask
-   **Database/ORM:** SQLAlchemy (currently configured for SQLite via `connect_connector.py`)
-   **Testing:** `unittest` (standard library) and `pytest` (installed via requirements)

## Architecture
-   **Monolithic Structure:** The core application logic and route definitions reside in `main.py`.
-   **Data Model:** The database schema (`Package` table) is defined in `data_model.py` using SQLAlchemy declarative base.
-   **Database Connection:** Database session management is handled via `connect_connector.py` (imports `SessionMaker`, `Base`, `engine`).
-   **API Design:** RESTful endpoints accepting and returning JSON.

## Key Files
-   `main.py`: The entry point for the Flask application. Defines API routes (`/discovery`, `/liveness`, `/packages`, etc.) and handles request processing.
-   `data_model.py`: Defines the `Package` SQLAlchemy model.
-   `connect_connector.py`: Handles database connection setup and session creation (inferred).
-   `requirements.txt`: Lists Python dependencies (Flask, SQLAlchemy, requests, pytest, etc.).
-   `activate.sh`: Sets up environment variables (GCP project, location, model ID) and modifies `PATH`.
-   `tests/test.py`: Unit tests using Python's `unittest` framework.
-   `curl.sh`: A shell script for manual integration testing via `curl` commands.

## Setup & Running

### Prerequisites
-   Python 3.12+
-   `pip`

### Installation
1.  **Virtual Environment:**
    It is recommended to use a virtual environment.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    *Note: `activate.sh` also exports specific GCP-related environment variables.*

2.  **Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
Start the Flask development server:
```bash
python3 main.py
```
The server listens on `http://0.0.0.0:8000`.

## Testing

### Unit Tests
Run the test suite using `pytest` (recommended) or `unittest`:
```bash
pytest
# OR
python3 -m unittest tests/test.py
```

### Integration Tests
Use the provided `curl` script to verify endpoints against a running server:
```bash
./curl.sh
```

## Development Conventions
-   **Code Style:** Follows standard Python PEP 8 guidelines.
-   **Session Management:** Database sessions are manually managed in each route using a `try...finally` block to ensure `session.close()` is called.
-   **Error Handling:** Uses Flask's `abort()` to return HTTP error codes (400, 404).
-   **Environment Variables:** The `activate.sh` script suggests integration with Google Cloud Platform (Vertex AI/Gemini), likely for future AI-driven features.
