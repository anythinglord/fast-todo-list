# Todo List Api powered by FastAPI

A simple and efficient **ToDo List REST API** built using [FastAPI](https://fastapi.tiangolo.com/) and [SQLite](https://www.sqlite.org/index.html). Designed for quick prototyping and learning modern Python web development with async capabilities.

---

## 🚀 Features

- Create, Read, Update, Delete (CRUD) tasks
- SQLite database (local, lightweight)
- Auto-generated interactive docs (Swagger / ReDoc)
- FastAPI dependency injection and response models
- Modular and extensible code structure

---

## 🧱 Tech Stack

- **FastAPI** — modern, fast web framework for building APIs
- **SQLite** — local embedded database
- **SQLAlchemy** — ORM for database interaction
- **Pydantic** — for data validation
- **Uvicorn** — ASGI server for FastAPI

---

## 📁 Project Structure

```bash
├── main.py # FastAPI application
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic models
├── database.py # DB connection and session
├── crud.py # CRUD operation logic
└── README.md
```

---

## 🧪 Installation & Running Locally

1. **Clone the repo**

```bash
git clone https://github.com/anythinglord/fast-todo-list.git
cd fast-todo-list
```

2. **Create virtual env**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the API**
```bash
uvicorn main:app --reload
```

5. **Open docs**

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint    | Description       |
| ------ | ----------- | ----------------- |
| GET    | /tasks/     | List all tasks    |
| GET    | /tasks/{id} | Get task by ID    |
| POST   | /tasks/     | Create a new task |
| PUT    | /tasks/{id} | Update task by ID |
| DELETE | /tasks/{id} | Delete task by ID |

## ToDo List (Project Roadmap)

### MVP (Minimum Viable Product)

- [] SQLite database setup
- [] Task model (id, title, description, completed)
- [] CRUD operations
- [] Basic API documentation via FastAPI

## Example Task JSON

```json
{
  "title": "Write README",
  "description": "Create the README file for the FastAPI project",
  "completed": false
}
```

## License

MIT License — free to use, modify and distribute.

## Author
Made with ❤️ by Anythinglord



