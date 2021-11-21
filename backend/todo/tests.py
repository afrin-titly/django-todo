from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', description='a body here')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected = f'{todo.title}'
        self.assertEqual(expected, 'first todo')

    def test_description_content(self):
        todo = Todo.objects.get(id=1)
        expected = f'{todo.description}'
        self.assertEqual(expected, 'a body here')
