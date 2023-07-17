# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('register/student/', views.register_student, name='register_student'),
#     path('register/driver/', views.register_driver, name='register_driver'),
#     path('login/student/', views.login_student, name='login_student'),
#     path('login/driver/', views.login_driver, name='login_driver'),
#     path('dashboard/student/', views.dashboard_student, name='dashboard_student'),
#     path('dashboard/driver/', views.dashboard_driver, name='dashboard_driver'),
#     path('update/student/', views.update_student, name='update_student'),
#     path('update/driver/', views.update_driver, name='update_driver'),
#     path('delete/student/', views.delete_student, name='delete_student'),
#     path('delete/driver/', views.delete_driver, name='delete_driver'),
#     path('booking/', views.booking, name='booking'),
#     path('delete_booking/<int:booking_no>/', views.delete_booking, name='delete_booking'),

# ]

from django.urls import path
from . import views

app_name = 'VanBooking'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/driver/', views.register_driver, name='register_driver'),
    path('login/student/', views.login_student, name='login_student'),
    path('login/driver/', views.login_driver, name='login_driver'),
    path('dashboard/student/', views.dashboard_student, name='dashboard_student'),
    path('dashboard/driver/', views.dashboard_driver, name='dashboard_driver'),
    path('update/student/', views.update_student, name='update_student'),
    path('update/driver/', views.update_driver, name='update_driver'),
    path('delete/student/', views.delete_student, name='delete_student'),
    path('delete/driver/', views.delete_driver, name='delete_driver'),
    path('booking/', views.booking, name='booking'),
    path('dashboard/student/delete_booking/<int:booking_no>', views.delete_booking, name='delete_booking'),
]