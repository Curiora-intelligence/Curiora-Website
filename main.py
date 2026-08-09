from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app=FastAPI(title="saiganesh",docs_url=None,openapi_external_docs=None,redoc_url=None)

app.mount("/static",StaticFiles(directory="static"),name="static")

template=Jinja2Templates(directory="templates")

@app.get("/")
async def home(request:Request):
    return template.TemplateResponse(request,"home.html",{"title":"Curiora"})

@app.get("/research")
async def research(request:Request):
    return template.TemplateResponse(request,"research.html",{"title": "Research — Curiora"})

@app.get("/about")
async def about(request: Request):
    return template.TemplateResponse(request, "about.html",{"title": "About — Curiora" })