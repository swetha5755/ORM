# Generated by Django 5.1.3 on 2024-12-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('Acc_holder_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Acc_holder_name', models.CharField(max_length=100)),
                ('Mobile_no', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('DoB', models.DateField()),
                ('Loan_amount', models.IntegerField()),
            ],
        ),
    ]
