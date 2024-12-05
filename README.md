# Ex02 Django ORM Web Application
# Date:01.12.2024
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
admin.py

from django.contrib import admin
from .models import Loan, LoanAdmin
admin.site.register(Loan, LoanAdmin)

models.py

from django.db import models
from django.contrib import admin
class Loan (models.Model):
   Acc_holder_id=models.CharField(max_length=20, primary_key=True)
   Acc_holder_name=models.CharField(max_length=100)
   Mobile_no=models.IntegerField( )
   Age=models.IntegerField( )
   Email=models.EmailField( )
   DoB=models.DateField( )
   Loan_amount=models.IntegerField( )
class LoanAdmin(admin.ModelAdmin):
    list_display=('Acc_holder_id', 'Acc_holder_name', 'Mobile_no', 'Age', 'Email','DoB', 'Loan_amount')





```
# OUTPUT
![alt text](<Screenshot 2024-12-01 151235.png>)

![Screenshot 2024-12-06 020215](https://github.com/user-attachments/assets/7831a736-6156-49c2-b0ae-b6f230e6b0ee)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
