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
