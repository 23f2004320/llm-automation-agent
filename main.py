from fastapi import FastAPI, HTTPException
import os

def execute_task(task: str):
    # Placeholder implementation of execute_task
    if task == "example":
        return "Task executed successfully"
    else:
        raise ValueError("Invalid task")

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    try:
        # Parse and execute the task
        result = execute_task(task)
        return {"status": "success", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(path, "r") as file:
        content = file.read()
    return {"content": content}