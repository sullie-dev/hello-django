from django.test import TestCase
from .forms import ItemsForm

class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemsForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemsForm({'name': 'Test Todo Form'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_forms_metaclass(self):
        form = ItemsForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
