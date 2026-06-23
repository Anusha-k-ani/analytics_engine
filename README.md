Analytics Engine

#Overview

This project is a modular backend analytics engine built using FastAPI for an e-commerce platform. 
The purpose of this project is to simulate a backend service that handles transaction calculations and storefront performance analysis. 
The application is designed using a clean and scalable architecture by separating route logic using FastAPI’s APIRouter.

#Features

* Modular FastAPI project structure
* Root health-check endpoint
* Transaction valuation calculation
* Storefront performance analysis
* Query parameter handling
* Path parameter handling
* Interactive API documentation with Swagger UI

#Project Structure


analytics_engine/
├── .gitignore
├── pyproject.toml
└── app/
    ├── __init__.py
    ├── main.py
    └── routers/
        ├── __init__.py
        └── metrics.py


#File Description

* main.py → Initializes FastAPI app and registers routes
* metrics.py → Contains analytics API endpoints
* routers/→ Organizes application routes

#API Endpoints

#Root Endpoint

*GET /

Returns application health status.

Example Response:


{
  "status": "Engine Online",
  "version": "1.0.0"
}


#Calculate Transaction Valuation

*POST /metrics/calculate

Query Parameters:

* unit_price (float)
* quantity (int)
* currency (string)

Example:


/metrics/calculate?unit_price=150&quantity=3&currency=USD


Response:


{
  "transaction_total": 450.0,
  "formatted_summary": "Total amount is 450.00 USD"
}


#Storefront Performance Profile

*GET /metrics/store/{store_id}

Path Parameter:

* store_id (string)

Optional Query Parameter:

* filter_type (default = "all")

Example:


/metrics/store/main-hub?filter_type=all


Response:

{
  "store_id": "main-hub",
  "active_filter": "all",
  "performance_tier": "High Volume Profile"
}


#Installation and Setup

#Clone Repository
git clone <repository-url>
cd analytics_engine

#Create Virtual Environment

Mac/Linux:

python3 -m venv .venv
source .venv/bin/activate

#Install Dependencies

pip install fastapi uvicorn

#Running the Application

Start the FastAPI server:
uvicorn app.main:app --reload

Server will run at:
http://127.0.0.1:8000


#API Documentation

Swagger UI:
http://127.0.0.1:8000/docs


ReDoc:
http://127.0.0.1:8000/redoc

## Technologies Used

* Python
* FastAPI
* Uvicorn
* GitHub
