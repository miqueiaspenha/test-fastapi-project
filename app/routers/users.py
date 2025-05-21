from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

fake_users_db = ["maria", "joão", "ana"]

@router.get("/")
def list_users():
    return fake_users_db

@router.get("/{user_id}")
def get_user(user_id: int):
    if 0 <= user_id < len(fake_users_db):
        return {"user": fake_users_db[user_id]}
    return {"error": "Usuário não encontrado"}