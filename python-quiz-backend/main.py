from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

# Create the API
app = FastAPI()

# Allow your frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This will handle requests from your Lovable frontend
@app.get("/")
def root():
    return {"message": "Backend is running!", "status": "online"}

@app.get("/get-data")
def get_data():
    # This is where you'll put your Streamlit logic later
    return {"message": "Hello from your backend!", "status": "connected", "data": [1, 2, 3, 4, 5]}

@app.post("/send-data")
def send_data(data: dict):
    # This is where you'll process data from your frontend
    print(f"Received from frontend: {data}")
    return {"response": f"Backend received: {data}", "status": "success"}

# For deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
