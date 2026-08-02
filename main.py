from fastapi import (
    FastAPI,
    Form,
    HTTPException,
    status,
    Depends,
)

from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from utils.security import (
    create_access_token,
    verify_access_token,
)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# -----------------------------
# Models
# -----------------------------
class User(BaseModel):
    id: int
    name: str
    email: str


class UserUpdate(BaseModel):
    name: str
    email: str


# -----------------------------
# Sample Data
# -----------------------------
users = [
    User(
        id=1,
        name="Dinesh",
        email="dinesh@gmail.com"
    ),
    User(
        id=2,
        name="Rahul",
        email="rahul@gmail.com"
    ),
    User(
        id=3,
        name="Amit",
        email="amit@gmail.com"
    ),
]


# -----------------------------
# Home API
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to Demo API"
    }


# -----------------------------
# Login API (JWT)
# -----------------------------
@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):

    if username == "admin" and password == "admin123":

        access_token = create_access_token(
            data={
                "sub": username
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password"
    )


# -----------------------------
# Protected Profile API
# -----------------------------
@app.get("/profile")
def get_profile(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_access_token(token)

    username = payload.get("sub")

    return {
        "message": "Profile fetched successfully",
        "username": username
    }


# -----------------------------
# Get All Users
# -----------------------------
@app.get("/users")
def get_users():
    return users


# -----------------------------
# Get User By ID
# -----------------------------
@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:

        if user.id == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


# -----------------------------
# Create User
# -----------------------------
@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)
def create_user(user: User):

    users.append(user)

    return {
        "message": "User added successfully",
        "user": user
    }


# -----------------------------
# Update User
# -----------------------------
@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    updated_user: UserUpdate
):

    for user in users:

        if user.id == user_id:

            user.name = updated_user.name
            user.email = updated_user.email

            return {
                "message": "User updated successfully",
                "user": user
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


# -----------------------------
# Delete User
# -----------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:

        if user.id == user_id:

            users.remove(user)

            return {
                "message": "User deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )