from django.shortcuts import render , redirect
import razorpay
from django.conf import settings
from .form import *
from .models import *
import csv
from django.http import HttpResponse

def home(request):
    return render(request, 'Home.html')
# Create your views here.

def about(request):
    return render (request, 'About.html')

def work(request):
    return render (request , 'work.html')

def project(request):
    return render(request , 'Projects.html')

def media(request):
    return render(request , 'media.html')

def get(request):
    return render(request , 'get.html')

def blog(request):
    return render (request , 'blog.html')

def schooldrive(request):
    return render(request , 'schooldrive.html')

def womenhealth(request):
    return render(request , 'womenhealth.html')

def volunteer_signup(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'volin.html', {'form': form})

def volunteer_list(request):
    volunteers = VolunteerApplication.objects.all().order_by('-submitted_at')
    return render(request, 'volcard.html', {'volunteers': volunteers})



#paymanet

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.amount = donation.amount * 100  # Convert to paisa
            data = {
                "amount": donation.amount,
                "currency": "INR",
                "payment_capture": 1,
            }
            order = client.order.create(data=data)
            donation.save()

            context = {
                'donation': donation,
                'order_id': order['id'],
                'razorpay_key': settings.RAZORPAY_KEY_ID,
            }
            return render(request, 'payment_checkout.html', context)
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def download_report(request):
    # Create a response with the correct CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="women_health_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Women Reached', 'Health Camps Conducted', 'Districts Covered', 'Medical Volunteers'])  # Add relevant headers

    # Example data (replace with real data from your database)
    data = [
        ['8,500+', '35', '12', '60+'],  # Replace with actual values
    ]

    # Write data rows
    for row in data:
        writer.writerow(row)

    return response


def download_skill_report(request):
    # Create a response with the correct CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="women_skill_development_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Women Beneficiaries', 'States Covered', 'Program Timeline'])  # Headers

    # Example data (Replace with real data from your database)
    data = [
        ['1,200+', 'Rajasthan & MP', '2023 – Ongoing'],  # Example data
    ]

    # Write data rows
    for row in data:
        writer.writerow(row)

    return response

import csv
from django.http import HttpResponse

def download_health_report(request):
    # Create a response with the correct CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="community_health_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Individuals Reached', 'States Covered', 'Program Timeline'])  # Headers

    # Example data (Replace with actual data from your database)
    data = [
        ['10,000+', 'UP, Odisha, Assam', 'Ongoing'],  # Example data
    ]

    # Write data rows
    for row in data:
        writer.writerow(row)

    return response

def empowerwomen(request):
    return render (request, 'empowerwomen.html')

def edumilestone(request):
    return render (request, 'edumilestone.html')

def healthcare(request):
    return render (request, 'healthcare.html')

def schoolinbox(request):
    return render (request, 'schoolinbox.html')