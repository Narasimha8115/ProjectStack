from email import message
import re
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import Projectss,Profile_Up
from django.urls import reverse_lazy
from django.conf.urls.static import static

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def home(request):
    return render(request,"home.html")

def home_page(request):
    return render(request,"home.html")


@login_required(login_url=reverse_lazy('login_user'))
def projectpage(request):
    projectss=Projectss.objects.all()
    current_user=request.user
    user_id=current_user.id
    
    return render(request,"projects.html",{"projectss":projectss,"user_id":user_id})


def join(request):
    if request.method=="POST":
        username = request.POST.get('name')
        email = request.POST.get('email') 
        password = request.POST.get('password')
        repeat_pass = request.POST.get('repeat-pass')

        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()

        subject = "Account created succesfully PROJECTSTACK"
        message = f'hello {user.username},\nThank you for creating an account on our ProjectStack site.We are glad you are going to exploring ProjectStack!\n Explore the projects now and share your great ideas,GOOD LUCK\n If you have forgotten your password (it happens to the best of us), use the Forgot password? link to reset it.\n Regards,\nProjectStack site'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject,message,email_from,recipient_list)

        return redirect("login_user") 
    return render(request,"join.html")

def login_user(request):
    context={}
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password') 

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("project-page")
        else:
            context["error_message"]="*Please enter the correct details"
            return render(request,"login.html",context)

    return render(request,"login.html")


@login_required(login_url=reverse_lazy('login_user'))
def logout_views(request):

    logout(request)
    return redirect("home")




@login_required(login_url=reverse_lazy('login_user'))
def add_project(request):
   
    return render(request,"share_project.html",)


@login_required(login_url=reverse_lazy('login_user'))
def create_project(request):
    context={}
    context_success={}
    if request.method=="POST":
        try:
            Projectss.objects.create(
                title=request.POST.get("title_of_pro"),
                category=request.POST.get("category_of_pro"),
                description=request.POST.get("decription_of_pro"),
                technologies=request.POST.get("techno_of_pro"),
                images_one=request.FILES.get('image_one'),
                images_two=request.FILES.get('image_two'),
                images_three=request.FILES.get('image_three'),
                videos=request.FILES.get('video_of_pro'),
                author=request.user
            )
            context_success["success"]="*Project published successfully"
            return redirect(request,"add-project",context_success)
        except:
            context["notsuccessfull"]="*Provide all required fields"
    return render(request,"share_project.html",context)


#individual post function
@login_required(login_url=reverse_lazy('login_user'))
def individual(request,pk):
    post=Projectss.objects.get(id=pk)
    return render(request,"individual_post.html",{"post":post})


@login_required(login_url=reverse_lazy('login_user'))
def profile(request,pk):
    profile_data=User.objects.get(id=pk)
    current_user=request.user
    user_id=current_user.id

    return render(request,"profilepage.html",{"profile_data":profile_data,"user_id":user_id})

def profile_edit(request,pk):
    profile_edit_data=User.objects.get(id=pk)
    return render(request,"profile_edit.html",{ "profile_edit_data": profile_edit_data})

def update_prof(request):
    if request.method=="POST":
        Profile_Up.objects.create(
            phone = request.POST.get('phone'),
            profession = request.POST.get('prof'),
            ins_or_org = request.POST.get('ins'),
            address = request.POST.get('add'),
            profile_img=request.FILES.get('prof_img')
        )
        return redirect(request,"profile")
    return render(request,"profile_edit.html")




