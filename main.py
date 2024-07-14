from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session

from core.db.session import session
from core.db.models import Employee

app = FastAPI()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(Employee).all()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)