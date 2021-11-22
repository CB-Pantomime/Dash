from django.shortcuts import redirect, render
# from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, DetailView, UpdateView

# IMPORT MODELS
from .models import Poem


# ALL VIEWS
class Home(TemplateView):

    template_name = "home.html"



# START CREATE VIEWS
class CreateIndex(TemplateView):

    template_name = "create_index.html"

class CreateBeach(TemplateView):

    template_name = "create_beach.html"

class CreateAnimals(TemplateView):

    template_name = "create_animals.html"

class CreateTouch(TemplateView):

    template_name = "create_touch.html"

class CreateFreeWrite(TemplateView):

    template_name = "create_free_write.html"

# END CREATE VIEWS



# START PROFILE VIEWS
class ProfileDetail(DetailView):

    template_name = "profile_detail.html"

class ProfileUpdate(UpdateView):

    template_name = "profile_update.html"

# END PROFILE VIEWS



# START POEM VIEWS
class PoemCreate(CreateView):

    def post(self, request, pk):
        
        name = request.POST.get("name")
        title = request.POST.get("title")
        body = request.POST.get("body")
        Poem.objects.create(name=name, title=title, body=body)
        return redirect("confirm-continue.html")

class PoemsIndex(TemplateView):

    template_name = "poems_index.html"

class PoemDetail(DetailView):

    model = Poem
    template_name = "poem_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poems"] = Poem.objects.all()

class Confirm(TemplateView):

    template_name = "confirm-continue.html"
    
# END POEM VIEWS