from fastapi import FastAPI
import sqlite3
app = FastAPI()
con = sqlite3.connect("fights.db")
 
@app.get("/")
def main():
    return"Hello from fight-nepal!"

@app.post("/event")
def create_event():
    return "creating an event"
@app.get("/event/delete")
def delete_event():
    return "deleting and event with id"
@app.get("/event/get-all")
def get_all_events():
    return "all events"

if __name__ == "__main__":
    main()
