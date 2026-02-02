from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from timers.timer_manager import TimerManager
from recipes.substitutions import get_substitutes
import os
import json

app = FastAPI(title="Voice-Controlled Smart Kitchen API")

# Simple in-memory timer manager (stub)
tm = TimerManager()

# Pantry persistence (simple JSON file)
PANTRY_FILE = os.path.join(os.path.dirname(__file__), "..", "pantry.json")


def read_pantry():
    try:
        with open(os.path.abspath(PANTRY_FILE), "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"items": []}


def write_pantry(data):
    with open(os.path.abspath(PANTRY_FILE), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# Shopping list storage
SHOPPING_FILE = os.path.join(os.path.dirname(__file__), "..", "shopping_list.json")


def read_shopping():
    try:
        with open(os.path.abspath(SHOPPING_FILE), "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"items": []}


def write_shopping(data):
    with open(os.path.abspath(SHOPPING_FILE), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/recipes/search")
def search_recipes(q: str = ""):
    # Placeholder: call recipes.ingest or scaledown lookup
    return {"query": q, "results": []}


class TimerRequest(BaseModel):
    label: str
    seconds: int


@app.post("/timers")
def create_timer(req: TimerRequest):
    if req.seconds <= 0:
        raise HTTPException(status_code=400, detail="seconds must be > 0")
    tm.set_timer(req.label, req.seconds)
    return {"status": "ok", "label": req.label, "seconds": req.seconds}


@app.get("/timers")
def list_timers():
    return {"timers": tm.list_timers()}


@app.get("/iot/devices")
def list_devices():
    # Placeholder for IoT device discovery
    return {"devices": []}


@app.get("/pantry")
def get_pantry():
    return read_pantry()


@app.post("/pantry")
def add_pantry(items: dict):
    # expected body: {"items": ["eggs","milk"]}
    data = read_pantry()
    incoming = items.get("items", [])
    for it in incoming:
        if it not in data["items"]:
            data["items"].append(it)
    write_pantry(data)
    return data


class SubstituteRequest(BaseModel):
    ingredient: str


@app.post("/substitute")
def substitute(req: SubstituteRequest):
    subs = get_substitutes(req.ingredient)
    return {"ingredient": req.ingredient, "substitutes": subs}


@app.post("/shopping_list")
def create_shopping_list(items: dict):
    # expected body: {"items": ["eggs","milk"]}
    pantry = read_pantry()
    needed = items.get("items", [])
    missing = [it for it in needed if it not in pantry.get("items", [])]
    shop = read_shopping()
    for m in missing:
        if m not in shop["items"]:
            shop["items"].append(m)
    write_shopping(shop)
    return {"missing": missing, "shopping_list": shop}


@app.get("/shopping_list")
def get_shopping_list():
    return read_shopping()


@app.get("/shopping_list/export")
def export_shopping_list():
    shop = read_shopping()
    # return CSV string
    lines = ["item"] + shop.get("items", [])
    csv = "\n".join(lines)
    return {"csv": csv}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
