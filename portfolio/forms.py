from django import forms
import requests
from .models import (CustomUser,Personal_Information,Education,
                     Technical_Skils,Internship,Key_Projects,Certifications,
                     Extracurricular_Activities,Contact)
from django.core.exceptions import ValidationError
import os
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE_PATH = os.path.join(BASE_DIR, '.env')

# 2. Force load_dotenv to look directly at that specific path
load_dotenv(dotenv_path=ENV_FILE_PATH)

load_dotenv()

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
        fields = ['name', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # 1. Load API Key
        API_KEY = os.getenv('ZEROBOUNCE_API_KEY')
        
        # SECURITY CHECK: Print to terminal to ensure the key actually loaded
        if not API_KEY:
            print("🛑 ERROR: ZEROBOUNCE_API_KEY is missing or .env is not loading!")
            
        url = f"https://api.zerobounce.net/v2/validate?api_key={API_KEY}&email={email}"
        
        try:
            # 2. Call the validation API
            response = requests.get(url, timeout=5)
            data = response.json()
            
            # DEBUGGING: Print the exact response from ZeroBounce to your terminal
            print("🟢 ZeroBounce Response:", data)
            
            # 3. Check if ZeroBounce threw an error (like Invalid Key or Out of Credits)
            if "error" in data:
                print("🛑 ZEROBOUNCE API ERROR:", data["error"])
                return email
            
            status = data.get('status')
            sub_status = data.get('sub_status')
            
            # 4. Reject if the inbox physically does not exist
            if status == 'invalid':
                raise ValidationError("This email address does not exist. Please check for typos.")
                
            # 5. Block common fake behaviors (like random strings)
            if sub_status in ['mailbox_not_found', 'global_suppression', 'disposable']:
                raise ValidationError("Please provide a valid, active email address.")
                
        except requests.RequestException as e:
            print("🛑 REQUEST EXCEPTION:", e)
            pass
        return email
       