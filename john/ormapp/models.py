from django.db import models
from django.contrib import admin 
class Bankloan (models.Model):
    loanid=models.CharField(max_length=20,help_text="Employee ID")
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField() 
    email=models.EmailField()

class BankloanAdmin(admin.ModelAdmin):
    list_display=('loanid', 'name', 'salary', "age" , 'email')
