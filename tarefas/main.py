from fastapi import FastAPI
from tarefas.routes import router

app = FastAPI()
app.include_router(router)