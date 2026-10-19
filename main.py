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
from starlette.authentication import requires, AuthenticationError
from fastapi.responses import HTMLResponse, JSONResponse

from fastapi_authz import CasbinMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware

import api.basic_auth as basic_auth
import casbin
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException

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

@app.exception_handler(AuthenticationError)
async def auth_exception_handler(
    request: Request,
    exc: AuthenticationError,
):
    """Return authentication errors as JSON responses."""
    return JSONResponse(
        content={
            "success": False,
            "message": str(exc),
            "data": [],
        },
        status_code=401,
    )

@app.get("/api")
async def api_index():
    return JSONResponse(
        content={
            "success": True,
            "message": "Endpoint: /",
            "data": [
                {"greeting": "Hello, world."}
            ],
        }
    )


@app.get("/api/ds1/res1")
async def api_ds1_res1():
    return JSONResponse(
        content={
            "success": True,
            "message": "Endpoint: ds1/res1",
            "data": [
                {"greeting": "Resource 1 accessed"}
            ],
        }
    )


@app.get("/api/ds2/res2")
async def api_ds2_res2():
    return JSONResponse(
        content={
            "success": True,
            "message": "Endpoint: ds2/res2",
            "data": [
                {"greeting": "Resource 2 accessed"}
            ],
        }
    )


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
