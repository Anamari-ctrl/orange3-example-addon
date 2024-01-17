import unittest
from Orange.widgets.tests.base import WidgetTest

from orangecontrib.example.widgets.owFileUpload import uploadFile


class ExampleTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)


class TestMyWidget(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(uploadFile)

    def test_addition(self):
        self.assertEqual(1 + 1, 2)
