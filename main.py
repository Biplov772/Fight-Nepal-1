from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

con = sqlite3.connect("fights.db")

def initalize_databse():
    create_event_table = """
    CREATE TABLE events (
        eventName TEXT,
        participantOne TEXT,
        participantTwo TEXT,
        time TEXT,
        winner TEXT
    );
    """

app = FastAPI()


@app.get("/")   
def main():
    return "flight-nepal"


class CreateEventRequest(BaseModel):
    eventName: str
    participantOne: str
    participantTwo: str
    time: str
    winner: str




@app.post("/event")
def create_event(event: CreateEventRequest):
    return event


@app.get("/event/delete")
def delete_event():
    return "delete event"


@app.get("/event/get-all")
def get_all_events():
    return "All event"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
