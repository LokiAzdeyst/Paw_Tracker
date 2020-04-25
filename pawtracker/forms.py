
from flask_wtf import FlaskForm, Form
from wtforms.fields.html5 import DateField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from Paw_Tracker.models import Client, Services, Vet
from Paw_Tracker import db


class loginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=32)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=32)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=8, max=32), EqualTo('password')])
    first_Name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=50)])
    last_Name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=50)])
    phone = StringField("Phone Number", validators=[Length(min=0, max=11)])
    submit = SubmitField("Register Now")

    def validate_email(self, email):
        user = Client.objects(client_EmailAddress=email.data).first()
        if user:
            raise ValidationError("Sorry this email address has already been taken. Please pick another email address.")

class ServicesForm(FlaskForm):
    service_Name = StringField("Service Name", validators=[DataRequired()])
    service_Description = StringField("Service Description", validators=[DataRequired()])
    service_Length = StringField("Service Length", validators=[DataRequired()])
    service_Diration = StringField("Service Diration", validators=[DataRequired()])
    service_Single_Price = StringField("Service Single Price", validators=[DataRequired()])
    service_Group_Price = StringField("Service Group Price", validators=[DataRequired()])
    submit = SubmitField("Add to Database")

class ServicesFormDelete(FlaskForm):
    service_ID = StringField("Service ID")
    service_Name = StringField("Service Name")
    service_Description = StringField("Service Description")
    service_Length = StringField("Service Length")
    service_Diration = StringField("Service Diration")
    service_Single_Price = StringField("Service Single Price")
    service_Group_Price = StringField("Service Group Price")
    submit = SubmitField("Delete from Database")

class ServicesFormEdit(FlaskForm):
    service_ID = StringField("Service ID")
    service_Name = StringField("Service Name")
    service_Description = StringField("Service Description")
    service_Length = StringField("Service Length")
    service_Diration = StringField("Service Diration")
    service_Single_Price = StringField("Service Single Price")
    service_Group_Price = StringField("Service Group Price")
    submit = SubmitField("Update service on Database")

class ServicesFormSelect(FlaskForm):
    service_Name = StringField("Service Name")
    submit = SubmitField("Select service from Database")

class VetForm(FlaskForm):
    vet_First_Name = StringField("Vet First Name")
    vet_Last_Name = StringField("Vet Last Name")
    vet_EmailAddress = StringField("Vet Email Address")
    vet_Street_Address = StringField("Vet Street Address")
    vet_City = StringField("Vet City")
    vet_State = StringField("Vet State")
    vet_Zipcode = StringField("Vet Zip Code")
    vet_Phone = StringField("Vet Phone Number")
    submit = SubmitField("Add a new vet to the Database")

class VetFormDelete(FlaskForm):
    vet_First_Name = StringField("Vet First Name")
    vet_Last_Name = StringField("Vet Last Name")
    vet_EmailAddress = StringField("Vet Email Address")
    vet_Street_Address = StringField("Vet Street Address")
    vet_City = StringField("Vet City")
    vet_State = StringField("Vet State")
    vet_Zipcode = StringField("Vet Zip Code")
    vet_Phone = StringField("Vet Phone Number")
    submit = SubmitField("Delete a vet from the Database")

class VetFormSelect(FlaskForm):
    vet_First_Name = StringField("Vet First Name")
    vet_Last_Name = StringField("Vet Last Name")
    vet_EmailAddress = StringField("Vet Email Address")
    vet_Street_Address = StringField("Vet Street Address")
    vet_City = StringField("Vet City")
    vet_State = StringField("Vet State")
    vet_Zipcode = StringField("Vet Zip Code")
    vet_Phone = StringField("Vet Phone Number")
    submit = SubmitField("Select a vet from the Database")

class VetFormEdit(FlaskForm):
    vet_First_Name = StringField("Vet First Name")
    vet_Last_Name = StringField("Vet Last Name")
    vet_EmailAddress = StringField("Vet Email Address")
    vet_Street_Address = StringField("Vet Street Address")
    vet_City = StringField("Vet City")
    vet_State = StringField("Vet State")
    vet_Zipcode = StringField("Vet Zip Code")
    vet_Phone = StringField("Vet Phone Number")
    submit = SubmitField("Update vet information in the Database")

class PetForm(FlaskForm):
    pet_First_Name = StringField("First Name",validators=[DataRequired()])
    pet_Last_Name = StringField("Last Name",validators=[DataRequired()])
    pet_Breed = StringField("Breed",validators=[DataRequired()])
    pet_Gender = StringField("Gender",validators=[DataRequired()])
    pet_Age = StringField("Age",validators=[DataRequired()])
    pet_Picture = StringField("Picture")
    submit = SubmitField("Add a new pet")

class PetFormSelect(FlaskForm):
    pet_First_Name = StringField("First Name",validators=[DataRequired()])
    pet_Last_Name = StringField("Last Name")
    pet_Breed = StringField("Breed")
    pet_Gender = StringField("Gender")
    pet_Age = StringField("Age")
    pet_Picture = StringField("Picture")
    submit = SubmitField("Select a pet")

class PetFormDelete(FlaskForm):
    pet_First_Name = StringField("First Name",validators=[DataRequired()])
    pet_Last_Name = StringField("Last Name",validators=[DataRequired()])
    pet_Breed = StringField("Breed")
    pet_Gender = StringField("Gender")
    pet_Age = StringField("Age")
    pet_Picture = StringField("Picture")
    submit = SubmitField("Delete pet information")

class PetFormEdit(FlaskForm):
    pet_First_Name = StringField("First Name",validators=[DataRequired()])
    pet_Last_Name = StringField("Last Name",validators=[DataRequired()])
    pet_Breed = StringField("Breed",validators=[DataRequired()])
    pet_Gender = StringField("Gender",validators=[DataRequired()])
    pet_Age = StringField("Age",validators=[DataRequired()])
    pet_Picture = StringField("Picture")
    submit = SubmitField("Edit pet information")

class NoteForm(FlaskForm):
    pet_First_Name = StringField("Pet First Name",validators=[DataRequired()])
    note_Date = DateField("Date", validators=[DataRequired()])
    note_Notes = StringField("Notes",validators=[DataRequired()])
    submit = SubmitField("Add a new note")

class NoteFormSelect(FlaskForm):
    pet_First_Name = StringField("Pet First Name",validators=[DataRequired()])
    note_Date = DateField("Date", validators=[DataRequired()])
    note_Notes = StringField("Notes")
    submit = SubmitField("Select a note")

class NoteFormDelete(FlaskForm):
    pet_First_Name = StringField("Pet First Name",validators=[DataRequired()])
    note_Date = DateField("Date", validators=[DataRequired()])
    note_Notes = StringField("Notes")
    submit = SubmitField("Delete note information")

class NoteFormEdit(FlaskForm):
    pet_ID = StringField()
    pet_First_Name = StringField("Pet First Name")
    note_Date = DateField("Date")
    note_Notes = StringField("Notes")
    submit = SubmitField("Edit note information")