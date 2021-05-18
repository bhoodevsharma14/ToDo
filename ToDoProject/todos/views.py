from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_todo_items(request):
    return render(request,'todos/todos.html')