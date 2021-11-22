from django.urls import path
from . import views

urlpatterns = [
    # home url
    path('', views.Home.as_view(), name ="home"),

    # start of create poem urls
    path('create', views.CreateIndex.as_view(), name ="create_index"),
    path('create/beach', views.CreateBeach.as_view(), name ="create_beach"),
    path('create/animals', views.CreateAnimals.as_view(), name ="create_animals"),
    path('create/touch', views.CreateTouch.as_view(), name ="create_touch"),
    path('create/freewrite', views.CreateFreeWrite.as_view(), name ="create_free_write"),
    # end of create poem urls

    # start of profile urls
    path('profile/<int:pk>', views.ProfileDetail.as_view(), name="profile_detail"),
    path('profile/<int:pk>/update', views.ProfileDetail.as_view(), name="profile_update"),
    # end of profile urls

    # start of poem urls
    path('poems/<int:pk>/new-poem', views.PoemCreate.as_view(), name ="poem_create"),
    path('confirm', views.Confirm.as_view(), name ="confirm-continue"),
    path('poems', views.PoemsIndex.as_view(), name ="poems_index"),
    path('poems/<int:pk>', views.PoemDetail.as_view(), name ="poem_detail"),
    # end of poem urls
]

