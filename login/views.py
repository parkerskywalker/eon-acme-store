from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout as do_logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

class Login(LoginView):
    template_name = "templates/login/login.html"

    def post(self, request, *args, **kwargs):

        try:
            data_user = User.objects.get(email=self.request.POST["email"])
            password = self.request.POST["password"]
            user = authenticate(request, username=data_user.username, password=password)

            if user is not None:
                login(request, user)
                if user.is_superuser or user.is_staff:
                    return redirect("webmin:product_list")                
                return redirect('webstore:index')
            
            

        except Exception as e:
            pass
    
        return redirect("login:login")


def logout(request, *args, **kwargs):
    do_logout(request)

    return redirect("/")