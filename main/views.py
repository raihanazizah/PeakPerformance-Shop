from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Peak Performance Shop',
        'student_name': 'Raihana Nur Azizah',
        'student_id': '2406413426',
        'student_class': 'PBP D',
    }
    return render(request, 'home.html', context)
