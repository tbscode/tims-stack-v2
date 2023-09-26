from django.conf import settings
from bs4 import BeautifulSoup
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

    # Matomo Tag
    matomo_tag = """var _paq = window._paq = window._paq || [];
                      _paq.push(['trackPageView']);
                      _paq.push(['enableLinkTracking']);
                      (function() {
                        var u="//localhost:8080/";
                        _paq.push(['setTrackerUrl', u+'matomo.php']);
                        _paq.push(['setSiteId', '1']);
                        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
                        g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
                      })();
                      """

    # Parse HTML
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Create new tag
    new_tag = soup.new_tag('script')
    new_tag.string = matomo_tag
    soup.head.append(new_tag)

    # Rendered HTML
    rendered_html = str(soup)

    # Return the HTML response as usual.
    return HttpResponse(rendered_html)
