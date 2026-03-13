from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import router
from config.settings import APP_NAME, API_VERSION


# CREATE FASTAPI APP

app = FastAPI(
    title=APP_NAME,
    version=API_VERSION,
    description="AI Slide Tutor Backend API"
)



# ENABLE CORS (for frontend communication)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# REGISTER ROUTES


app.include_router(router)



# ROOT ENDPOINT


@app.get("/")
def root():
    return {
        "message": "AI Slide Tutor Backend Running",
        "version": API_VERSION
    }