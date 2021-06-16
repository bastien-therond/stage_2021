from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('depot-annonce/', views.postAnnonce, name = "depot-annonce"),
	path('modif-compt/', views.modifCompt, name="modif-compt"),

    path('', views.home, name="home"),
    path('profile', views.profile, name="profile"),
	path('autre/', views.autre, name = "autre"),
	path('modelisme/', views.modelisme, name = "modelisme"),
	path('oenologie/', views.oenologie, name = "oenologie"),
	path('philatelie/', views.philatelie, name = "philatelie"),
	path('login/edit/', views.post_edit, name='post_edit')
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)