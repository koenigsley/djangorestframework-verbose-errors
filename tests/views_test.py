import unittest

from django.conf import settings

settings.configure()

from rest_framework.exceptions import APIException

from rest_framework_verbose_errors.views import exception_handler


class ViewsTestCase(unittest.TestCase):
    def test_exception_handler_returns_correct_response_if_detail_is_str(self):
        exc = APIException('You are not authenticated')
        context = {}
        response = exception_handler(exc, context)
        expected = {
            'errors': [
                {
                    'field': None,
                    'messages': ['You are not authenticated'],
                },
            ],
        }
        self.assertEqual(expected, response.data)

    def test_exception_handler_returns_correct_response_if_detail_is_dict_which_contains_detail_key(self):
        exc = APIException({'detail': 'Permisssion denied'})
        context = {}
        response = exception_handler(exc, context)
        expected = {
            'errors': [
                {
                    'field': None,
                    'messages': ['Permisssion denied'],
                },
            ],
        }
        self.assertEqual(expected, response.data)

    def test_exception_handler_returns_correct_response_if_detail_is_list(self):
        exc = APIException(['Invalid name', 'Invalid age'])
        context = {}
        response = exception_handler(exc, context)
        expected = {
            'errors': [
                {
                    'field': None,
                    'messages': ['Invalid name', 'Invalid age'],
                },
            ],
        }
        self.assertEqual(expected, response.data)

    def test_exception_handler_returns_correct_response_if_detail_is_tuple(self):
        exc = APIException(('Invalid name', 'Invalid age'))
        context = {}
        response = exception_handler(exc, context)
        expected = {
            'errors': [
                {
                    'field': None,
                    'messages': ['Invalid name', 'Invalid age'],
                },
            ],
        }
        self.assertEqual(expected, response.data)

    def test_exception_handler_returns_correct_response_if_detail_is_dict_which_contains_list_value(self):
        exc = APIException(
            {
                'name': [
                    'This field is required',
                    'This field can not be null',
                ],
            },
        )
        context = {}
        response = exception_handler(exc, context)
        expected = {
            'errors': [
                {
                    'field': 'name',
                    'messages': ['This field is required', 'This field can not be null'],
                },
            ],
        }
        self.assertEqual(expected, response.data)
