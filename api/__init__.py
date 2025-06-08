from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.tracking import router as tracking_router

import logfire

from dotenv import load_dotenv
import os

load_dotenv()

logfire.configure(
    token=os.environ['LOGFIRE_TOKEN'], 
    scrubbing=False, 
    environment="production",
    distributed_tracing=False
)

app = FastAPI(title="Personal Site Tracking Pixel", version="1.0.0", openapi_url=None)
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tracking_router)    