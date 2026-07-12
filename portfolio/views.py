from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import (
    PersonalInformationForm,
    EducationForm,
    Technical_SkilsForm,
    InternshipForm,
    KeyProjectsForm,
    CertificationsForm,
    Extracurricular_ActivitiesForm,
    ContactForm
)
from .models import (
    Personal_Information,
    Education,
    Technical_Skils,
    Internship,
    Key_Projects,
    Certifications,
    Extracurricular_Activities,
    Contact
)


def is_admin_user(user):
    return user.is_authenticated and user.is_staff


def home_page(request):
    context = {
        'personal_info': Personal_Information.objects.first(),
        'educations': Education.objects.order_by('-end_year'),
        'skills': Technical_Skils.objects.all(),
        'internships': Internship.objects.prefetch_related('projects').all(),
        'projects': Key_Projects.objects.all(),
        'certifications': Certifications.objects.order_by('-year'),
        'contact' : Contact.objects.all().order_by("-created_at")
    }
    return render(request, 'home.html', context)


def success_page(request):
    return render(request, 'success_page.html')


def logout_view(request):
    logout(request)
    return redirect('home_page')


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def dashboard(request):
    context = {
        'personal_info': Personal_Information.objects.first(),
        'educations': Education.objects.order_by('-end_year'),
        'skills': Technical_Skils.objects.all(),
        'internships': Internship.objects.prefetch_related('projects').all(),
        'projects': Key_Projects.objects.all(),
        'certifications': Certifications.objects.order_by('-year'),
        'contact' : Contact.objects.all().order_by("-created_at")

    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def personal_information(request):
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PersonalInformationForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'Personal Information', 'submit_label': 'Save Personal Information'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def edit_personal_information(request, pk):
    personal_info = get_object_or_404(Personal_Information, pk=pk)
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST, request.FILES, instance=personal_info)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PersonalInformationForm(instance=personal_info)
    return render(request, 'form_page.html', {'form': form, 'title': 'Edit Personal Information', 'submit_label': 'Update Personal Information'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def delete_personal_information(request, pk):
    personal_info = get_object_or_404(Personal_Information, pk=pk)
    if request.method == 'POST':
        personal_info.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'object': personal_info, 'title': 'Delete Personal Information'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EducationForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'Add Education', 'submit_label': 'Add Education'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def edit_education(request, pk):
    education_item = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES, instance=education_item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EducationForm(instance=education_item)
    return render(request, 'form_page.html', {'form': form, 'title': 'Edit Education', 'submit_label': 'Update Education'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def delete_education(request, pk):
    education_item = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        education_item.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'object': education_item, 'title': 'Delete Education'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def technical_skills(request):
    if request.method == 'POST':
        form = Technical_SkilsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = Technical_SkilsForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'Add Skill', 'submit_label': 'Add Skill'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def edit_skill(request, pk):
    skill = get_object_or_404(Technical_Skils, pk=pk)
    if request.method == 'POST':
        form = Technical_SkilsForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = Technical_SkilsForm(instance=skill)
    return render(request, 'form_page.html', {'form': form, 'title': 'Edit Skill', 'submit_label': 'Update Skill'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def delete_skill(request, pk):
    skill = get_object_or_404(Technical_Skils, pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'object': skill, 'title': 'Delete Skill'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def add_internship(request):
    if request.method == 'POST':
        form = InternshipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = InternshipForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'Add Internship', 'submit_label': 'Add Internship'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def edit_internship(request, pk):
    internship = get_object_or_404(Internship, pk=pk)
    if request.method == 'POST':
        form = InternshipForm(request.POST, request.FILES, instance=internship)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = InternshipForm(instance=internship)
    return render(request, 'form_page.html', {'form': form, 'title': 'Edit Internship', 'submit_label': 'Update Internship'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def delete_internship(request, pk):
    internship = get_object_or_404(Internship, pk=pk)
    if request.method == 'POST':
        internship.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'object': internship, 'title': 'Delete Internship'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def add_project(request):
    if request.method == 'POST':
        form = KeyProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = KeyProjectsForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'Add Project', 'submit_label': 'Add Project'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def edit_project(request, pk):
    project = get_object_or_404(Key_Projects, pk=pk)
    if request.method == 'POST':
        form = KeyProjectsForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = KeyProjectsForm(instance=project)
    return render(request, 'form_page.html', {'form': form, 'title': 'Edit Project', 'submit_label': 'Update Project'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def delete_project(request, pk):
    project = get_object_or_404(Key_Projects, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'object': project, 'title': 'Delete Project'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def add_certification(request):
    if request.method == 'POST':
        form = CertificationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CertificationsForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'Add Certification', 'submit_label': 'Add Certification'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def edit_certification(request, pk):
    certification = get_object_or_404(Certifications, pk=pk)
    if request.method == 'POST':
        form = CertificationsForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CertificationsForm(instance=certification)
    return render(request, 'form_page.html', {'form': form, 'title': 'Edit Certification', 'submit_label': 'Update Certification'})


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def delete_certification(request, pk):
    certification = get_object_or_404(Certifications, pk=pk)
    if request.method == 'POST':
        certification.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'object': certification, 'title': 'Delete Certification'})


def contact(request):
    print("Method:", request.method)

    if request.method == "POST":
        print(request.POST)

        form = ContactForm(request.POST)

        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect("home_page")
        else:
            print("Form errors:", form.errors)

    else:
        form = ContactForm()

    return render(request, "shared_portfolio_content.html", {
        "form": form,
    })
        




@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='login')
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        contact.delete()
        return redirect('dashboard')

    return render(request, "confirm_delete.html", {'object': contact, 'title': 'Delete Contact'})