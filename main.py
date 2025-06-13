from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Task
from pydantic_models import TaskCreate

# Create the tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency: sesión per request
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/api/v1/tasks")
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
  try:
    task = Task(
      title= task_data.title,
      description= task_data.description,
      completed= task_data.completed
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail=f"Error creating task: {str(e)}"
    )
  
  
@app.get("/api/v1/tasks")
def get_tasks(db: Session = Depends(get_db)):
  return db.query(Task).all()

