---
title: README.md
homepage: true
---
<!--![](assets/banner.svg)-->

# README.md
To deploy changes:

`uv run mkdocs serve` - Start the live-reloading docs server.

`uv run mkdocs gh-deploy` - Build and push to GitHub gh-pages branch.

## Setup
``` bash
uv add mkdocs mkdocs-material
uv run mkdocs new .
```
## Project layout
```
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    ...       # Other markdown pages, images and other files.
```
