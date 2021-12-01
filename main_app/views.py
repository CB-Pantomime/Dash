from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.urls import reverse

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
            return redirect("/")
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


# ***************************************
# JUST WORKING WITH THIS ONE FOR NOW
@method_decorator(login_required, name='dispatch')
class CreateFreeWrite(CreateView):

    model = Poem
    fields = ['name', 'title', 'body']
    template_name = "create_free_write.html"
    
    # This is our new method that will add the user into our submitted form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateFreeWrite, self).form_valid(form)

    # def get_success_url(self):
    #     return reverse('/')

    def get_success_url(self):
       return reverse('poem_detail', kwargs={'pk': self.object.pk})

   



    # def get_success_url(self):
    #     return redirect('confirm')
    # success_url = "confirm"
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
# @method_decorator(login_required, name='dispatch')
# class PoemCreate(View):

#     def post(self, request):
#         print(f'Here is name: {request.POST}')
#         name = request.POST.get("name")
#         title = request.POST.get("title")
#         body = request.POST.get("body")       
#         Poem.objects.create(name=name, title=title, body=body)
#         return redirect("confirm")

#     def form_valid(self, form):
#             form.instance.user = self.request.user
#             return super(PoemCreate, self).form_valid(form)


# @method_decorator(login_required, name='dispatch')
# class PoemCreate(CreateView):
#     model = Poem
#     fields = ['name', 'title', 'body']
#     template_name = "create_free_write.html"
    # success_url = "confirm"
    # This is our new method that will add the user into our submitted form
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(PoemCreate, self).form_valid(form)

    # def get_success_url(self):
    #     return redirect('confirm')
    # success_url = "confirm"


# class ArtistCreate(CreateView):
#     model = Artist
#     fields = ['name', 'img', 'bio', 'verified_artist']
#     template_name = "artist_create.html"

#     # This is our new method that will add the user into our submitted form
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(ArtistCreate, self).form_valid(form)

#     def get_success_url(self):
#         return reverse('artist_detail', kwargs={'pk': self.object.pk})




@method_decorator(login_required, name='dispatch')
class PoemsIndex(TemplateView):

    template_name = "poems_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["poems"] = Poem.objects.filter(name__icontains=name, user=self.request.user)
        else:
            context["poems"] = Poem.objects.filter(user=self.request.user)
        return context

    # def form_valid(self, form):

    #         form.instance.user = self.request.user
    #         return super(PoemsIndex, self).form_valid(form)



@method_decorator(login_required, name='dispatch')
class PoemDetail(DetailView):

    model = Poem
    template_name = "poem_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poems"] = Poem.objects.all()
        return context 




@method_decorator(login_required, name='dispatch')
class PoemUpdate(UpdateView):

    model = Poem
    fields = ['name','title','body']
    template_name = "poem_update.html"
    success_url = "/"


@method_decorator(login_required, name='dispatch')
class PoemDelete(DeleteView):

    model = Poem
    template_name = "poem_delete_confirmation.html"
    success_url = "/"










@method_decorator(login_required, name='dispatch')
class Confirm(TemplateView):

    template_name = "confirm.html"
    
# END POEM VIEWS