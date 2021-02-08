from django.shortcuts import render,redirect
# from django.contrib.auth import login, authenticate
# from .forms import SignUpForm
# from django.contrib.auth.decorators import login_required
# from rest_framework_simplejwt.views import TokenObtainPairView # new

# from .serializers import LogInSerializer, UserSerializer
# from django.contrib.auth import get_user_model
# from rest_framework  import generics

# Create your views here.
# class SignUpView(generics.CreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
# class LogInView(TokenObtainPairView): # new
#     serializer_class = LogInSerializer
# @login_required(login_url='/accounts/login/')
def index (request) :


    return render(request, 'index.html',{})

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})



def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })  