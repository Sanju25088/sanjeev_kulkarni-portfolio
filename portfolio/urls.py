from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('personal-information/', views.personal_information, name='personal_information'),
    path('personal-information/<int:pk>/edit/', views.edit_personal_information, name='edit_personal_information'),
    path('personal-information/<int:pk>/delete/', views.delete_personal_information, name='delete_personal_information'),
    path('education/', views.education, name='education'),
    path('education/<int:pk>/edit/', views.edit_education, name='edit_education'),
    path('education/<int:pk>/delete/', views.delete_education, name='delete_education'),
    path('technical-skills/', views.technical_skills, name='technical_skills'),
    path('technical-skills/<int:pk>/edit/', views.edit_skill, name='edit_skill'),
    path('technical-skills/<int:pk>/delete/', views.delete_skill, name='delete_skill'),
    path('internships/add/', views.add_internship, name='add_internship'),
    path('internships/<int:pk>/edit/', views.edit_internship, name='edit_internship'),
    path('internships/<int:pk>/delete/', views.delete_internship, name='delete_internship'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('certifications/add/', views.add_certification, name='add_certification'),
    path('certifications/<int:pk>/edit/', views.edit_certification, name='edit_certification'),
    path('certifications/<int:pk>/delete/', views.delete_certification, name='delete_certification'),
    path('contact/', views.contact, name='contact'),
    path('contact/delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('success/', views.success_page, name='success_page'),
]
