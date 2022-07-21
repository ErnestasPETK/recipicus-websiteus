"""

Sample tests for the app.

"""
from django.test import SimpleTestCase
from rest_framework.test import APIClient

from app import calc


class CalcTests(SimpleTestCase):
    """
    Test calc module
    """

    def test_add_numbers(self):
        """
        Test add numbers
        """
        result = calc.add(1, 2)

        self.assertEqual(result, 3)

    def test_subtract_numbers(self):
        """
        Test subtract numbers
        """
        result = calc.subtract(15, 10)

        self.assertEqual(result, 5)


# class TestViews(SimpleTestCase):
#     def test_get_greetings(self):
#         """
#         Test get greetings
#         """
#         client = APIClient()
#         response = client.get("/greetings/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, "Hello World")
