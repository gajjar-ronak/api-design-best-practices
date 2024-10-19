# Designing Clean and Organized APIs for Scalability Using FastAPI and MongoDB and PostgreSQL support.

![API](https://github.com/user-attachments/assets/5854a286-caff-46b6-9b0d-adbd716307b9)


This project demonstrates a scalable and modular RESTful API using **FastAPI**, integrating both **PostgreSQL** and **MongoDB** for data storage. It is designed to handle large-scale applications with clean project structure and extensibility.

## Features

- **PostgreSQL**: Used for structured data storage (SQLAlchemy).
- **MongoDB**: Used for flexible, document-based data storage (Motor).
- **Modular Architecture**: Separation of concerns for scalability and maintainability.
- **RESTful API**: Implements user-related APIs with the capability to easily add new modules.
- **Test Cases**: Includes unit tests for the API using FastAPI’s `TestClient`.

## Project Structure
``` 
├── app
│   ├── api
│   │── v1
│   ├── core
│   ├── models
│   ├── schemas
│   ├── services
│   ├── tests
│────── __init__.py
│────── main.py
│── .env
│── .gitignore
│── .README.md
│── requirement.txt
```

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:gajjar-ronak/api-design-best-practices.git
    cd fastapi-scalable-project
    ```

2. Create and configure the `.env` file:
    ```
    POSTGRES_DB=your_db
    POSTGRES_USER=your_user
    POSTGRES_PASSWORD=your_password
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    MONGODB_URI=mongodb://localhost:27017
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

5. Access the API at `http://127.0.0.1:8000`.

## Testing

Run the test cases using:
```bash
pytest
```

## Endpoints

`POST /api/v1/users/: Create a new user.
GET /api/v1/users/{user_id}: Retrieve user details by ID.
`

