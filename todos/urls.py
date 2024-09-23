from django.urls import path
from todos import views

urlpatterns = [
    path('todos/', views.TodosAPIView.as_view(), name='todos-list-create'),
    path('todo/<int:pk>/', views.TodoAPIView.as_view(), name='todo-detail'),
]