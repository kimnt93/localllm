from fastapi import FastAPI
import uvicorn

from localllm.router import api_router


if __name__ == "__main__":
    app = FastAPI()
    app.include_router(api_router)

    uvicorn.run(app, host='0.0.0.0', port=8000)
