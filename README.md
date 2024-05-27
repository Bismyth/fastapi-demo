# FastAPI - DEMO

Language Versions used:
- Python: 3.11
- Node: 20.12.2

## Run locally
1. Install dependencies
    -
    <b>Python</b>
    ```bash
    cd backend
    pip install -r requirements.txt
    ```
    <b>Vue</b>
    ```bash
    cd frontend
    npm install
    ```

3. Start Services
    -
    <b>Python (Backend)</b>
    ```bash
    cd backend
    fastapi dev main.py
    ```
    <b>Vue (Frontend)</b>
    ```bash
    cd frontend
    npm run dev
    ```
    Vite is now serving the frontend on port 8080 by default.


## Run using docker compose

Docker compose file definition at the root of the project.

To run the stack:

```bash
docker compose up --build
```

*This will launch the webserver at localhost:8010 by default