from django.conf import settings
import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes, throttle_classes
from core.api.user_data import get_user_data
from django.shortcuts import redirect
from rest_framework.request import Request
from django.http import HttpResponseRedirect
from core import tools

PUBLIC_PAGES = ["/article", "articles"]

def get_page_props(request, path):
    if path in ["/article", "article"]:
        return {
            "feed": {

            }
        }
    return {
        "connection": {
            "state": "unauthenticated"
        }
    }


@api_view(['GET'])
def index(request, path):
    # TODO: use authentication based redirect instead
    print("User requesting path", path)

    if request.user.is_authenticated and (not path in PUBLIC_PAGES):
        return render_nextjs_page(get_user_data(request.user, request), path=path)
    elif (not request.user.is_authenticated) and (path in PUBLIC_PAGES):
        return render_nextjs_page({
            
        }, path=path)
    else:
        if not (path in ["/login", "login"]):
            return HttpResponseRedirect("/login")
        return render_nextjs_page({
            "connection": {
                "state": "unauthenticated"
            }
        }, path=path)


def render_nextjs_page(data, path=""):
    url = settings.NEXTJS_HOST_URL
    url = f"{url}/{path}"
    print(f"TBS Routing to {url}")
    resp = requests.post(url, json=data)
    return HttpResponse(resp.text)
