from fastapi import HTTPException, status
from fastapi.security import HTTPBasicCredentials

# In-memory users for demo
USERS = {
    "appscrip_user": "secure123"
}

def verify_user(credentials: HTTPBasicCredentials) -> str:
    username = credentials.username
    password = credentials.password

    if username in USERS and USERS[username] == password:
        return username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password.",
        headers={"WWW-Authenticate": "Basic"},
    )
