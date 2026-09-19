from fastapi import FastAPI
import uvicorn

from app.Models import CustomerModel

app = FastAPI()


@app.get("/health")
def health_check():
    return {"message": "Health is good"}


@app.post("/add-customer")
def AddCustomer(body: CustomerModel):
    return {"message": f"Nice meeting you {body.Email}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
