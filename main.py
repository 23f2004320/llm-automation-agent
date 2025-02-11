from fastapi import FastAPI, HTTPException
import os
import subprocess

app = FastAPI()

DATA_DIR = "data"  # Ensure operations are limited to this directory

@app.post("/run")
async def run_task(task: str):
    try:
        if "format" in task.lower():
            file_path = f"{DATA_DIR}/format.md"
            subprocess.run(["npx", "prettier", "--write", file_path], check=True)
            return {"message": "File formatted successfully"}
        if task.lower() == "a5":
            # Your logic for A5 task
            return {"message": "A5 task executed successfully"}

        return {"error": "Task not recognized"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str):
    full_path = os.path.join(DATA_DIR, path)
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    with open(full_path, "r") as f:
        content = f.read()
    return {"content": content}

@app.delete("/delete")
async def delete_file(path: str):
    full_path = os.path.join(DATA_DIR, path)
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    os.remove(full_path)
    return {"message": "File deleted successfully"}

# Add this to keep the server running:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)