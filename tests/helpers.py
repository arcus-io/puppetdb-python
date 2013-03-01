from mock import Mock
import fixtures
import json

NODES = {
    'name': 'foo'
}

def mock_api_request(host_url=None, path=None, *args, **kwargs):
    resp = Mock()
    # HACK: find the api version in url
    data = None
    if host_url.find('v2') > -1:
        data = fixtures.v2().get(path)
    resp.content = json.dumps(data)
    resp.headers = kwargs.get('headers')
    return resp
