from fastapi import FastAPI, Depends
from config import get_db, get_current_user, common_params

app = FastAPI()

@app.get("/config")
def read_config(db: dict = Depends(get_db), user: dict = Depends(get_current_user), params: dict = Depends(common_params)):
    return {"db": db, "user": user, "params": params}