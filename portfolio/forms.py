from django import forms
from .models import (CustomUser,Personal_Information,Education,
                     Technical_Skils,Internship,Key_Projects,Certifications,
                     Extracurricular_Activities,Contact)


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'profile_image']

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = Personal_Information
        fields = [
            'full_name', 'designation', 'tagline', 'about', 'phone', 'email',
            'address', 'city', 'state', 'country', 'github', 'linkedin',
            'portfolio_url', 'resume', 'profile_photo'
        ]

class EducationForm(forms.ModelForm):
    
    class Meta:
        model = Education
        fields = [
            'level','stream_or_course','institution','location', 
            'score_type','score_value','start_year','end_year','edu_image'
        ]
    

class Technical_SkilsForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Web Frameworks', 'Web Frameworks'),
        ('Libraries','Libraries'),
        ('Frontend', 'Frontend'),
        ('Languages', 'Languages'),
        ('Database', 'Database'),
        ('Tools', 'Tools'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    proficiency = forms.IntegerField(
        min_value=0,
        max_value=100,
        help_text='Skill proficiency percentage (0-100)'
    )
    
    class Meta:
        model = Technical_Skils
        fields = [
             'category' ,'skill_name', 'proficiency'
        ]
    

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = [
              'company', 'role',
              'start_year' ,'end_year', 'internship_image'
        ]

class KeyProjectsForm(forms.ModelForm):
    class Meta:
        model = Key_Projects
        fields = [
            'title',
            'description',
            'technologies',
            'domain',
            'internship',
            'project_image',
            'project_link'
        ]


class CertificationsForm(forms.ModelForm):
    class Meta:
        model = Certifications
        fields = [
            'organization','title','location','year'
        ]

class Extracurricular_ActivitiesForm(forms.ModelForm):
 class Meta:
     model = Extracurricular_Activities
     fields = [ 
          'role', 'organization','event_name','description','year'
     ]
   
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name','email','message'
        ]
     
       
