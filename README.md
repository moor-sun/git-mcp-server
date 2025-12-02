# Git MCP Server (FastAPI)

A lightweight FastAPI server that exposes local Git repository operations as MCP-compatible APIs.  
Useful for AI agents or automation systems that need programmatic file access from a Git project.

---

## Features

| Endpoint | Description |
|---------|-------------|
| `POST /git-mcp/file` | Read and return the content of a file from the repository |
| `POST /git-mcp/list` | Recursively list files under a given path (filter by extension) |
| `POST /git-mcp/pr-diff` | Placeholder for PR diff functionality (future enhancement) |

---

## Technology

- Python 3.9+
- FastAPI
- Uvicorn
- Pydantic
- CORS middleware enabled by default

---

## Configuration

Set the environment variable to define your repository root:

### Windows CMD
```cmd
set GIT_LOCAL_REPO=D:\path\to\your\repo
```

### PowerShell
```powershell
$env:GIT_LOCAL_REPO="D:\path\to\your\repo"
```

### Linux / macOS
```bash
export GIT_LOCAL_REPO="/home/user/project"
```

If not set, the default fallback path is:
```
D:/Sundar/MTech/Dissertation/svc-accounting
```

---

## Running the Server

### Install dependencies
```bash
pip install fastapi uvicorn pydantic
```

### Start the server
```bash
uvicorn main:app --reload --port 8003
```

### Open API Docs
Use Swagger UI:

```
http://localhost:8003/docs
```

---

## API Examples

### Fetch a File
```json
POST /git-mcp/file
{
  "repo": "local-repo",
  "path": "src/main/java/Example.java"
}
```

### List Files
```json
POST /git-mcp/list
{
  "repo": "local-repo",
  "base_path": "src",
  "ext": ".java"
}
```

### Pull Request Diff (To be implemented)
```json
POST /git-mcp/pr-diff
{
  "repo": "local-repo",
  "pr_number": 10
}
```

---

## Future Improvements

- Git diff support using GitPython or pygit2
- Branch listing and checkout interfaces
- Search inside repository content
- Binary file handling
- Optional authentication

---

## Contribution

Open to improvements — feel free to extend routes and submit enhancements!
