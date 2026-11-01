# Python Placement Preparation — Day 3
Name: Telugu Shivani 
Date:29/10/2026  
Day: 3 — HTTP & FastAPI Basics

## 1. Coding Problem: Build a Validated FastAPI Items API

### Approach:

1. Import `FastAPI`, `HTTPException`, `BaseModel`, and `Field`.
2. Create a FastAPI application using `FastAPI()`.
3. Define a Pydantic request model named `ItemCreate`.
4. Use `Field()` to validate that the item name is not empty and the price is greater than zero.
5. Create an empty dictionary to store items.
6. Create a POST endpoint `/items` to add a new item.
7. Create a GET endpoint `/items/{item_id}` to retrieve an item using its ID.
8. Create another GET endpoint `/items?limit=...` to retrieve items with a limit.
9. Use `HTTPException` to return a 404 error if the requested item does not exist.
10. Define a response model to control the output returned by the API.

### Code:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)

class ItemOut(BaseModel):
    id: int
    name: str
    price: float

items = {}

@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(item: ItemCreate):
    item_id = len(items) + 1

    new_item = {
        "id": item_id,
        "name": item.name,
        "price": item.price
    }

    items[item_id] = new_item
    return new_item

@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Item ID must be positive"
        )

    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return items[item_id]

@app.get("/items")
def list_items(limit: int = 20):
    if limit < 1 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 100"
        )

    return list(items.values())[:limit]


### Test Inputs and Outputs:

Test Case 1 — Create an item

Method: POST

URL:

/items


Input:

{
    "name": "Laptop",
    "price": 50000
}


Output:
{
    "id": 1,
    "name": "Laptop",
    "price": 50000
}


Status Code: `201 Created`

Test Case 2 — Get an existing item

Method: GET

URL:

/items/1


Output:

{
    "id": 1,
    "name": "Laptop",
    "price": 50000
}


Status Code: `200 OK`

Test Case 3 — Get a missing item

Method: GET

URL:

/items/99


Output:

{
    "detail": "Item not found"
}


Status Code: `404 Not Found`

Test Case 4 — Invalid price

Method: POST

Input:

{
    "name": "Laptop",
    "price": -100
}


Expected Result: Validation error because the price must be greater than zero.

Status Code: `422 Unprocessable Content`

Test Case 5 — List items

Method: GET

URL:

/items?limit=10


Expected Result: Returns up to 10 items.

### Time/Space Complexity:

- Time Complexity: O(1) average for dictionary lookup by ID; O(n) for listing items.
- Space Complexity: O(n), because the dictionary stores the items.

## 2. Concept Question

### Question 1: What is the difference between GET, POST, PUT, PATCH, and DELETE?

Answer:

HTTP methods describe the action that a client wants to perform on a server.

- **GET:** Used to retrieve data.
- **POST:** Used to create or submit data.
- **PUT:** Used to replace an existing resource.
- **PATCH:** Used to partially update a resource.
- **DELETE:** Used to delete a resource.

### Question 2: What are HTTP status codes?

**Answer:**

HTTP status codes tell the client whether a request was successful or whether an error occurred.

- `200 OK` — Request successful.
- `201 Created` — Resource created successfully.
- `400 Bad Request` — Invalid request.
- `401 Unauthorized` — Authentication is missing or invalid.
- `403 Forbidden` — User does not have permission.
- `404 Not Found` — Resource not found.
- `409 Conflict` — Request conflicts with the current resource state.
- `422 Unprocessable Content` — Request data failed validation.
- `500 Internal Server Error` — Server-side error.

### Question 3: What is the difference between path parameters and query parameters?

**Answer:**

A path parameter identifies a particular resource.

Example:

/items/12


Here, `12` is the path parameter.

A query parameter is commonly used to filter or limit results.

Example:

/items?limit=20


Here, `limit` is the query parameter.

### Question 4: What is Pydantic?

**Answer:**

Pydantic is a Python library used to validate and parse data. FastAPI uses Pydantic models to validate incoming request data.

Example:

from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)

Here, the name must contain at least one character and the price must be greater than zero.

### Question 5: What is response_model in FastAPI?

**Answer:**

`response_model` defines the expected structure of the API response. It helps validate and filter the returned data so that unwanted internal fields are not exposed.

### Question 6: What is HTTPException?

**Answer:**

`HTTPException` is used to return an HTTP error response with a specific status code and message.

Example:

raise HTTPException(
    status_code=404,
    detail="Product not found"
)


### Question 7: What is UploadFile?

**Answer:**

`UploadFile` is used in FastAPI to receive uploaded files. It provides file information such as filename and content type, along with a file-like interface.

## 3. Debugging Challenge

### Issue:

The PDF contains the following incorrect condition:

if product_id = 0:
    return {"error": "invalid"}

There are two issues:

1. A single `=` is used instead of a comparison operator.
2. The endpoint does not return a clear HTTP error status.

### Fix:

Use `<=` to check whether the product ID is zero or negative. Use `HTTPException` to return a proper error response.

from fastapi import HTTPException

@app.get("/products/{product_id}")
def read_product(product_id: int):
    if product_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="product_id must be positive"
        )

    return {"id": product_id}

## 4. What I Learned

- How HTTP request and response communication works.
- The difference between GET, POST, PUT, PATCH, and DELETE.
- How to understand common HTTP status codes.
- How to create FastAPI routes using decorators.
- The difference between path parameters and query parameters.
- How to use Pydantic models for request validation.
- How to use `Field()` for validation rules.
- How to use `response_model` to control API responses.
- How to handle errors using `HTTPException`.
- How to receive uploaded files using `UploadFile`.
- How to read form data, headers, and cookies.

## 5. What I Found Difficult

I need more practice understanding:

- How HTTP requests and responses work.
- The difference between path parameters and query parameters.
- How Pydantic validates incoming data.
- How `BaseModel` and `Field()` work together.
- How `response_model` controls API output.
- When to use different HTTP status codes.
- How to handle errors using `HTTPException`.
- How file uploads work in FastAPI.

