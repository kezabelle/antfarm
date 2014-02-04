
from unittest import TestCase, main

from antfarm import App, Response
from antfarm.http import STATUS

BASE_ENV = {
    'REQUEST_METHOD': 'GET',
}

class AppTest(TestCase):

    def test_001_basic(self):
        app = App(root_view=lambda r: Response('true'))

        self.status, self.headers = None, None
        def start_response(s, h):
            self.status = s
            self.headers = h

        resp = app(BASE_ENV, start_response)

        self.assertEqual(self.status, '200 OK')
        self.assertTrue(any(h[0] == 'Content-Type' for h in  self.headers))
        self.assertEqual(resp, [b'true'])

if __name__ == '__main__':
    main()
