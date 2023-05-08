import unittest

from django.conf import settings
from rest_framework.exceptions import APIException

from rest_framework_verbose_errors.views import exception_handler

settings.configure()


class ViewsTestCase(unittest.TestCase):

    def test_exception_handler_returns_correct_response_if_detail_is_str(self):
        exc = APIException("error")
        context = {}
        response = exception_handler(exc, context)
        expected = {
            "errors": [{
                "field": None,
                "messages": ["error"],
            }]
        }
        self.assertEqual(expected, response.data)

    def test_exception_handler_returns_correct_response_if_detail_is_detail_dict(
            self):
        exc = APIException({"detail": "error"})
        context = {}
        response = exception_handler(exc, context)
        expected = {
            "errors": [{
                "field": None,
                "messages": ["error"],
            }]
        }
        self.assertEqual(expected, response.data)

    def test_exception_handler_returns_correct_response_if_detail_is_dict_with_list(
        self, ):
        exc = APIException(
            {"name": ["This field is required", "This field can not be null"]})
        context = {}
        response = exception_handler(exc, context)
        expected = {
            "errors": [{
                "field":
                "name",
                "messages": [
                    "This field is required",
                    "This field can not be null",
                ],
            }]
        }
        self.assertEqual(expected, response.data)
