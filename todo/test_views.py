from django.test import TestCase
from .models import Items

# Create your tests here.
class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')
    
    def test_edit_item_page(self):
        item = Items.objects.create(name="Test Todo")
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        res = self.client.post('/add', {'name': "Test Todo Item"})
        self.assertRedirects(res, '/')

    def test_can_delete_item(self):
        item = Items.objects.create(name="Test Todo")
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Items.objects.filter(id = item.id)
        self.assertEqual(len(existing_items), 0)
        
    def test_can_toggle_item(self):
        item = Items.objects.create(name="Test Todo Item", done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Items.objects.get(id= item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Items.objects.create(name="Test Todo Item", done=True)
        response = self.client.post(f'/edit/{item.id}', {'name': 'This is the updated name'})
        self.assertRedirects(response, '/')
        updated_item = Items.objects.get(id= item.id)
        self.assertEqual(updated_item.name, 'This is the updated name')
