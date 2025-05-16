from django.shortcuts import render, redirect
from .models import Skill, Project, ContactMessage
from django.contrib import messages

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('-date_completed')
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill)
    
    about = {
        'name': 'Irish Prajapati',
        'intro': "I'm a developer specializing in creating beautiful and functional websites and applications.",
        'about': "I'm a dedicated developer specializing in Python with Django. My journey in web development began with frontend technologies, but over time, I expanded my expertise to backend development. I'm passionate about building scalable, high-performance applications and constantly learning new technologies to stay ahead in the industry.\n\nI believe in writing clean, maintainable code and staying up-to-date with the latest industry trends and best practices.\n\nBeyond coding, I enjoy hiking, reading, and exploring new challenges.",
        'email': 'irishmjn@gmail.com',
        'location': 'Bhaktapur',
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent!')
            return redirect('portfolio:home')
        else:
            messages.error(request, 'Please fill in all fields.')

    context = {
        'about': about,
        'skill_categories': skill_categories,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)
