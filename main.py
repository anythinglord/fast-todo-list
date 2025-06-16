from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Task
from schemas import TaskCreate, TaskPatch

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

@app.get("/api/v1/tasks/{task_id}")
def get_task(task_id, db: Session = Depends(get_db)):
  return db.query(Task).get(task_id)

@app.patch("/api/v1/tasks/{task_id}")
def update_task(task_id, task_data: TaskPatch, db: Session = Depends(get_db)):
  task = db.query(Task).filter(Task.id == task_id).first()
  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  if task_data.title is not None:
    task.title = task_data.title
  if task_data.description is not None:
    task.title = task_data.description
  if task_data.completed is not None:
    task.completed = task_data.completed
  
  db.commit()
  db.refresh(task)
  return task

@app.delete("/api/v1/tasks/{task_id}")
def delete_task(task_id, db: Session = Depends(get_db)):
  task = db.query(Task).filter(Task.id == task_id).first()
  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  db.delete(task)
  db.commit()
  return {"detail": f"Task with id {task_id} was deleted"}
