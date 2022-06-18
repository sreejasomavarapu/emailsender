from email import message
from tkinter.tix import Form
from django.shortcuts import redirect, render
from . forms import ContactForm
from django.core.mail import send_mail
from .models import Plan
from . forms import PlanBookForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def contact(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            email_input = form.cleaned_data.get('sender')
            subject =form.cleaned_data.get('subject')
            message =form.cleaned_data.get('message')
            send_mail(subject,message,email_input,['sreejasomavarapu29@gmail.com'])
            #print()
            return redirect('contactnext')
         
    else:
        form = ContactForm()
    return render(request,'user/contactform.html',{'form':form})

def contactnext(request):
    return render(request,'user/contactnext.html')

def plans(request):
    plans_all = Plan.objects.all()
    return render(request,'user/plans.html',{'plans_all':plans_all})

@login_required(login_url='sign_in')
def planbook(request):
    if request.method=='POST':
        form =PlanBookForm(request.POST)
        if form.is_valid():
            planbooked = form.save(commit=False)
            planbooked.user = request.user
            planbooked.save()
            subject ='Plan Book Registration Successful'
            message='Thank you '+ str(planbooked.user.username) +' for booking ' + str(form.cleaned_data.get('plan'))
            email_send_to= request.user.email
            send_mail(subject,message,'sreejasomavarapu29@gmail.com',[email_send_to])
            return redirect('plans')
    else:
        form =PlanBookForm()
    context ={'form':form}
    return render(request,'user/planbook.html',context)
    