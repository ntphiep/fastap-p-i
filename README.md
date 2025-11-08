## Install `uv`

```bash
pip install uv
``` 

or

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Base

Init:


```bash
uv init fastapi-vip
```

Add dependencies:


```bash
uv add fastapi uvicorn[standard] pydantic loguru httpx python-multipart
uv add --dev pytest pytest-asyncio black isort ruff
```

Sync and lock dependencies:

```bash
uv sync
uv lock
```

Run `dev` environment server:

```bash
uv run uvicorn app.main:app --reload
```

