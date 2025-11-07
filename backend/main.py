from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend import chart

# Create FastAPI app
app = FastAPI(title="Astrolog API", version="0.1.0")

# --- CORS (allow frontend access) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",  # use specific origins later for security, e.g. "https://your-vercel-app.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Request model ---
class BirthData(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    latitude: float
    longitude: float

# --- Root route ---
@app.get("/")
def home():
    return {"message": "Welcome to Astrolog API"}

# --- Main endpoint ---
@app.post("/api/chart")
def create_chart(data: BirthData):
    try:
        result = chart.calculate_chart(
            data.year,
            data.month,
            data.day,
            data.hour,
            data.minute,
            data.latitude,
            data.longitude
        )
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
