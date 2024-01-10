from django.shortcuts import render
from .models import User
from .form import UserSignUpForm


# Create your views here.

def index(request):
    user_count = User.objects.count()

    users = User.objects.all()

    for user in users:
        print(user.name)

    context = {
        "user_count": user_count,
        "users": users
    }
    return render(request, 'users/index.html', context)

# GET & POST
def signup(request):
    form = UserSignUpForm()
    errors = []
    message = None

    # When the data is present to be saved
    # That is the case when the request method is of type POST
    if request.method == "POST" :
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            message = "New user created"
        else :
            errors = form.errors

    context = {
        'form': form,
        'errors': errors,
        'message': message
    }
    return render(request, 'users/signup.html', context)
