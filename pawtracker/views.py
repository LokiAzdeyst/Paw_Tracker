"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, url_for, session, request
from Paw_Tracker import app, db
import Paw_Tracker.forms
from Paw_Tracker.models import Client, Services, Vet, Pet, Notes




@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year
    )

@app.route('/register', methods=['GET','POST'])
def register():
    form = Paw_Tracker.forms.RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        First_Name = form.first_Name.data
        Last_Name = form.last_Name.data
        phone = form.phone.data
        user = Client(client_First_Name=First_Name, client_Last_Name=Last_Name, client_EmailAddress=email, client_Phone=phone)
        user.set_password(password)
        user.save()
        return redirect(url_for('home'))
    return render_template(
        'register.html',
        title='register',
        form=form,
        login=True,
        year=datetime.now().year
        )

@app.route('/login', methods=['GET','POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('home'))

    form = Paw_Tracker.forms.loginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = Client.objects(client_EmailAddress=email).first()
        if user and user.get_password(password):
            flash("You have logged in.", "success")
            session['user_id'] = user.client_EmailAddress
            return redirect(url_for('home'))
        else:
            flash("Sorry something went wrong.", "danger")

    return render_template(
    'login.html',
    form=form,
    login=True,
    title='Login',
    year=datetime.now().year
    )

@app.route('/logout')
def logout():
    session['user_id'] = False
    return redirect(url_for('home'))

@app.route('/services')
def services():
    services = Services.objects.all()
    return render_template(
    'services.html',
    services=services,
    login=True,
    title='Login',
    year=datetime.now().year
    )
@app.route('/services/add', methods=['GET','POST'])
def add_Service():
    form = Paw_Tracker.forms.ServicesForm()
    

    if form.validate_on_submit():
        service_Name = form.service_Name.data
        service_Description = form.service_Description.data
        service_Length = form.service_Length.data
        service_Diration = form.service_Diration.data
        service_Single_Price = form.service_Single_Price.data
        service_Group_Price = form.service_Group_Price.data

        service = Services(service_Name=service_Name, service_Description=service_Description, service_Length=service_Length, service_Diration=service_Diration, service_Single_Price=service_Single_Price, service_Group_Price=service_Group_Price)
        service.save()
        flash("Service has been added to the database.", "success")
        return redirect(url_for('services'))
    print(form.data)
    return render_template(
    'servicesadd.html',
    title = "Add a New Service",
    form = form,
    year=datetime.now().year
    )

@app.route('/services/delete', methods=['GET','POST'])
def delete_Service():
    services = Services.objects.all()
    form = Paw_Tracker.forms.ServicesFormDelete()

    if form.validate_on_submit():
        service_Name = form.service_Name.data
        Services.objects.get(service_Name = service_Name).delete()
        flash("Service has been deleted from the database.", "success")
        return redirect(url_for('services'))

    return render_template(
    'servicesdelete.html',
    title = "Delete a Service",
    services = services,
    form = form,
    year=datetime.now().year)

@app.route('/services/select', methods=['GET','POST'])
def select_Service():
    services = Services.objects.all()
    form = Paw_Tracker.forms.ServicesFormSelect()
    data = form.service_Name.data

    if form.validate_on_submit():
        service_Name = Services.objects.get(service_Name = data)
        service_Data = service_Name.service_Name
        print(service_Data)
        return redirect(url_for('edit_Service', service_Name=service_Data))

    return render_template(
    'servicesselect.html',
    title = "Select a Service",
    services = services,
    form = form,
    year=datetime.now().year)

@app.route('/services/edit/<service_Name>', methods=['GET','POST'])
def edit_Service(service_Name):
    service = Services.objects.get(service_Name = service_Name)
    print(service)
    form = Paw_Tracker.forms.ServicesFormEdit( obj=service)


    if request.method == 'POST' and form.validate_on_submit():
        
        record = Services.objects.get(service_Name = service_Name)
        record.service_Name = form.service_Name.data
        record.service_Description = form.service_Description.data
        record.service_Length = form.service_Length.data
        record.service_Diration = form.service_Diration.data
        record.service_Single_Price = form.service_Single_Price.data
        record.service_Group_Price = form.service_Group_Price.data
        record.save()
        return redirect(url_for('services'))

    return render_template(
    'servicesedit.html',
    title = "Edit a Service",
    form = form,
    year=datetime.now().year)

@app.route('/vet',  methods=['GET','POST'])
def vet():
    vet = Vet.objects.all()
    form = Paw_Tracker.forms.VetForm()
    return render_template(
    'vetinfo.html',
    vet=vet,
    form = form,
    login=True,
    title='Login',
    year=datetime.now().year
    )
@app.route('/vet/add',  methods=['GET','POST'])
def add_Vet():
    form = Paw_Tracker.forms.VetForm()
    if form.validate_on_submit():
        vet_First_Name = form.vet_First_Name.data
        vet_Last_Name = form.vet_Last_Name.data
        vet_Street_Address = form.vet_Street_Address.data
        vet_City = form.vet_City.data
        vet_State = form.vet_State.data
        vet_Zipcode = form.vet_Zipcode.data
        vet_EmailAddress = form.vet_EmailAddress.data
        vet_Phone = form.vet_Phone.data

        vet = Vet(vet_First_Name=vet_First_Name, vet_Last_Name=vet_Last_Name, vet_Street_Address=vet_Street_Address, vet_City=vet_City, vet_State=vet_State, vet_Zipcode=vet_Zipcode, vet_EmailAddress=vet_EmailAddress, vet_Phone=vet_Phone)
        vet.save()
        flash("Vet has been added to the database.", "success")
        return redirect(url_for('vet'))
    print(form.data)
    return render_template(
    'vetadd.html',
    title = "Add a new vet",
    form = form,
    year=datetime.now().year
    )
@app.route('/vet/delete',  methods=['GET','POST'])
def delete_Vet():
    vet = Vet.objects.all()
    form = Paw_Tracker.forms.VetFormDelete()

    if form.validate_on_submit():
        vet_First_Name = form.vet_First_Name.data
        vet_Last_Name = form.vet_Last_Name.data
        vet_EmailAddress = form.vet_EmailAddress.data
        print(vet_EmailAddress)
        Vet.objects.get(vet_EmailAddress = vet_EmailAddress, vet_Last_Name = vet_Last_Name, vet_First_Name=vet_First_Name).delete()
        flash("Vet has been deleted from the database.", "success")
        return redirect(url_for('vet'))

    return render_template(
    'vetdelete.html',
    title = "Delete a vet",
    vet = vet,
    form = form,
    year=datetime.now().year)

@app.route('/vet/select', methods=['GET','POST'])
def select_Vet():
    vet = Vet.objects.all()
    form = Paw_Tracker.forms.VetFormSelect()
    data = form.vet_EmailAddress.data

    if form.validate_on_submit():
        vet_EmailAddress = Vet.objects.get(vet_EmailAddress = data)
        vet_Data = vet_EmailAddress.vet_EmailAddress
        print(vet_Data)
        return redirect(url_for('edit_Vet', vet_EmailAddress=vet_Data))

    return render_template(
    'vetselect.html',
    title = "Select a vet",
    vet = vet,
    form = form,
    year=datetime.now().year
    )
@app.route('/vet/edit/<vet_EmailAddress>',  methods=['GET','POST'])
def edit_Vet(vet_EmailAddress):
    vet = Vet.objects.get(vet_EmailAddress = vet_EmailAddress)
    form = Paw_Tracker.forms.VetFormEdit( obj=vet)


    if request.method == 'POST' and form.validate_on_submit():
        
        record = Vet.objects.get(vet_EmailAddress = vet_EmailAddress)
        record.vet_First_Name = form.vet_First_Name.data
        record.vet_Last_Name = form.vet_Last_Name.data
        record.vet_EmailAddress = form.vet_EmailAddress.data
        record.vet_Street_Address = form.vet_Street_Address.data
        record.vet_City = form.vet_City.data
        record.vet_State = form.vet_State.data
        record.vet_Zipcode = form.vet_Zipcode.data
        record.vet_Phone = form.vet_Phone.data
        record.save()
        flash("Record has been updated.","success")
        return redirect(url_for('vet'))

    return render_template(
    'vetedit.html',
    title = "Edit a vet",
    form = form,
    year=datetime.now().year)

@app.route('/pet', methods=['GET','POST'])
def pet():
    pet = Pet.objects.all()
    form = Paw_Tracker.forms.PetForm()
    return render_template(
        'pets.html',
        pet = pet,
        form = form,
        login=True,
        title='Add Pet Information',
        year=datetime.now().year
        )
@app.route('/pet/add', methods=['GET','POST'])
def add_Pet():
    form = Paw_Tracker.forms.PetForm()
    if form.validate_on_submit():
        pet_First_Name = form.pet_First_Name.data
        pet_Last_Name = form.pet_Last_Name.data
        pet_Breed = form.pet_Breed.data
        pet_Gender = form.pet_Gender.data
        pet_Age = form.pet_Age.data
        pet_Picture = form.pet_Picture.data

        pet = Pet(pet_First_Name=pet_First_Name, pet_Last_Name=pet_Last_Name, pet_Breed=pet_Breed, pet_Gender=pet_Gender, pet_Age=pet_Age, pet_Picture=pet_Picture)
        pet.save()
        flash("Pet has been added to the database.", "success")
        return redirect(url_for('pet'))

    print(form.data)
    return render_template(
    'petadd.html',
    title = "Add a new pet",
    form = form,
    year=datetime.now().year
    )
@app.route('/pet/delete', methods=['GET','POST'])
def delete_Pet():
    pet = Pet.objects.all()
    form = Paw_Tracker.forms.PetFormDelete()

    if form.validate_on_submit():
        pet_First_Name = form.pet_First_Name.data
        pet_Last_Name = form.pet_Last_Name.data
        print(pet_First_Name)
        Pet.objects.get(pet_First_Name = pet_First_Name, pet_Last_Name = pet_Last_Name).delete()
        flash("Pet has been deleted from the database.", "success")
        return redirect(url_for('pet'))

    return render_template(
    'petdelete.html',
    title = "Delete a pet",
    pet = pet,
    form = form,
    year=datetime.now().year)
@app.route('/pet/select', methods=['GET','POST'])
def select_Pet():
    pet = Pet.objects.all()
    form = Paw_Tracker.forms.PetFormSelect()
    data = form.pet_First_Name.data

    if form.validate_on_submit():
        pet_First_Name = Pet.objects.get(pet_First_Name = data)
        pet_Data = pet_First_Name.pet_First_Name
        print(pet_Data)
        return redirect(url_for('edit_Pet', pet_First_Name=pet_Data))

    return render_template(
    'petselect.html',
    title = "Select a pet",
    pet = pet,
    form = form,
    year=datetime.now().year
    )
@app.route('/pet/edit/<pet_First_Name>',  methods=['GET','POST'])
def edit_Pet(pet_First_Name):
    pet = Pet.objects.get(pet_First_Name = pet_First_Name)
    form = Paw_Tracker.forms.PetFormEdit( obj=pet)


    if request.method == 'POST' and form.validate_on_submit():
        
        record = Pet.objects.get(pet_First_Name = pet_First_Name)
        record.pet_First_Name = form.pet_First_Name.data
        record.pet_Last_Name = form.pet_Last_Name.data
        record.pet_Breed = form.pet_Breed.data
        record.pet_Gender = form.pet_Gender.data
        record.pet_Age = form.pet_Age.data
        record.pet_Picture = form.pet_Picture.data
        record.save()
        flash("Record has been updated.","success")
        return redirect(url_for('pet'))

    return render_template(
    'petedit.html',
    title = "Edit a pet",
    form = form,
    year=datetime.now().year)

@app.route('/notes', methods=['GET','POST'])
def notes():
    notes = Notes.objects.all()
    form = Paw_Tracker.forms.NoteForm()
    return render_template(
        'notes.html',
        notes = notes,
        form = form,
        login=True,
        title='Add Notes on a Pet',
        year=datetime.now().year
        )
@app.route('/notes/add', methods=['GET','POST'])
def add_Note():
    form = Paw_Tracker.forms.NoteForm()
    if form.validate_on_submit():
        pet_First_Name = form.pet_First_Name.data
        note_Date = form.note_Date.data
        note_Notes = form.note_Notes.data

        note = Notes(pet_First_Name=pet_First_Name, note_Date=str(note_Date), note_Notes=note_Notes)
        note.save()
        flash("Note has been added to the database.", "success")
        return redirect(url_for('notes'))

    print(form.data)
    return render_template(
    'notesadd.html',
    title = "Add a new note on a pet",
    form = form,
    year=datetime.now().year
    )
@app.route('/notes/delete', methods=['GET','POST'])
def delete_Note():
    notes = Notes.objects.all()
    form = Paw_Tracker.forms.NoteFormDelete()

    if form.validate_on_submit():
        pet_First_Name = form.pet_First_Name.data
        note_Date = form.note_Date.data
        print(pet_First_Name)
        Notes.objects.get(pet_First_Name = pet_First_Name, note_Date = str(note_Date)).delete()
        flash("Note has been deleted from the database.", "success")
        return redirect(url_for('notes'))

    return render_template(
    'notesdelete.html',
    title = "Delete a note",
    notes = notes,
    form = form,
    year=datetime.now().year)
@app.route('/notes/select', methods=['GET','POST'])
def select_Note():
    notes = Notes.objects.all()
    form = Paw_Tracker.forms.NoteFormSelect()
    data = form.pet_First_Name.data
    note_Date = form.note_Date.data
    print(data)
    if form.validate_on_submit():
        pet_First_Name = Notes.objects.get(pet_First_Name = data)#, note_Date=str(form.note_Date.data))
        print(pet_First_Name)
        session['pet_info'] = pet_First_Name
        return redirect(url_for('edit_Note', pet_First_Name=pet_First_Name.pet_First_Name))

    return render_template(
    'notesselect.html',
    title = "Select a note",
    notes = notes,
    form = form,
    year=datetime.now().year
    )
@app.route('/notes/edit/<pet_First_Name>',  methods=['GET','POST'])
def edit_Note(pet_First_Name):
    data = session.get('pet_info')
    notes = Notes.objects.get(pet_First_Name = data['pet_First_Name'])
    form = Paw_Tracker.forms.NoteFormEdit( obj= notes)


    if request.method == 'POST' and form.validate_on_submit():
        record = Notes.objects.get(pet_First_Name = pet_First_Name)
        print(data)
        print(record['pet_ID'] )
        record['pet_First_Name'] = form.pet_First_Name.data
        record['note_Notes'] = form.note_Notes.data
        print(record)
        record.save()
        flash("Record has been updated.","success")
        return redirect(url_for('notes'))

    return render_template(
    'notesedit.html',
    title = "Edit a note",
    form = form,
    year=datetime.now().year)

@app.route('/profile')
def profile():
    return redirect(url_for('home'))

@app.route('/events')
def events():
    return redirect(url_for('home'))