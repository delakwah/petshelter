from django.db import models

# Create your models here.

class Pets(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    breed = models.CharField(max_length=255)
    age = models.IntegerField()
    health = models.TextField(null=True)
    pet_image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'Pets'

    def __str__(self):
        return self.name
    
class Adopt(models.Model):
    MALE = "M"
    FEMALE = "F"

    GenderChoice = {
        (MALE, 'Male'),
        (FEMALE, 'Female')
    }
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE, default=1)
    fname = models.CharField('First Name', max_length=255)
    lname = models.CharField('Last Name', max_length=255)
    age = models.CharField('Age', max_length=11)
    gender = models.CharField(max_length=1, choices=GenderChoice)
    phonenum = models.CharField('Contact', max_length=11)
    email = models.EmailField('Email Address', max_length=254)
    address = models.CharField(max_length=300)
    occup = models.CharField('Occupation', max_length=255)

    def __str__(self):
        return f"Adoption request for {self.pet.name} by {self.lname}"
    
class Volunteer(models.Model):
    MALE = "M"
    FEMALE = "F"

    GenderChoice = {
        (MALE, 'Male'),
        (FEMALE, 'Female')
    }
    firstname = models.CharField('First Name', max_length=255)
    lastname = models.CharField('Last Name', max_length=255)
    age = models.CharField('Age', max_length=11)
    gender = models.CharField(max_length=1, choices=GenderChoice)
    phonenum = models.CharField('Contact', max_length=11)
    email = models.EmailField('Email Address', max_length=254)

    def __str__(self):
        return f"Volunteer Request: {self.lastname}, {self.firstname}"


