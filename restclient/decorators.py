from restclient import GET, POST, DELETE, PUT
from string import Template
import urllib

def get(f):
    """Decorator to wrap a function as a GET call.
    The decorated function must return a dictionary with the restclient options*

    """
    def wrapper(*args, **kargs):
        func_dict = f(*args, **kargs)
        url = func_dict['url']
        # do url magic

        if 'url_param' in func_dict:
            url = Template(url).substitute(func_dict['url_param'])
        response = GET(url,
                       params = func_dict.get('params', None),
                       files  = func_dict.get('files', None),
                       accept = func_dict.get('accept',[]),
                       headers= func_dict.get('headers', None),
                       async  = func_dict.get('async', False),
                       resp   = func_dict.get('resp', False),
                       credentials= func_dict.get('credentials', None))
        return response
    return wrapper



def post(f):
    """Decorator to wrap a function as a POST call.
    The decorated function must return a dictionary with the restclient options*

    * url is required,
    * added url_param not existant in the restclient functions that allows
    * to add param to the url part.
    * added get_param: allows to add get parameters even if it is a POST call.

    """
    def wrapper(*args, **kargs):
        func_dict = f(*args, **kargs)
        url = func_dict['url']
        # do url magic

        if 'url_param' in func_dict:
            url = Template(url).substitute(func_dict['url_param'])

        if 'get_param' in func_dict:
            url = url + '?' + urllib.urlencode(func_dict['get_param'])
            
        response = POST(url,
                       params = func_dict.get('params', None),
                       files  = func_dict.get('files', None),
                       accept = func_dict.get('accept',[]),
                       headers= func_dict.get('headers', None),
                       async  = func_dict.get('async', False),
                       resp   = func_dict.get('resp', False),
                       credentials= func_dict.get('credentials', None))
        return response
    return wrapper


def delete(f):
    pass

def put(f):
    pass
