from django import forms
from multiselectfield import MultiSelectFormField
class ContactForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile'
            }
        )
    )
    mobile=forms.IntegerField(
        label="enter your mobile",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile'
            }
        )
    )
    COURSES_CHOICES=(
        ('python','python'),
        ('django','django'),
        ('ui','ui'),
        ('restapi','restapi'),
        ('flask','flask')
    )
    courses=MultiSelectFormField(max_length=100,choices=COURSES_CHOICES)
    LOCATION_CHOICES=(
        ('hyd','hyderabd'),
        ('bang','banglore'),
        ('che','chennai'),
    )
    locaions=MultiSelectFormField(max_length=100,choices=LOCATION_CHOICES)
    SHIFT_CHOICES=(
        ('mrng','morning'),
        ('aftrn','afternoon'),
        ('evng','evening')
    )
    shifts=MultiSelectFormField(max_length=100,choices=SHIFT_CHOICES)
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    rating=forms.IntegerField(
        label="enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your rating'
            }
        )
    )
    feedback=forms.CharField(
        label="enter your feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'your feedback'
            }
        )
    )