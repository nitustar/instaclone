from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # return render(request, 'users/index.html')
    # return HttpResponse('Hello, world. You are at the users index view for views.py.')

    check_text = request.GET['text']

    message = "I don't know anything about your favorite colour"

    if check_text == 'blue':
        message = 'You like blue!'
    elif check_text == 'red':
        message = 'You like red!'
    elif check_text == 'green':
        message = 'You like green!'
    elif check_text == 'yellow':
        message = 'You like yellow!'

    # message = f'{request.method}'
    return HttpResponse(message)
