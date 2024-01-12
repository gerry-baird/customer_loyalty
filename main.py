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
        "url": "https://github.com/gerry-baird/customer_loyalty",
        "email": "gerry.baird@uk.ibm.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

security = HTTPBasic()

class Customer_Loyalty(BaseModel):
    id: str
    name: str
    total_products: int
    relationship_length: int
    customer_age: int
    current_products: int

class Message(BaseModel):
    message: str

def regenCustomers():
    return [
        Customer_Loyalty(id="abc1234", name="Fred", total_products=4, relationship_length=36,
                  customer_age=55, current_products=2)
        ]


# this is our datastore
pre_baked_customers = regenCustomers()

@app.get("/",
         summary='Customer Loyalty Ping',
         description='Customer Loyalty Ping',
         response_description="Customer Loyalty Ping",
         tags=["Hello World"]
         )
async def greeting(credentials: HTTPBasicCredentials = Depends(security)) -> Message:
    return {"message": "Customer Loyalty is Alive"}


@app.get("/customer/{id}",
         summary='View a customer',
         description='View a customer',
         response_description="The customer loyalty details",
         tags=["Customer"]
         )
def get_customer(id: str) -> Customer_Loyalty:
    for customer in pre_baked_customers:
        if customer.id.lower() == id.lower():
            return customer

    raise HTTPException(status_code=404, detail="Candidate not found")