from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')


# see https://cloud.google.com/appengine/docs/python/issue-requests#issuing_an_http_request
import requests
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

# also monkey patch platform.platform() from https://code.google.com/p/googleappengine/issues/detail?id=12982
import platform

def patch(module):
    def decorate(func):
        setattr(module, func.func_name, func)
        return func
    return decorate


@patch(platform)
def platform():
    return 'AppEngine'