# SH2404-Astrophysics

## Notebook Environment

This project uses a local virtual environment for `RadTransferII23.ipynb`.

Create or update the environment with `uv`:

```bash
uv sync
```

Register it as a Jupyter kernel:

```bash
uv run python -m ipykernel install --sys-prefix --name sh2404-astrophysics --display-name "Python (.venv SH2404 Astrophysics)"
```

Then open `RadTransferII23.ipynb` and select the kernel named `Python (.venv SH2404 Astrophysics)`.

To use the environment from a terminal:

```bash
source .venv/bin/activate
```