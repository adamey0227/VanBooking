from django.db import models

class Student(models.Model):
    studentName=models.TextField(max_length=128)
    studentID=models.CharField(max_length=11,primary_key=True)
    studentPhone=models.TextField(max_length=128)
    studentEmail=models.EmailField()
    studentPassword=models.CharField(max_length=128)

class Driver(models.Model):
    driverName=models.TextField(max_length=128)
    driverID=models.CharField(max_length=3,primary_key=True)
    driverPhone=models.TextField(max_length=128)
    driverEmail=models.EmailField()
    driverPassword=models.CharField(max_length=128)

class Booking(models.Model):
    bookingNo=models.AutoField(primary_key=True)
    studentID=models.ForeignKey(Student,on_delete=models.CASCADE)
    bookingDate=models.DateField(blank=True,null=True)
    bookingTime=models.TimeField(blank=True,null=True)
    driverID=models.ForeignKey(Driver,on_delete=models.CASCADE)
