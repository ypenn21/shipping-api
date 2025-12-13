# Shipping Service API

## Overview
The Shipping Service API is a Python-based microservice designed to manage package information for Acme Corp. It provides a RESTful interface for creating, retrieving, updating, and deleting package details, including dimensions, weight, and special handling instructions.

## Business Logic
The service handles the lifecycle of package data:
-   **Package Creation**: Allows new packages to be registered with specific physical attributes (height, width, depth, weight) and handling instructions.
-   **Package Retrieval**: Packages can be looked up by their associated `product_id`.
-   **Package Updates**: Existing package details can be modified to reflect changes in dimensions or handling requirements.
-   **Package Deletion**: Packages can be removed from the system when no longer needed.

## API Routes

| Method | Endpoint                  | Description                                      |
| :----- | :------------------------ | :----------------------------------------------- |
| `GET`  | `/discovery`              | Returns service metadata (name, version, owners). |
| `GET`  | `/liveness`               | Health check endpoint to verify the service is running. |
| `GET`  | `/readiness`              | Readiness check endpoint.                        |
| `GET`  | `/packages/<product_id>`  | Retrieves package details by Product ID.         |
| `POST` | `/packages`               | Creates a new package.                           |
| `PUT`  | `/packages/<package_id>`  | Updates an existing package by Package ID.       |
| `DELETE`| `/packages/<package_id>` | Deletes a package by Package ID.                 |

## Design Patterns & Architecture
-   **Microservice Architecture**: Designed as a standalone service responsible for shipping domain data.
-   **RESTful API**: Follows REST principles for resource management.
-   **ORM (Object-Relational Mapping)**: Uses **SQLAlchemy** to abstract database interactions.
-   **In-Memory Database**: Currently configured to use **SQLite** with a `StaticPool` for persistence within the application process, making it easy to run locally without external dependencies.
-   **Session Management**: Implements a robust database session handling pattern (`try...finally`) to ensure connections are properly closed.

## Frameworks & Libraries
-   **Python 3.12+**: The core programming language.
-   **Flask**: A lightweight WSGI web application framework for building the API endpoints.
-   **SQLAlchemy**: The SQL toolkit and Object Relational Mapper for database operations.
-   **Requests**: Used for internal service calls (e.g., discovery).

## How to Run

### Prerequisites
-   Python 3.12 or higher installed.
-   `pip` (Python package installer).

### Installation

1.  **Clone the repository**:
    ```bash
    git clone git@github.com:ypenn21/shipping-api.git
    cd shipping-api
    ```

2.  **Create and activate a virtual environment** (recommended):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    # .venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r app/requirements.txt
    ```

### Running the Application

1.  **Start the server**:
    ```bash
    python3 main.py
    ```
    The application will start on `http://0.0.0.0:8000`.

### Testing

A `curl.sh` script is provided to test the main API endpoints.

1.  **Run the test script**:
    ```bash
    ./curl.sh
    ```
    This script will perform a sequence of `GET`, `POST`, `PUT`, and `DELETE` operations to verify the API's functionality.
