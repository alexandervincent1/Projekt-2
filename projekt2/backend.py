from pymongo import MongoClient
from datetime import datetime, timedelta

# --- Connect to MongoDB ---
def get_database():
    uri = "mongodb+srv://eriq:pass123@cluster0.eak0s2o.mongodb.net/"
    client = MongoClient(uri)
    db = client['food_waste']  # Updated to match your generator
    return db['school_lunches']  # Updated to match your generator

# --- Database functions ---

def add_entry(collection, date, meal, students_total, students_ate, food_waste_kg):
    """Add a new meal entry."""
    datetime_obj = datetime.combine(date, datetime.min.time())
    collection.insert_one({
        "datum": datetime_obj,            # matches generator
        "meal": meal,
        "students_total": students_total,
        "students_ate": students_ate,
        "mat_slängt_kg": food_waste_kg   # matches generator
    })

def get_total_food_waste(collection):
    """Total food waste."""
    total = 0
    for doc in collection.find():
        total += doc.get("mat_slängt_kg", 0)
    return total

def get_total_students_ate(collection):
    """Total students who ate."""
    total = 0
    for doc in collection.find():
        total += doc.get("students_ate", 0)
    return total

def get_average_food_waste_per_meal(collection):
    """Average food waste per student."""
    total_waste = 0
    total_students = 0
    for doc in collection.find():
        total_waste += doc.get("mat_slängt_kg", 0)
        total_students += doc.get("students_ate", 0)
    if total_students == 0:
        return 0
    return total_waste / 800

def get_total_in_period(collection, days):
    """Total food waste and students for last N days."""
    cutoff = datetime.now() - timedelta(days=days)
    total_waste = 0
    total_students = 0
    # Query using 'datum' field
    for doc in collection.find({"datum": {"$gte": cutoff}}):
        total_waste += doc.get("mat_slängt_kg", 0)
        total_students += doc.get("students_ate", 0)
    return total_waste, total_students

def get_total_on_date(collection, date):
    """Total food waste and students for a specific date."""
    start_datetime = datetime.combine(date, datetime.min.time())
    end_datetime = start_datetime + timedelta(days=1)

    total_waste = 0
    total_students = 0

    query = {
        "datum": {
            "$gte": start_datetime,
            "$lt": end_datetime
        }
    }

    for doc in collection.find(query):
        total_waste += doc.get("mat_slängt_kg", 0)
        total_students += doc.get("students_ate", 0)
    return total_waste, total_students
