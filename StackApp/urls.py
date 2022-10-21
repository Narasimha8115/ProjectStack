from django.contrib import admin
from django.urls import path
from StackApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"), 
    path('join',views.join,name="join"),
    path('login',views.login_user,name="login_user"),
    path('home-page',views.home_page,name="home_page"),
    path("project-page/",views.projectpage,name="project-page"),
    path("logout",views.logout_views,name="logout"),
    path("add-project",views.add_project,name="add-project"),
    path("create-project",views.create_project,name="create-project"),
    
    path("individual/<str:pk>",views.individual,name="individual",),

    path("profile/<str:pk>",views.profile,name="profile"),
    
    path("profile-edit/<str:pk>",views.profile_edit,name="profile-edit"),

    path("profile_updated",views.update_prof,name="update-profile")

]

urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)