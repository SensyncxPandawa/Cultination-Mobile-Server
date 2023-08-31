import json
import os
from datetime import datetime

class EnumeratorCache:
    def __init__(self):
        self.enums = {}

    def update_enumerator_by_enum_name(self, enum_name: str, enum_data):
        self.enums[enum_name] = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": enum_data
        }
        self._write_to_file(enum_name, enum_data)
        return self.enums[enum_name]

    def _write_to_file(self, enum_name, enum_data):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        enum_file = "data/" + enum_name + ".json"
        file_path = os.path.join(current_dir, enum_file)
        with open(file_path, "w") as file:
            json.dump({enum_name: enum_data}, file, indent=4)

    def get_all_latest_enumerator(self):
        return self.enums

    def get_specific_latest_enumerator_by_enum_name(self, enum_name: str):
        return self.enums.get(enum_name, {})

# Load fish type data from the JSON file
def load_data(enum_name: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    enum_file = "data/" + enum_name + ".json"
    file_path = os.path.join(current_dir, enum_file)
    with open(file_path, "r") as file:
        data = json.load(file)
    return data.get(enum_name, {})

# Initialize the cache
cache = EnumeratorCache()

# Load all data from the JSON file
city_data = load_data("city")
fish_size_preference_data = load_data("fish_size_preference")
fish_type_data = load_data("fish_type")
market_preference_data = load_data("market_preference")
pond_size_range_data = load_data("pond_size_range")
pond_total_data = load_data("pond_total")
proficiency_level_data = load_data("proficiency_level")
province_city_data = load_data("province_city")
province_data = load_data("province")

# Update the cache
cache.update_enumerator_by_enum_name("city", city_data)
cache.update_enumerator_by_enum_name("fish_size_preference", fish_size_preference_data)
cache.update_enumerator_by_enum_name("fish_type", fish_type_data)
cache.update_enumerator_by_enum_name("market_preference", market_preference_data)
cache.update_enumerator_by_enum_name("pond_size_range", pond_size_range_data)
cache.update_enumerator_by_enum_name("pond_total", pond_total_data)
cache.update_enumerator_by_enum_name("proficiency_level", proficiency_level_data)
cache.update_enumerator_by_enum_name("province_city", province_city_data)
cache.update_enumerator_by_enum_name("province", province_data)

# Update Community Cache
def update_enumerator_by_enum_name(enum_name: str, enum_data):
    return cache.update_enumerator_by_enum_name(enum_name, enum_data)

# Display Community Cache
def get_all_latest_enumerator():
    return cache.get_all_latest_enumerator()

def get_specific_latest_enumerator_by_enum_name(enum_name: str):
    return cache.get_specific_latest_enumerator_by_enum_name(enum_name)
