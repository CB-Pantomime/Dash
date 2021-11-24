from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# IMPORT MODELS
from .models import Poem


# ALL VIEWS
class Home(TemplateView):

    template_name = "home.html"



# START ACCOUNT VIEWS
class Signup(View):

    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    # on form submit validate the form and login the user
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home.html")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

# END ACCOUNT VIEWS



# START PROFILE VIEWS
@method_decorator(login_required, name='dispatch')
class ProfileDetail(DetailView):

    model = User
    template_name = "profile_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context["poems"] = Poem.objects.all()
    #     return context


# class ProfileUpdate(UpdateView):

#     template_name = "profile_update.html"

# END PROFILE VIEWS



# START CREATE VIEWS
@method_decorator(login_required, name='dispatch')
class CreateIndex(TemplateView):

    template_name = "create_index.html"

@method_decorator(login_required, name='dispatch')
class CreateBeach(TemplateView):

    template_name = "create_beach.html"

@method_decorator(login_required, name='dispatch')
class CreateAnimals(TemplateView):

    template_name = "create_animals.html"

@method_decorator(login_required, name='dispatch')
class CreateTouch(TemplateView):

    template_name = "create_touch.html"

@method_decorator(login_required, name='dispatch')
class CreateFreeWrite(TemplateView):

    
    template_name = "create_free_write.html"

    # def post(self, request, user_id):
    #     def get_user(request):
    #         current_user = request.user
    #         return current_user
        
    #     name = request.POST.get("name")
    #     title = request.POST.get("title")
    #     body = request.POST.get("body")
    #     Poem.objects.create(name=name, title=title, body=body)
    #     return redirect("confirm-continue.html")

# END CREATE VIEWS






# START POEM VIEWS
@method_decorator(login_required, name='dispatch')
class PoemCreate(View):

    def post(self, request):
        # print(f'Here is name: {request.POST}')
        name = request.POST.get("name")
        title = request.POST.get("title")
        body = request.POST.get("body")       
        Poem.objects.create(name=name, title=title, body=body)
        return redirect("confirm-continue")

    def form_valid(self, form):
            form.instance.user = self.request.user
            return super(PoemCreate, self).form_valid(form)








@method_decorator(login_required, name='dispatch')
class PoemsIndex(TemplateView):

    model = Poem
    template_name = "poems_index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["poems"] = Poem.objects.filter(name__icontains=name)
        else:

            context["poems"] = Poem.objects.all()
        return context

    def form_valid(self, form):

            form.instance.user = self.request.user
            return super(PoemsIndex, self).form_valid(form)







@method_decorator(login_required, name='dispatch')
class PoemDetail(DetailView):

    model = Poem
    template_name = "poem_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poems"] = Poem.objects.all()

@method_decorator(login_required, name='dispatch')
class Confirm(TemplateView):

    template_name = "confirm-continue.html"
    
# END POEM VIEWS