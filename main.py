"""
 Assessment Title: Portfolio Part 3
 Cluster:          Intermediate RIoT
 Qualification:    ICT50220 Diploma of Information Technology (Advanced Programming)
 Name:             Nelson Gomez
 Student ID:       20149093
 Year/Semester:    2026/S2

 YOUR SUMMARY OF PORTFOLIO ACTIVITY
 GOES HERE

"""

# Imports
from fastapi_authz import CasbinMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware

import api.basic_auth as basic_auth
import casbin
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Global CONSTANTS


## Global Variables

app = FastAPI(title="NGG-InterRIot-AT2_POR-Pt3-2026-S2")

enforcer = casbin.Enforcer(
    "api/rbac_model.conf",
    "api/rbac_policy.csv",
)

backend = basic_auth.BasicAuth()

app.add_middleware(CasbinMiddleware, enforcer=enforcer)
app.add_middleware(AuthenticationMiddleware, backend=backend)

BASE_PATH = Path(__file__).parent
print(BASE_PATH)

app.mount("/static",
          StaticFiles(directory="static"),
          name="static")

app.mount("/css",
          StaticFiles(directory="static/css"),
          name="css")
app.mount("/js",
          StaticFiles(directory="static/js"),
          name="js")
app.mount("/images",
          StaticFiles(directory="static/img"),
          name="images")

TEMPLATES = Jinja2Templates(directory="templates")


# Functions/Methods

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return TEMPLATES.TemplateResponse(
        request=request,
        name="pages/home.html"
    )

@app.get("/api")
async def api_index():
    return {
        "success": True,
        "message": "Welcome",
        "data": [
            {"greeting": "Hello, world."}
        ],
    }

@app.get("/api/ds1/res1")
async def api_ds1_res1():
    return "Resource 1 accessed"


@app.get("/api/ds2/res2")
async def api_ds2_res2():
    return "Resource 2 accessed"


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return TEMPLATES.TemplateResponse(
        request=request,
        name="pages/about.html"
    )

@app.get("/api/data")
async def api_data(request: Request):
    return { 'name':'Frank Spencer' }

# Main Code
