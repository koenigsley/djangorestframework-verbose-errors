# Verbose Errors

[![Test](https://github.com/koenigsley/djangorestframework-verbose-errors/actions/workflows/test.yaml/badge.svg)](https://github.com/koenigsley/djangorestframework-verbose-errors/actions/workflows/test.yaml)

A simple package for DRF errors formatting

## Requirements

- Python 3.6 or newer
- Django 3.2 or newer
- Django Rest Framework 3.14 or newer

## Formatting

This package provides the exception handler that formats handled DRF exceptions into verbose error response

### Generic error

```json
{
  "errors": [
    {
      "field": null,
      "messages": [
        "You do not have enough permissions to perform this action"
      ]
    }
  ]
}
```

### Error related to an object field

```json
{
  "errors": [
    {
      "field": "name",
      "messages": [
        "This field is required", 
        "This field can not be null"
      ]
    }
  ]
}
```

## Installation

You can install this package using pip:

```shell
pip install djangorestframework-verbose-errors
```

## Configuration

Configure your project in order to use the exception handler:

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework_verbose_errors.views.exception_handler',
}
```

## License

[MIT](https://github.com/koenigsley/djangorestframework-verbose-errors/blob/main/LICENSE)
