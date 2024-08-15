from django.http import HttpResponse
from django.shortcuts import render

from errors import settings


def error_page(request, status_code):
    if status_code not in [403, 404, 500, 502, 504]:
        return HttpResponse(status_code, status=status_code)

    return render(
        request,
        f"{status_code}.html",
        {
            "hostname": settings.ERRORS_HOSTNAME,
        },
        status=status_code,
    )
