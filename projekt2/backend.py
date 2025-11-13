from pymongo import MongoClient
from datetime import datetime, timedelta

# --- Anslut till MongoDB ---
def get_database():
    uri = "mongodb+srv://ericrocklind_db_user:pass123@matsvinn.xlizucx.mongodb.net/"
    client = MongoClient(uri)
    db = client['matsvinn']
    return db['matavfall']  # returnerar collection

# --- Databasfunktioner ---

def add_entry(collection, date, amount):
    """Lägg till en ny post i databasen.""" 
    datetime_obj = datetime.combine(date, datetime.min.time())
    collection.insert_one({"datum": datetime_obj, "mat_slängt_kg": amount})

def get_total(collection):
    """Returnerar totalt slängd mat."""
    total = 0
    for doc in collection.find():
        total += doc.get("mat_slängt_kg", 0)
    return total

def get_total_in_period(collection, days):
    """Returnerar totalt slängd mat inom senaste X dagar."""
    cutoff = datetime.now() - timedelta(days=days)
    total = 0
    for doc in collection.find():
        doc_date = doc["datum"]
        if doc_date >= cutoff:
            total += doc.get("mat_slängt_kg", 0)
    return total

def get_total_on_date(collection, date):
    """Returnerar totalen för ett specifikt datum."""
    selected_datetime = datetime.combine(date, datetime.min.time())
    total = 0
    for doc in collection.find():
        if doc["datum"].date() == selected_datetime.date():
            total += doc.get("mat_slängt_kg", 0)
    return total
