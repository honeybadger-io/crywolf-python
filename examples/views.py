from django.shortcuts import render

from django.http import HttpResponse

from honeybadger import honeybadger


def index(request):
    return HttpResponse("Hello, world. You're at the crywolf index.<br><br>Looking to <a href='/fail/?foo=bar&amp;bar=baz&amp;user_email=user@example.com'>fail</a>?")


def fail(request):
    with honeybadger.context(user_email=request.GET.get('user_email', None)):
        raise RuntimeError(
            "This is a runtime error generated by the crywolf app.")
