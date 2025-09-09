from django.shortcuts import render

def home(request):
    context = {
        'app_name': 'Peak Performance Shop',
        'student_name': 'Raihana Nur Azizah',
        'student_class': 'PBP D',
    }
    return render(request, 'home.html', context)
