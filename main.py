import os
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Git MCP Server")

# Read repo root from env
REPO_ROOT = Path(os.getenv("GIT_LOCAL_REPO", "D:/Sundar/MTech/Dissertation/svc-accounting")).resolve()

print("📁 MCP Git Server using repo root:", REPO_ROOT)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class FileRequest(BaseModel):
    repo: str
    path: str

class ListRequest(BaseModel):
    repo: str
    base_path: str
    ext: str

class PRDiffRequest(BaseModel):
    repo: str
    pr_number: int


@app.post("/git-mcp/file")
def get_file(req: FileRequest):
    file_path = REPO_ROOT / req.path
    if not file_path.exists():
        return {"error": f"File not found: {file_path}"}
    return {"content": file_path.read_text(encoding="utf-8")}


@app.post("/git-mcp/list")
def list_files(req: ListRequest):
    base = REPO_ROOT / req.base_path
    if not base.exists():
        return {"files": []}

    files = [
        str(p.relative_to(REPO_ROOT))
        for p in base.rglob(f"*{req.ext}")
    ]
    return {"files": files}


@app.post("/git-mcp/pr-diff")
def get_pr_diff(req: PRDiffRequest):
    # Optional: implement real PR diff using GitPython or pygit2
    return {"diff": "// TODO: implement PR diff support"}
