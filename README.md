# Shipping Service API

## Overview

The Shipping Service API is a Python-based microservice designed to manage package information for Acme Corp. It provides a RESTful interface for creating, retrieving, updating, and deleting package details, including dimensions, weight, and special handling instructions.

## Business Logic

The service handles the lifecycle of package data:

- **Package Creation**: Allows new packages to be registered with specific physical attributes (height, width, depth, weight) and handling instructions.
- **Package Retrieval**: Packages can be looked up by their associated `product_id`.
- **Package Retrieval**: Packages can be looked up by their associated `package_id`.

## API Routes

| Method | Endpoint                 | Description                                             |
| :----- | :----------------------- | :------------------------------------------------------ |
| `GET`  | `/discovery`             | Returns service metadata (name, version, owners).       |
| `GET`  | `/liveness`              | Health check endpoint to verify the service is running. |
| `GET`  | `/readiness`             | Readiness check endpoint.                               |
| `POST` | `/packages`              | Creates a new package entry.                            |
| `GET`  | `/packages/<package_id>` | Retrieves package details by Package ID.                |

## Design Patterns & Architecture

- **Microservice Architecture**: Designed as a standalone service responsible for shipping domain data.
- **RESTful API**: Follows REST principles for resource management.
- **ORM (Object-Relational Mapping)**: Uses **SQLAlchemy** to abstract database interactions.
- **In-Memory Database**: Currently configured to use **SQLite** with a `StaticPool` for persistence within the application process, making it easy to run locally without external dependencies.
- **Session Management**: Implements a robust database session handling pattern (`try...finally`) to ensure connections are properly closed.

## Frameworks & Libraries

- **Python 3.12+**: The core programming language.
- **Flask**: A lightweight WSGI web application framework for building the API endpoints.
- **SQLAlchemy**: The SQL toolkit and Object Relational Mapper for database operations.
- **Requests**: Used for internal service calls (e.g., discovery).

## How to Run

### Prerequisites

- Python 3.12 or higher installed.
- `pip` (Python package installer).

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
    pip install -r requirements.txt
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

    PYTHONPATH=. pytest tests/test.py

    PYTHONPATH=. python3 -m unittest tests/test.py
    ```

### Testing prompts in gemini cli

1. /generate:gemini_md
2. Explain to me the design patterns, framework, and workflow used in this web service. Show me where the rest end points are mapped and the life of a request.
3. /explain:interactive
4. Generate an open api spec documentation for the rest api endpoints defined in main.py, and output to shipping-open-api.yaml.
   \*note after open api spec is generated validate the spec here https://editor.swagger.io/
5. Now add to the @shipping-open-api.yaml. create an delete endpoint that takes a package id parameter, and return 200 if delte is successful. Then add put endpoint that takes the package as payload, and returns the updated package as response.
6. Use the openapi spec create the delete, and put endpoint for the package.
7. Write unit tests for different endpoints in main.py utilize mocking for any db connection and run the tests with python command. Make sure the tests pass as criteria.
8. /plan:new Follow the design pattern for model view controllers. Break out the source code in @main.py to fit this pattern. create service.py where the business logic lives.
9. /plan:impl @path_plan_created_in_step4
10. Write unit tests for different functions in service.py you just generated from the previous prompt, and run the tests with python command. Make sure the tests pass.
11. Use nano banana to generate architecture diagrams of the shipping service python app.
12. /plan:new Generate a dockerfile for deployment to cloud run or gke in gcp.
13. /plan:impl @path_plan_created_in_step8
14. extensions:
    a. gemini extensions install https://github.com/ddobrin/gemini-plan-commands
    b. gemini extensions install https://github.com/gemini-cli-extensions/nanobanana

15. write a command for solid..
    Principle Description
    Single Responsibility A class or function should have only one reason to change (e.g., separating data persistence logic from business logic).
    Open/Closed Software entities should be open for extension but closed for modification. You can add new features without changing existing, working code.
    Liskov Substitution Objects of a superclass should be replaceable with objects of a subclass without breaking the application.
    Interface Segregation It's better to have many client-specific, focused interfaces than one general-purpose interface.
    Dependency Inversion Depend on abstractions (interfaces) rather than concrete implementations. This improves modularity and testability.
