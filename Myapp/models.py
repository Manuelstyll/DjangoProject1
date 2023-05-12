from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.IntegerField()
    phone_number=models.IntegerField(null=True)

class Meta:
    db_table= "Student"

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class assignment(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Office=models.CharField(max_length=50)
    Age=models.IntegerField()
    Start_date=models.DateField()
    Salary=models.IntegerField()

    def __str__(self):
        return self.Name + ' ' + self.Position

class newitem(models.Model):
    Venue_Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Zip_PostCode=models.IntegerField()
    Contact_Phone=models.IntegerField()
    Web_Address=models.CharField(max_length=50)
    Email_Address=models.CharField(max_length=50)
    def __str__(self):
        return self.Venue_Name +' , '+ self.Address


class olditem(models.Model):
    Author=models.CharField(max_length=50)
    Title=models.CharField(max_length=50)
    Text=models.CharField(max_length=1000)
    Created=models.DateTimeField()
    Published_date=models.DateTimeField()

    def __str__(self):
        return self.Author +','+ self.Title