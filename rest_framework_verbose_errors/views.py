from rest_framework.views import exception_handler as _exception_handler


def exception_handler(exc, context):
    response = _exception_handler(exc, context)
    if response is not None:
        if isinstance(response.data, dict) and 'detail' in response.data:
            detail = response.data['detail']
        else:
            detail = response.data

        if isinstance(detail, dict):
            errors = [{
                'field': field,
                'messages': messages,
            } for field, messages in detail.items()]
        else:
            messages = detail if isinstance(detail, list) else [detail]
            errors = [{
                'field': None,
                'messages': messages,
            }]

        response.data = {'errors': errors}

    return response
