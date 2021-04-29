from django.test import TestCase

# Create your tests here.


class TestModels(TestCase):

    def test_assertions(self):
        is_true = True
        self.assertIs(is_true, True, "Give value is not True")
