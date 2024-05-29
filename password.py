import json, uuid, helper
from ende import Ende
class Password:
    def __init__(self, name, password, place):
        self._name = name
        self._password = Ende.encrypt(password)
        self._place = place
        self._id = uuid.uuid5().hex
    
    @property
    def name(self):
        return self._name
    @property
    def password(self):
        return self._password
    @property
    def place(self):
        return self._place
    @property
    def id(self):
        return self._id
    
    @name.setter
    def name(self, newName: str):
        self._name = newName
    @password.setter
    def password(self, newPassword: str):
        self._password = newPassword
    @place.setter
    def place(self, newPlace: str):
        self._place = newPlace

    def append_data(self) -> bool:
        formatted = { "id": self.id, "place": self.place, "name": self.name, "password": self.password }
        if(helper.Helper.check_existing(place=self.place)):
            return False
        with open('password.json', 'r+') as db:
            db_data = json.load(db)
            db_data.append(formatted)
            db.seek(0)
            try:
                json.dump(db_data, db, ident=4)
                return True
            except Exception:
                return False
    
    def delete_data(self, place: str) -> bool:
        if(not helper.Helper.check_existing(place=place)):
            return False
        with open('password.json', 'r+') as db:
            db_data = json.load(db)
            for data in db_data:
                if(data['place'] == place):
                    db_data.remove(data)
                    db.seek(0)
                    try:
                        json.dump(db_data, db, ident=4)
                        return True
                    except Exception:
                        return False
        return False
    
    def update_data(self, place: str, key: str, newInfo: str) -> bool:
        if(not helper.Helper.check_existing(place=place)):
            return False
        with open('passwords.json', 'r+') as db:
            db_data = json.load(db)
            for data in db_data:
                if(data['place'] == place):
                    data[key] = newInfo
                    db.seek(0)
                    try:
                        json.dump(db_data, db, ident=4)
                        db.truncate()
                        return True
                    except Exception:
                        return False
        return False
