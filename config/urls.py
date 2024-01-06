from django.urls import path
from .views import home, detail

urlpatterns = [
    path('', home),
    path('project/<int:id>/', detail, name='project_detail'),
]
