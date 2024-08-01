from fastapi import FastAPI
from src.view.healthcheck import router as healthcheck_router
from src.view.persona import router as persona_router

app = FastAPI()

app.include_router(healthcheck_router)
app.include_router(persona_router)
