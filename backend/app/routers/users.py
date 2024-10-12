from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import jwt
from jwt import PyJWTError

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserDetail
from app.schemas.token import Token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/users/", response_model=UserDetail)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    db_user = db.query(User).filter(
        User.username == user.username
    ).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Crear un nuevo usuario
    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, email=user.email,
                    password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + \
            timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
) -> Token:
    username = form_data.username
    plain_password = form_data.password
    db_user = db.query(User).filter(
        User.username == username
    ).first()
    if db_user:
        if pwd_context.verify(plain_password, db_user.password):
            access_token_expires = timedelta(
                minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": db_user.username},
                expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=403, detail="Usuario o contraseña incorrecto"
    )


def get_current_user(
        token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    """
    Extract the current user from the JWT token.
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        # Decode the JWT token to get the user data
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception

    # Query the user from the database using the username from the token
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user


@router.get("/me", response_model=UserDetail)
def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Get details of the logged-in user.
    """
    return current_user
