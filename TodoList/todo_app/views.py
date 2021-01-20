from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Todo
#Create your views here. (contorller)
# request로 부터 parameter valid check
# business method 호출 또는 구현
# view(template)에서 참조할 데이터 저장
# view(template) 선택
#todo_app/
def index(request):
    todos = Todo.objects.all()
    context = {"todos": todos}

    return render(request, 'index.html',context)
#todo_app/createTodo
def createTodo(request):
    todoContent = request.POST['todoContent']
    new_todo = Todo(content =todoContent)
    new_todo.save()
    return HttpResponseRedirect(reverse("index"))

#todo_app/todoList
def todoList(request):
    pass

#todo_app/deleteTodo
def deleteTodo(request):
    delete_todo_id = request.GET['id']
    print("삭제 :", delete_todo_id)
    todo = Todo.objects.get(id = delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse("index"))
        

