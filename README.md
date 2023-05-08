# Verbose Errors

A simple package for DRF errors formatting

## Setting up

Install this package using pip

```bash
pip install djangorestframework-verbose-errors
```

Register the exception handler

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework_verbose_errors.views.exception_handler'
}
```
