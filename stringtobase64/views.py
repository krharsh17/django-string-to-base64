from django.http import HttpResponse

import base64


def index(request):
    input_string = request.GET.get('input_string')

    if input_string is None:
        return HttpResponse("Please provide a valid 'input_string' parameter in the query.")

    b = base64.b64encode(bytes(input_string, 'utf-8'))
    base64_str = b.decode('utf-8')

    return HttpResponse(base64_str)