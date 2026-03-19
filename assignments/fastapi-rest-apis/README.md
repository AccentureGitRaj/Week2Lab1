# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a beginner-friendly REST API using FastAPI to understand routing, request/response handling, and API testing. By the end of this assignment, you will create endpoints that return data and accept user input.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Set up a FastAPI application with foundational endpoints for a small student task tracker service. You will define routes for a health check and for listing tasks.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Add a `GET /` endpoint that returns a welcome message.
- Add a `GET /tasks` endpoint that returns a list of at least 3 sample tasks in JSON format.


### 🛠️	Add Request Handling and Validation

#### Description
Extend the API with an endpoint that accepts data from the client and adds a new task. Use FastAPI models to validate input and return clear responses.

#### Requirements
Completed program should:

- Add a `POST /tasks` endpoint that accepts a task title and completion status.
- Use a Pydantic model for request validation.
- Return the created task with an auto-incremented `id` field.
