from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assign/', views.assign, name='assist'),
    path('enlist/', views.enlist, name='list'),
    path('cat/', views.cat, name='animal'),
    path('', views.form, name='forms'),
    path('members/', views.members, name='forms'),
    path('student/', views.student),
    path('employee/', views.employee),
    path('gsession/', views.getsession),
    path('ssession/', views.setsession),
    path('form/', views.forms),
    path('new/', views.newassign),


]
