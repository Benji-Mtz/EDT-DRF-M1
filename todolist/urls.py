from django.urls import path
from . import views

urlpatterns = [
    # as_view() para trabsformar la clase a un metodo o funcion
    path('', views.IndexView.as_view()),
    path('tarea/', views.TareaView.as_view()),
    path('tarea/<int:pk>', views.TareaDetailView.as_view()),
]
