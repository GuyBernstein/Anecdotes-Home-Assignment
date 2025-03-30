# FastAPI DummyJSON API Client

# Watch me --> https://drive.google.com/file/d/15Al_Ai8qxV_hH_TzwmnKveSUPc5H3X80/view?usp=sharing

This repository contains a FastAPI application that serves as a client for the DummyJSON API, providing several endpoints that aggregate and transform data from various DummyJSON services.

## Overview

The application provides three main endpoints:

1. `/get-first-valid-user` - Finds and returns the first user with valid login credentials
2. `/get-60-posts` - Retrieves 60 posts with minimal information
3. `/get-60-posts-with-comments` - Retrieves 60 posts along with their comments, demonstrating concurrent API calls

## Features

- Asynchronous HTTP requests using `httpx`
- Concurrent API calls with `asyncio`
- Docker containerization
- Clean FastAPI structure

## External APIs Used

The application interacts with the following DummyJSON endpoints:

- `https://dummyjson.com/users` - User data
- `https://dummyjson.com/auth/login` - Authentication
- `https://dummyjson.com/posts` - Post data
- `https://dummyjson.com/comments/post` - Comments for posts

## Prerequisites

- Python 3.11+
- Docker (optional, for containerized deployment)

## Installation

### Local Setup

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   uvicorn main:app --reload
   ```

### Docker Setup

1. Build the Docker image:
   ```
   docker build -t fastapi-dummyjson-client .
   ```
2. Run the container:
   ```
   docker run -p 8000:8000 fastapi-dummyjson-client
   ```

## API Endpoints

### GET /get-first-valid-user

Returns the first user from the DummyJSON API that has valid login credentials.

**Response Example:**
```json
{
  "firstName": "Terry",
  "lastName": "Medhurst",
  "username": "atuny0",
  "password": "9uQFF1Lh",
  "auth": {
    "token": "...",
    "id": 1,
    "username": "atuny0",
    "email": "atuny0@sohu.com",
    "firstName": "Terry",
    "lastName": "Medhurst",
    "gender": "male",
    "image": "..."
  }
}
```

### GET /get-60-posts

Returns a list of 60 posts with minimal information (id and title).

**Response Example:**
```json
{
  "posts": [
    {
      "id": 1,
      "title": "His mother had always taught him"
    },
    {
      "id": 2,
      "title": "He was an expert but not in a discipline"
    },
    ...
  ]
}
```

### GET /get-60-posts-with-comments

Returns a list of 60 posts, each with its associated comments. This endpoint demonstrates concurrent API calls.

**Response Example:**
```json
{
  "posts": [
    {
      "id": 1,
      "title": "His mother had always taught him",
      "comments": [
        {
          "id": 1,
          "body": "This is some awesome thinking!",
          "postId": 1,
          "user": {
            "id": 63,
            "username": "eburras1q"
          }
        },
        ...
      ]
    },
    ...
  ]
}
```

## Documentation

After starting the application, you can access the automatically generated API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

The live version of this API is available at:
- https://anecdotes-home-assignment.runmydocker-app.com/docs#/

## Project Structure

```
/
├── main.py            # FastAPI application and endpoints
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker configuration
└── README.md          # This documentation file
```

## License

[Include your license information here]

## Contributing

[Include contribution guidelines here]
