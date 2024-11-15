from django.shortcuts import render, redirect
from myapp.models import Appointment, Contact

# Create your views here.
def home(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def doctors(request):
    return render(request,'doctors.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def appointment(request):
    if request.method == "POST":
       myappointments=Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            datetime=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
       myappointments.save()
       return redirect('/appointment')

    else:
        return render(request,'appointment.html')



def show(request):
    allappointments=Appointment.objects.all()
    return render(request,'show.html',{'appointment':allappointments})

def delete(request,id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

def contact(request):
    if request.method == "POST":
        records=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        records.save()
        return redirect('/contact')
    else:
        return render(request,'contact.html')

def myrecords(request):
    allrecords=Contact.objects.all()
    return render(request,'myrecords.html',{'contact':allrecords})

def delete_contact(request,id):
    record = Contact.objects.get(id=id)
    record.delete()
    return redirect('/myrecords')