from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('student/<str:pk>', views.student, name = 'student'),
    path('single_class/<str:pk>', views.single_class, name='single_class'),
    path('single_student/<str:pk>', views.single_student, name='single_student'),
    path('add_score/<str:pk>', views.add_score, name='add_score'),
    path('report/<str:pk>', views.report, name='report'),
    path('registeration', views.registeration, name='registeration'),
    path('update_student/<str:pk>', views.update_student, name='update_student'),
    path('update_score/<str:pk>', views.update_score, name = 'update_score'),
    path('logout', views.Logout, name='logout'),
]