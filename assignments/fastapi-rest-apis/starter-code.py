import importlib

fastapi_module = importlib.import_module("fastapi")
pydantic_module = importlib.import_module("pydantic")

FastAPI = fastapi_module.FastAPI
BaseModel = pydantic_module.BaseModel

app = FastAPI(title="Student Task Tracker API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Read FastAPI docs", "completed": False},
    {"id": 2, "title": "Build first endpoint", "completed": True},
    {"id": 3, "title": "Test with Swagger UI", "completed": False},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Task Tracker API"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: TaskCreate):
    next_id = tasks[-1]["id"] + 1 if tasks else 1
    new_task = {
        "id": next_id,
        "title": task.title,
        "completed": task.completed,
    }
    tasks.append(new_task)
    return new_task
