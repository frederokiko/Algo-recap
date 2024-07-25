from contact_model import *
import json

class Contact:
    """
        Classe de gestion des contacts de type CRUD
    """
    def __init__(self, contact_file):
        self.contact_file = contact_file
    
    def _read_contacts(self):
        with open(self.contact_file, 'r') as file:
            return json.load(file)
    
    def _write_contacts(self, data):
        with open(self.contact_file, 'w') as file:
            json.dump(data, file, indent=4)

    def get_list(self):
        data = self._read_contacts()
        return {key: {'firstname': value['firstname'], 'lastname': value['lastname']}
                for key, value in data.items()}

    def get(self, contact):
        data = self._read_contacts()
        contact_data = data.get(contact, {})
        if contact_data:
            return Person(contact_data['firstname'], contact_data['lastname'], contact_data['telephone'], contact_data['email'])
        return None        
    
    def update(self, contact_id, updated_person):
        data = self._read_contacts()
        data[contact_id] = {
            "firstname" : updated_person.firstname,
            "lastname" : updated_person.lastname,
            "telephone" : updated_person.telephone,
            "email" : updated_person.email,
        }
        self._write_contacts(data)

    def create(self, person):
        data = self._read_contacts()
        new_id = str(len(data) + 1)
        data[new_id] = {
            "firstname" : person.firstname,
            "lastname" : person.lastname,
            "telephone" : person.telephone,
            "email" : person.email,
        }
        self._write_contacts(data)
    
    def delete(self, contact):
        data = self._read_contacts()
        if contact in data:
            del data[contact]
            self._write_contacts(data)