from application import app
import application.routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

# Set up

class TestBase(TestCase):
    def create_app(self):
        return app

# Tests

class TestLocations(TestBase):
    @patch('random.choice', return_value='Manchester')
    def test_get_locations(self, patched):
        response = self.client.get(url_for('location'))
        self.assert200(response)
        self.assertIn(b'Manchester', response.data)

#patch more useful for service1
#'requests mock' for service2 and 3, QACommunicty>python advanced>test mocking