from django.shortcuts import render

def doctor(request):
    return render(request,'doctors/doctor.html')
