# FastAPI Image
```bash
# Setup environment
uv init --package vlewicki
cd vlewicki
uv add 'fastapi[standard]'
```

```python
# main.py
from vlewicki import app
```


```Dockerfile
# Dockerfile
FROM alpine:latest
RUN apk add python3 uv

WORKDIR /app
COPY ./pyproject.toml \
    ./uv.lock \
    ./.python-version \
    ./main.py \
    ./README.md \
    ./

COPY ./src \
    /app/src

RUN uv sync

CMD ["uv", "run", "fastapi", "run", "--host", "0.0.0.0"]
```

``` bash
# Building image
docker build -t vlewicki:0.1.0 .
docker run --rm -p 8000:8000 vlewicki:0.1.0
docker run -p 8000:8000 vlewicki:0.1.0 uv run fastapi dev --host 0.0.0.0
```
