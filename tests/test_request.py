
from http.cookies import SimpleCookie
from unittest import TestCase, main

from antfarm import request

BASE_ENVIRON = {'REQUEST_METHOD': 'GET'}
class RequestTest(TestCase):


    def test_001_content_type(self):
        req = request.Request(None, BASE_ENVIRON)
        self.assertEqual(req.content_type, '')

        req = request.Request(None, dict(BASE_ENVIRON,
            CONTENT_TYPE='text/plain',
        ))
        self.assertEqual(req.content_type, 'text/plain')

        req = request.Request(None, dict(BASE_ENVIRON,
            CONTENT_TYPE='text/plain; charset=utf-8',
        ))
        self.assertEqual(req.content_type, 'text/plain')
        self.assertEqual(req.content_params['charset'], 'utf-8')

    def test_002_cookies(self):
        req = request.Request(None, BASE_ENVIRON)
        self.assertEqual(req.cookies, {})

        req = request.Request(None, dict(BASE_ENVIRON,
            HTTP_COOKIE='keebler="E=everybody; L=\\"Loves\\"; fudge=\\012;";',
        ))
        self.assertEqual(req.cookies['keebler'], "E=everybody; L=\"Loves\"; fudge=\012;")

if __name__ == '__main__':
    main()
