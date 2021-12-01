from django.urls import path
from . import views

urlpatterns = [
    # home url
    path('', views.Home.as_view(), name ="home"),

    # start of account urls
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    # end of account urls

    # start of profile urls
    path('profile/<int:pk>', views.ProfileDetail.as_view(), name="profile_detail"),
    # path('profile/<int:pk>/update', views.ProfileDetail.as_view(), name="profile_update"),
    # end of profile urls

    # start of create poem urls
    path('create', views.CreateIndex.as_view(), name ="create_index"),
    path('create/beach', views.CreateBeach.as_view(), name ="create_beach"),
    path('create/animals', views.CreateAnimals.as_view(), name ="create_animals"),
    path('create/touch', views.CreateTouch.as_view(), name ="create_touch"),
    path('create/freewrite', views.CreateFreeWrite.as_view(), name ="create_free_write"),
    # end of create poem urls

    # start of poem urls
    # path('poems/new-poem', views.PoemCreate.as_view(), name ="poem_create"),
    path('confirm', views.Confirm.as_view(), name ="confirm"),
    path('profile/poems', views.PoemsIndex.as_view(), name ="poems_index"),

    # How do I pass this the object pk from the Poem model and have it related to the profile/account?
    path('poems/<int:pk>', views.PoemDetail.as_view(), name ="poem_detail"),
    path('posts/<int:pk>/update', views.PoemUpdate.as_view(), name="poem_update"),
    path('posts/<int:pk>/delete', views.PoemDelete.as_view(), name="poem_delete"),

    # end of poem urls
]

