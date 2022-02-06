from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from .models import Contact, About, Skills, Testimonials, Services, Education, Experience, Portfolio, Gallery
from system.models import ConfigChoice


# Create your views here.
def Test(request):
    about = About.objects.all().first()
    skills = Skills.objects.all()
    testimonials = Testimonials.objects.all()
    services = Services.objects.all()
    education = Education.objects.all()
    interest = ConfigChoice.objects.filter(category__type="Interest")
    experiences = Experience.objects.all()
    portfolio = Portfolio.objects.all()

    context={
        "about":about,
        "interest":interest,
        "skills":skills,
        "services":services,
        "testimonials":testimonials,
        "experiences":experiences,
        "projects":portfolio,
        "educations":education
    }
    return render(request, "home.html",context=context)


def ContactUS(request):
    if request.method == 'POST':
        first_name = request.POST.get('cf_name', "")
        last_name = request.POST.get('cf_lname', "")
        sender = request.POST.get('cf_email', "")
        subject = request.POST.get('cf_subject', "")
        phone = request.POST.get('cf_phone', "")
        description = request.POST.get('cf_description', "")
        Contact.objects.create(first_name=first_name, last_name=last_name,email=sender,subject=subject,message=description)

        messages.info(request, 'Successfully Submitted data')
        html_content = render_to_string("contact_us_mail_template.html",
                                        {'first_name': first_name,'last_name':last_name,
                                         "subject":subject,"description":description,
                                         "phone":phone,
                                         })
        test_contend = strip_tags(html_content)
        email="bhuoneghimire@gmail.com"
        email = EmailMultiAlternatives('Contact Us Mail', test_contend,  sender, [email])
        email.attach_alternative(html_content, 'text/html')
        try:
            email.send()
        except Exception as e:
            pass
        return redirect("home")

    else:
        about = About.objects.all().first()
        skills = Skills.objects.all()
        interest = ConfigChoice.objects.filter(category__type="Interest")
        context = {
            "about": about,
            "interest": interest,
            "skills": skills
        }
        return render(request, "home.html", context=context)

def Detail(request,id):
    project = Portfolio.objects.get(id=id)
    gallery = Gallery.objects.filter(project=id)
    context = {
        "project":project,
        "gallery":gallery
    }
    return render(request, "portfolio-details.html", context=context)