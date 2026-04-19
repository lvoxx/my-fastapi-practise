from fastapi import FastAPI
from config import DatabaseConfig, UserService
from wireup import Injected
import wireup
import wireup.integration.fastapi

app = FastAPI()

@app.get("/users", summary="Get user information",description="Fetch user details by user ID")
def get_user(user_id: int, user_service: Injected[UserService]):
    return user_service.get_user(user_id)

container = wireup.create_async_container(injectables=[DatabaseConfig, UserService])
wireup.integration.fastapi.setup(container, app)