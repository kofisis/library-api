import json
from pprint import pprint

from fastapi import FastAPI

from schema.schema import ReadersSchema

app = FastAPI()


# root test route
@app.get("/")
async def root():
    return registration_table


# store registration data locally
registration_table = [{}]


# create a user
@app.post("/register")
async def create_user(payload: ReadersSchema):
    new_data = registration_table.append(payload.dict())
    return payload

# GET endpoints 
# 1. /books
# 2. /books/{id}

# POST endpoints
# 1. /registration

# DELETE endpoints
# 1. /books/{id}
