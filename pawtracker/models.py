import flask
from Paw_Tracker import db
from werkzeug.security import generate_password_hash, check_password_hash


class Client(db.Document):
    client_First_Name = db.StringField(max_length=50)
    client_Last_Name = db.StringField(max_length=50)
    client_EmailAddress = db.StringField(max_length=50, unique=True)
    client_Password = db.StringField()
    client_Phone = db.StringField()

    def set_password(self, password):
        self.client_Password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.client_Password, password)

class Vet(db.Document):
    vet_First_Name = db.StringField(max_length=50)
    vet_Last_Name = db.StringField(max_length=50)
    vet_EmailAddress = db.StringField(max_length=50, unique=True)
    vet_Street_Address = db.StringField(max_length=50)
    vet_City = db.StringField(max_length=50)
    vet_State = db.StringField(max_length=50)
    vet_Zipcode = db.IntField(max_length=5)
    vet_Phone = db.StringField(max_length=11)

class Services(db.Document):
    service_Name = db.StringField(max_length=50)
    service_Description = db.StringField(max_length=2550)
    service_Length = db.StringField(max_length=50)
    service_Diration = db.StringField(max_length=50)
    service_Single_Price = db.StringField(max_length=50)
    service_Group_Price = db.StringField(max_length=50)

class Notes(db.Document):
    pet_ID = db.ObjectIdField()
    pet_First_Name = db.StringField()
    note_Date = db.StringField()
    note_Notes = db.StringField()

class Records(db.Document):
    pet_Name = db.StringField(max_length=50)
    client_Name = db.StringField(max_length=50)
    vet_Name = db.StringField(max_length=50)
    record = db.StringField()

class Pet(db.Document):
    pet_First_Name = db.StringField(max_length=50)
    pet_Last_Name = db.StringField(max_length=50)
    pet_Breed = db.StringField(max_length=50)
    pet_Gender = db.StringField(max_length=50)
    pet_Age = db.IntField(max_length=2)
    pet_Picture = db.StringField() #ImageField

class Enrollment(db.Document):
    service_Name = db.StringField()
    pet_Name = db.StringField()
    enrolled = db.StringField()
