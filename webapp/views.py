from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render 
from django.urls import reverse
from .models import Pets, Adopt, Volunteer
from .forms import AdoptionForm, PetForm, VolunteerForm, UpdateForm 


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')

def adopt(request):
    pet = {'adopt': Pets.objects.all()}
    return render(request, 'adopt.html', pet)

def steps(request):
    return render(request, 'steps.html')

def details(request, id):
    pets = get_object_or_404(Pets, pk=id)
    return render(request, 'details.html', {'pets': pets})

def adopt_form(request, pet_id):
    pet = get_object_or_404(Pets, pk=pet_id)
    if request.method == "POST":
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        initial_data = {'pet': pet}
        form = AdoptionForm(initial=initial_data)
    return render(request, 'adopt_form.html', {'form': form, 'pet': pet})

def adopt_request(request):
    adopt = {'adopt': Adopt.objects.all()}
    return render(request, 'adopt_request.html', adopt)

def thank_you(request):
    return render(request, 'thank_you.html')

def volunteer(request):
    form = VolunteerForm()
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("You have registered successfully! Thank you for volunteering!"))
            return redirect('home')
        else:
            messages.success(request, ("There was a problem registering please try again."))
            return redirect('volunteer')
    else:
        return render(request, 'volunteer.html', {'form':form})

def volunteer_list(request):
    volunteer = {'volunteer': Volunteer.objects.all()}
    return render(request, 'volunteer_list.html', volunteer)
    
def admin_panel(request):
    pet = {'adopt': Pets.objects.all()}
    return render(request, 'admin_panel.html', pet)

def add_adopt(request):
    submitted = False
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            messages.success(request, ("Pet added successfully!"))
            return HttpResponseRedirect(reverse('add_adopt') + '?submitted=True')

    else:
        form = PetForm()
        if 'submitted' in request.GET:
            submitted = True 

    return render(request, 'add_adopt.html', {'form': form, 'submitted': submitted})

def update_adopt(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    form = UpdateForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save()
        messages.success(request, ("Pet's info has been updated successfully"))
        return redirect('admin_panel')
    
    return render(request,'update_adopt.html', {'form': form, 'pet': pet})
    
def delete_adopt(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    pet.delete()
    messages.success(request, ("Pet has been deleted successfully"))
    return redirect('admin_panel')

    
