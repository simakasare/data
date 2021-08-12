from django.contrib import admin
from django.urls import path
from.views import CreateView ,Retrieve_ListView,Retrieve_DetailView,UpdateView,DeleteView



urlpatterns = [
  path('data/create', CreateView),
  path('data/', Retrieve_ListView),
  path('data/<int:_id>',Retrieve_DetailView),
  path('data/<int:_id>/update', UpdateView),
  path('data/<int:_id>/delete', DeleteView),

]