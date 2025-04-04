from fastapi import FastAPI
from dotenv import load_dotenv
from routes.user_router import user_routes
from routes.post_router import post_routes  

# Load environment variables from .env file
load_dotenv()

# Create FastAPI app instance
app = FastAPI()

# Include the user routes under the prefix '/users'
app.include_router(user_routes, prefix="/users", tags=["User"])
app.include_router(post_routes, prefix="/posts", tags=["Post"])

# Optionally, add more routes or configuration here if needed

# Example: Adding a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
