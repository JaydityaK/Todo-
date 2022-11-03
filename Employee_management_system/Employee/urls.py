from django.urls import path
from Employee import views
urlpatterns = [
    path('add/', views.add),
    path('delete/<int:tid>', views.delete),
    path('update/<int:tid>', views.update),
]
