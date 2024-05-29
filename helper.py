import json
class Helper:
    def __init__(self):
        self._helper = None
    
    def check_existing(self, place: str) -> bool:
        with open("password.json", 'r+') as db:
            db_data = json.load(db)
            for data in db_data():
                if data["place"] == place:
                    return True
        return False