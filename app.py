from pathlib import Path
import traceback
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates #used to generate HTML pages
from pydantic import BaseModel #checks that incoming data has the correct format and type before your code uses it

from backend import run_travel_agent


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="TripMate AI",
    description="LangGraph Multi-Agent Travel Planner with FastAPI Frontend",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)


templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

#Whenever someone sends data to this API, this is what I expect the data to look like
class TravelRequest(BaseModel):
    message: str
    thread_id: str | None = None

