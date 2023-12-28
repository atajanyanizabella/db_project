import requests
import json
import string
from randome import choice, randint, uniform
from datetime import datetime, timedelta


def generate_random_date(start_date, end_date):
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    random_days = randint(0, (end_datetime - start_datetime).days)
    random_date = start_datetime + timedelta(days=random_days)

    return random_date.strftime("%Y-%m-%d")



def generate_random_string(size: int):
    characters = string.ascii_lowercase + string.digits
    return "".join(choice(characters) for _ in range(size))


def generate_random_int(min_value, max_value):
    return random.randint(min_value, max_value)

def generate_random_float(min_value, max_value, precision=2):
    random_float = round(random.uniform(min_value, max_value), precision)
    return random_float

ship_names = [
    "Ocean Explorer",
    "Star Voyager",
    "Royal Navigator",
    "Silver Legend",
    "Golden Spirit",
    "Majestic Adventurer",
    "Sapphire Dream",
    "Diamond Discovery",
    "Coral Princess",
    "Emerald Seafarer"
]

ship_types = [
    "Cargo Ship",
    "Container Ship",
    "Cruise Ship",
    "Fishing Boat",
    "Sailboat",
    "Yacht",
    "Submarine",
    "Oil Tanker",
    "Ferry",
    "Naval Warship"
]

captains = [
    "James Smith",
    "Emily Johnson",
    "Michael Davis",
    "Olivia Wilson",
    "Benjamin Turner",
    "Sophia Miller",
    "Noah Harris",
    "Ava Clark",
    "William Martin",
    "Isabella Taylor"
]

port_names = [
    "Port Harbor",
    "Coastal Gateway",
    "Seaside Haven",
    "Maritime Point",
    "Harbor City",
    "Nautical Bay",
    "Oceanfront Terminal",
    "Island Port",
    "Seaport Village",
    "Coastal Marina"
]

port_cities = [
    "Harborville",
    "Coastalburg",
    "Seaview City",
    "Maritimeopolis",
    "Baytown",
    "Oceanfront Springs",
    "Portborough",
    "Island Bay City",
    "Seaside Haven",
    "Coastalopolis"
]

port_categories = [
    "Cargo",
    "Passenger",
    "Fishing",
    "Container Terminal",
    "Cruise Terminal"
]

arrival_purposes = [
    "Unloading Cargo",
    "Passenger Embarkation",
    "Fishing Operations",
    "Port Call for Repairs",
    "Tourism Visit"
]


for _ in range(1000):
    data = {}
    data["name"] = choice(ship_names) + "-" + generate_random_string(10)
    data["displacement"] = generate_random_int(2000, 9000)
    data["home_port"] = choice(port_names) + "-" + generate_random_string(10)
    data["ship_type"] = choice(ship_types) + "-" + generate_random_string(10)
    data["captain"] = choice(captains) + "-" + generate_random_string(10)

    response = requests.post(f"http://127.0.0.1:8000/ships", data=json.dumps(data))
    return response

for _ in range(1000):
    data = {}
    data["name"] = choice(port_names) + "-" + generate_random_string(10)
    data["city"] = choice(port_cities)
    data["category"] = choice(categories)
    data["day_price"] = generate_random_float(10000, 60000)

    response = requests.post(f"http://127.0.0.1:8000/ports", data=json.dumps(data))
    return response

for _ in range(10000):
    data = {}
    data["berth_number"] = generate_random_int(0, 20000)
    data["arrival_date"] = generate_random_date("2023-12-12", "2024-10-12")
    data["departure_date"] = generate_random_date("2023-01-01", "2023-12-12")
    data["arrival_purpose"] = choice(arrival_purposes) + "-" + generate_random_string(10)

    response = requests.post(f"http://127.0.0.1:8000/arrivals", data=json.dumps(data))
    return response
