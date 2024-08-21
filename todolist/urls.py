from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path('',view=views.index,name='index'),
    path('add/',view=views.add, name='add'),
    path('update/<int:todo_id>/',view=views.update, name='update'),
    path('delete/<int:todo_id>/',view=views.delete, name='delete')
]
