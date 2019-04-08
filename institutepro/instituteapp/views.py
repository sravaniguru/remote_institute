from django.shortcuts import render
from .models import  ContactData,FeedbackData
from  .forms import ContactForm,FeedbackForm
def home(request):
    return render(request,'home.html')
def contact(request):
    if request.method=="POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name=cform.cleaned_data.get('name','')
            email=cform.cleaned_data.get('email','')
            mobile=cform.cleaned_data.get('mobile','')
            courses=cform.cleaned_data.get('courses','')
            locations=cform.cleaned_data.get('locaions','')
            shifts=cform.cleaned_data.get('shifts','')
            data=ContactData(
                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                locations=locations,
                shifts=shifts
            )
            data.save()
            cform=ContactForm()
            return render(request,'institute_contact.html',{'cform':cform})
    else:
      cform = ContactForm()
      return render(request, 'institute_contact.html', {'cform': cform})
def services(request):
    return render(request,'service.html')
import datetime as dt
date1=dt.datetime.now()
def feedback(request):
    if request.method=="POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name','')
            rating=request.POST.get('rating','')
            feedback=request.POST.get('feedback','')
            data=FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1

            )
            data.save()
            fform=FeedbackForm()
            feedbacks=FeedbackData.objects.all()
            return render(request,'feedback.html',{'ffrom':fform,'feedbacks':feedbacks})
    else:
        fform=FeedbackForm()
        feedbacks=FeedbackData.objects.all()
        return render(request, 'feedback.html', {'fform':fform, 'feedbacks':feedbacks})
def gallery(request):
    return render(request,'gallery.html')




