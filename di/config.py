from fastapi import Depends

def get_db():
    # Esstablish a database connection here
    return {"db": "connected"}

def get_current_user(token: str = "fake-token"):
    # Some auth
    if token != "fake-token":
        return None
    return {"user": "dat"}

def common_params(q: str = "Dummy"):
    return {"q": q}