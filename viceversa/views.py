from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def reversed(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request, 'reversed.html', {'reversed_text':reversed_text})
