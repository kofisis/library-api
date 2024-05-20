from fastapi import FastAPI, Body



app = FastAPI()


# root test route
@app.get("/")
async def root():
    return {"message": "hello world"}


# create a user
@app.post("/register")
async def create_user(payload: dict = Body(...)):
    return payload

# GET endpoints 
# 1. /books
# 2. /books/{id}

# POST endpoints
# 1. /registration

# DELETE endpoints
# 1. /books/{id}
