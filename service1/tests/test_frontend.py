from application import app
import application.routes
from flask import url_for
from flask_testing import TestCase
import requests_mock

# Set up

class TestBase(TestCase):
    def create_app(self):
        return app

# Test

class TestFront(TestBase):
    def test_get_front(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5000/get_activity', text = 'Mini-Golf')
            m.get('http://service3:5000/get_location', text = 'Manchester')
            m.post('http://service4:5000/cost', text = 'Mini-Golf in Manchester! Which will cost: £15')
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'15', response.data)