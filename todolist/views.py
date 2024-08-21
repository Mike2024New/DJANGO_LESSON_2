from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from .models import Todo
# Create your views here.

def index(request):
    todolist = Todo.objects.all()
    context = {
        'title':'Главная страница',
        'todolist':todolist
    }
    return render(request, 'todolist/index.html',context)

@require_http_methods(['POST'])
def add(request):
    title=request.POST['title']
    todo = Todo(title=title)
    todo.save()
    return redirect('todolist:index')

def update(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.is_complete= not todo.is_complete
        todo.save()
        return redirect('todolist:index')
    except:
        return redirect('todolist:index')
    
def delete(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('todolist:index')
    except:
        return redirect('todolist:index')