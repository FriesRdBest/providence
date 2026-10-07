# Providence

A Streamlit-based application.

## Running in GitHub Codespaces

This repository includes a pinned Codespaces configuration (`.devcontainer/`) that sets up a reproducible Python 3.12 environment with all dependencies preinstalled.

1. From the repository page, click **Code** → **Codespaces** → **Create codespace on main**.
2. Wait for the container to build and the `postCreate.sh` script to finish installing dependencies.
3. In the integrated terminal, run:
   ```bash
   streamlit run app.py
   ```
4. Streamlit will open automatically on port 8501 in your browser.

The configuration also installs Ruff and Pytest for linting and testing.
