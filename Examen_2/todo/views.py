from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm


def home(request):
    """Vista principal con las opciones de lista"""
    return render(request, 'todo/home.html')


def login_view(request):
    """Vista para el login de usuarios"""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo:home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})


def register_view(request):
    """Vista para registro de usuarios"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cuenta creada exitosamente')
            return redirect('todo:home')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})


def logout_view(request):
    """Vista para logout"""
    logout(request)
    return redirect('todo:login')


# Vistas para listar todos los pendientes
@login_required
def todos_ids_only(request):
    """Lista de todos los pendientes del usuario (solo IDs)"""
    todos = Todo.objects.filter(user=request.user).values('id')
    return render(request, 'todo/todos_ids_only.html', {'todos': todos})


@login_required
def todos_ids_titles(request):
    """Lista de todos los pendientes del usuario (IDs y Titles)"""
    todos = Todo.objects.filter(user=request.user).values('id', 'title')
    return render(request, 'todo/todos_ids_titles.html', {'todos': todos})


@login_required
def todos_pending_id_title(request):
    """Lista de todos los pendientes sin resolver del usuario (ID y Title)"""
    todos = Todo.objects.filter(user=request.user, completed=False).values('id', 'title')
    return render(request, 'todo/todos_pending_id_title.html', {'todos': todos})


@login_required
def todos_completed_id_title(request):
    """Lista de todos los pendientes resueltos del usuario (ID y Title)"""
    todos = Todo.objects.filter(user=request.user, completed=True).values('id', 'title')
    return render(request, 'todo/todos_completed_id_title.html', {'todos': todos})


@login_required
def todos_ids_userids(request):
    """Lista de todos los pendientes del usuario (IDs y userID)"""
    todos = Todo.objects.filter(user=request.user).values('id', 'user_id')
    return render(request, 'todo/todos_ids_userids.html', {'todos': todos})


@login_required
def todos_completed_id_userid(request):
    """Lista de todos los pendientes resueltos del usuario (ID y userID)"""
    todos = Todo.objects.filter(user=request.user, completed=True).values('id', 'user_id')
    return render(request, 'todo/todos_completed_id_userid.html', {'todos': todos})


@login_required
def todos_pending_id_userid(request):
    """Lista de todos los pendientes sin resolver del usuario (ID y userID)"""
    todos = Todo.objects.filter(user=request.user, completed=False).values('id', 'user_id')
    return render(request, 'todo/todos_pending_id_userid.html', {'todos': todos})


# CRUD Operations
@login_required
def todo_list(request):
    """Lista completa de todos para el usuario logueado"""
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo/todo_list.html', {'todos': todos})


@login_required
def todo_create(request):
    """Crear un nuevo todo"""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, 'Tarea creada exitosamente')
            return redirect('todo:todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form, 'title': 'Crear Tarea'})


@login_required
def todo_detail(request, pk):
    """Detalle de un todo específico"""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


@login_required
def todo_update(request, pk):
    """Actualizar un todo existente"""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada exitosamente')
            return redirect('todo:todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form, 'title': 'Editar Tarea'})


@login_required
def todo_delete(request, pk):
    """Eliminar un todo"""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Tarea eliminada exitosamente')
        return redirect('todo:todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})


@login_required
def todo_toggle_complete(request, pk):
    """Marcar/desmarcar como completado"""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'completed': todo.completed,
            'message': 'Completado' if todo.completed else 'Pendiente'
        })
    
    return redirect('todo:todo_list')
