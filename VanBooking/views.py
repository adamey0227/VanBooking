from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Student, Driver, Booking

def index(request):
    return render(request, 'index.html')

def register_student(request):
    if request.method == 'POST':
        student = Student(
            studentName=request.POST['studentName'],
            studentID=request.POST['studentID'],
            studentPhone=request.POST['studentPhone'],
            studentEmail=request.POST['studentEmail'],
            studentPassword=request.POST['studentPassword']
        )
        student.save()
        return redirect('/my_page/login/student/')
    return render(request, 'register_student.html')

def register_driver(request):
    if request.method == 'POST':
        driver = Driver(
            driverName=request.POST['driverName'],
            driverID=request.POST['driverID'],
            driverPhone=request.POST['driverPhone'],
            driverEmail=request.POST['driverEmail'],
            driverPassword=request.POST['driverPassword']
        )
        driver.save()
        return redirect('/my_page/login/driver/')
    return render(request, 'register_driver.html')

def login_student(request):
    if request.method == 'POST':
        email = request.POST['studentEmail']
        password = request.POST['studentPassword']
        try:
            student = Student.objects.get(studentEmail=email, studentPassword=password)
            request.session['student_email'] = email  
            return redirect('/my_page/dashboard/student/')
        except Student.DoesNotExist:
            error_message = 'Invalid email or password!'
            return render(request, 'login_student.html', {'error_message': error_message})
    return render(request, 'login_student.html')

def login_driver(request):
    if request.method == 'POST':
        email = request.POST['driverEmail']
        password = request.POST['driverPassword']
        try:
            driver = Driver.objects.get(driverEmail=email, driverPassword=password)
            request.session['driver_email'] = email  
            return redirect('/my_page/dashboard/driver/')
        except Driver.DoesNotExist:
            error_message = 'Invalid email or password!'
            return render(request, 'login_driver.html', {'error_message': error_message})
    return render(request, 'login_driver.html')

def dashboard_student(request):
    email = request.session.get('student_email')
    student = Student.objects.get(studentEmail=email)

    bookings = Booking.objects.filter(studentID=student)

    if request.method == 'POST':
        return redirect('/my_page/booking/')  

    return render(request, 'dashboard_student.html', {'student': student, 'bookings': bookings})

def dashboard_driver(request):
    email = request.session.get('driver_email')
    driver = Driver.objects.get(driverEmail=email)

    bookings = Booking.objects.filter(driverID=driver)

    return render(request, 'dashboard_driver.html', {'driver': driver, 'bookings': bookings})

def update_student(request):
    email = request.session['student_email']
    student = Student.objects.get(studentEmail=email)

    if request.method == 'POST':
        student.studentName = request.POST['studentName']
        student.studentPhone = request.POST['studentPhone']
        student.studentEmail = request.POST['studentEmail']
        student.save()
        return redirect('/my_page/dashboard/student/')
    
    return render(request, 'update_student.html', {'student': student})

def update_driver(request):
    email = request.session['driver_email']
    driver = Driver.objects.get(driverEmail=email)

    if request.method == 'POST':
        driver.driverName = request.POST['driverName']
        driver.driverPhone = request.POST['driverPhone']
        driver.driverEmail = request.POST['driverEmail']
        driver.save()
        return redirect('/my_page/dashboard/driver/')
    
    return render(request, 'update_driver.html', {'driver': driver})

def delete_student(request):
    email = request.session['student_email']
    student = Student.objects.get(studentEmail=email)
    student.delete()
    del request.session['student_email']  
    return redirect('/my_page')

def delete_driver(request):
    email = request.session['driver_email']
    driver = Driver.objects.get(driverEmail=email)
    driver.delete()
    del request.session['driver_email']  
    return redirect('/my_page')


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['bookingDate', 'bookingTime']

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            email = request.session.get('student_email')
            student = Student.objects.get(studentEmail=email)
            booking.studentID = student
            booking.driverID = Driver.objects.order_by('?').first()  
            booking.save()
            return redirect('/my_page/dashboard/student/')
    else:
        form = BookingForm()

    email = request.session.get('student_email')
    student = Student.objects.get(studentEmail=email)
    return render(request, 'booking.html', {'form': form, 'student': student})

def delete_booking(request, booking_no):
    try:
        booking = Booking.objects.get(bookingNo=booking_no)
        booking.delete()
    except Booking.DoesNotExist:
        pass  

    return redirect('/my_page/dashboard/student')