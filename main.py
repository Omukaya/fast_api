from enum import Enum
from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello, World!"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# @app.get("/users/me")
# async def read_users_me():
#     return {"user_id": "Current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
    
#     return {"model_name": model_name, "message": "Have some residuals"}

# Query parameters with default values
# fake_items_db = [
#     {"item_name": "Sony"},
#     {"item_name": "Vitron"},
#     {"item_name": "V8"},
# ]

# @app.get("/items/")
# async def read_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

# Query parameter with optional parameter
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# Query parameters type conversion
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}

#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "This is an amaizing item that has long description"

#             }
#         )
#     return item

# Multiple paths and query parameters
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     item_id: int, user_id: str, q: str | None = None, short: bool = False
# ):
#     item = {
#         "item_id": item_id,
#         "owner_id": user_id
#     }

#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "This is an amaizing item that has a long description."
#             }
#         )
#     return item

# Required query parameters
@app.get("/items/{item_id}")
async def read_items(item_id: int, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return  item

