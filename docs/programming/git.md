Change git account for repo:
```bash
git config core.sshCommand "ssh -i ~/.ssh/key"
git config user.name "Valentin Lewicki"
git config user.email "vlewicki@vlewicki.ru"
```

GitHub:
```
name: CI
on:
  push:
    branches:
      - master
      - dev
  pull_request:
    branches:
      - master
      - dev

jobs:
  pytest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.13
      - name: Install dependencies
        run: |
          python -m pip install uv
          uv sync
      - name: Run tests
        run: uv run pytest
```
