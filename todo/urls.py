from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Listas específicas requeridas
    path('todos/ids-only/', views.todos_ids_only, name='todos_ids_only'),
    path('todos/ids-titles/', views.todos_ids_titles, name='todos_ids_titles'),
    path('todos/pending/id-title/', views.todos_pending_id_title, name='todos_pending_id_title'),
    path('todos/completed/id-title/', views.todos_completed_id_title, name='todos_completed_id_title'),
    path('todos/ids-userids/', views.todos_ids_userids, name='todos_ids_userids'),
    path('todos/completed/id-userid/', views.todos_completed_id_userid, name='todos_completed_id_userid'),
    path('todos/pending/id-userid/', views.todos_pending_id_userid, name='todos_pending_id_userid'),
    
    # CRUD operations
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/create/', views.todo_create, name='todo_create'),
    path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todos/<int:pk>/update/', views.todo_update, name='todo_update'),
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    path('todos/<int:pk>/toggle/', views.todo_toggle_complete, name='todo_toggle_complete'),
]
