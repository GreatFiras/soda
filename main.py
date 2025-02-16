from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from API.routes import router

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
async def home():
    return {"message": "FastAPI is running!"}
