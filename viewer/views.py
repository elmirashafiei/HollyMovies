from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import MovieForm, GenreForm
from .models import Movie
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from logging import getLogger

LOGGER = getLogger()



# Create your views here.
def hello(request, s0):
    s1 = request.GET.get('s1', '')  # Get the variable s1 from the URL encoder
    return render(
        request, template_name='viewer/hello.html',  # Template is the file you want to load
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']} # context are the variable you send to the template
    )
# Function view to show movies
def movie_list(request):
    movie_list = Movie.objects.all()
    return render(
        request,
        template_name="viewer/movies.html",
        context={'movies': movie_list}
    )
# Class based view to show movies
class MoviesView(View):
    def get(self, request):
        movie_list = Movie.objects.all()
        return render(
            request,
            template_name="viewer/movies.html",
            context={'movies': movie_list}
        )
# Template view class
class MoviesViewTemplate(TemplateView):
    template_name = "viewer/movies.html"
    extra_context = {'movies': Movie.objects.all()}


#List view class
class MoviesViewList(ListView):
    template_name = "viewer/movies.html"
    model = Movie


# class MovieCreateView(FormView):
#     template_name = "viewer/movie_form.html"
#     form_class = MovieForm
#     success_url = reverse_lazy("movies")
#     def form_valid(self, form):
#         result = super().form_valid(form) # Validate the form
#         cleaned_data = form.cleaned_data # Get me the data from the form
#         Movie.objects.create(
#             title=cleaned_data['title'],
#             genre=cleaned_data['genre'],
#             rating=cleaned_data['rating'],
#             released=cleaned_data['released'],
#             description=cleaned_data['description']
#         )
#         return result
#     def form_invalid(self, form):
#         LOGGER.warning('User provided invalid data.')
#         return super().form_invalid(form)


# class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#   template_name = 'viewer/movie_form.html'
#   form_class = MovieForm
#   success_url = reverse_lazy('movies')
#   permission_required = "viewer.add_movie"
#
#   def form_invalid(self, form):
#     LOGGER.warning('User provided invalid data.')
#     return super().form_invalid(form)
#
#
# class StaffRequiredMixin(UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.is_staff
#
#
class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class GenreCreateView(LoginRequiredMixin,PermissionRequiredMixin, StaffRequiredMixin, CreateView):
  template_name = 'viewer/genre_form.html'
  form_class = GenreForm
  success_url = reverse_lazy('movie_create')
  permission_required = "viewer.add_genre"

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data.')
    return super().form_invalid(form)
#
#
# class MovieUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
#   template_name = 'viewer/genre_form.html'
#   model = Movie
#   form_class = MovieForm
#   success_url = reverse_lazy('movies')
#   permission_required = "viewer.change_movie"
#
#   def form_invalid(self, form):
#     LOGGER.warning('User provided invalid data.')
#     return super().form_invalid(form)
#
#
# class MovieDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
#   template_name = 'viewer/delete_form.html'
#   model = Movie
#   success_url = reverse_lazy('movies')
#   permission_required = "viewer.delete_movie"
#
#
# class MovieDetailView(DetailView):
#   template_name = 'viewer/movie_details.html'
#   model = Movie



# Requires Log in, and Permission to add, and staff status
class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, StaffRequiredMixin, CreateView):
  template_name = 'viewer/movie_form.html'
  form_class = MovieForm
  success_url = reverse_lazy('movies')
  permission_required = "viewer.add_movie"


# Requires Log in, and Permission to change
class MovieUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "viewer/movie_form.html"
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("movies")
    permission_required = "viewer.change_movie"
    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)

# Requires Log in, and Permission to delete, and staff status and superuser status
class MovieDeleteView(LoginRequiredMixin, PermissionRequiredMixin, StaffRequiredMixin, DeleteView):
    template_name = "viewer/delete_form.html"
    model = Movie
    success_url = reverse_lazy("movies")
    permission_required = "viewer.delete_movie"
    def test_func(self):
        return super().test_func() and self.request.user.is_superuser
# It does not require any permissions nor Log in
class MovieDetailView(DetailView):
    template_name = "viewer/movie_details.html"
    model = Movie
