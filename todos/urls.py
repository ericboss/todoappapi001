from todos.views import TodosAPIView,TodoDetailAPIView
#CreateTodoAPIView, TodoListAPIView
from django.urls import path


urlpatterns = [
  
   path('', TodosAPIView.as_view(), name="todos"),
   path('<int:id>', TodoDetailAPIView.as_view(), name="todo"),

]
