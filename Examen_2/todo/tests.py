from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo


class TodoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_todo_creation(self):
        todo = Todo.objects.create(
            title='Test Todo',
            user=self.user
        )
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.user, self.user)
        self.assertFalse(todo.completed)
        
    def test_todo_str_representation(self):
        todo = Todo.objects.create(
            title='Test Todo',
            user=self.user
        )
        self.assertEqual(str(todo), 'Test Todo')
