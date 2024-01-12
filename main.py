from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.routing import APIRoute
from fastapi.security import HTTPBasic, HTTPBasicCredentials
app = FastAPI()

description = """
Customer Loyalty API helps you do awesome stuff. 🚀

## Customers

This API allows you to view the loyalty information . You will be able to:

* **View a customer**
* **Add a customer** (_not implemented_)
* **Edit a customer** (_not implemented_)
"""

app = FastAPI(
    title="Customer Loyalty",
    description=description,
    version="1.8",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Gerry Baird",
        "url": "https://github.com/gerry-baird/employee-eligibility-api",
        "email": "gerry.baird@uk.ibm.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

security = HTTPBasic()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
