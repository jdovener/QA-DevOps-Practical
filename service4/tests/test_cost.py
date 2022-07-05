from application import app
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import application.routes

#Set up

class TestBase(TestCase):
    def create_app(self):
        return app

#Test

class TestCost(TestBase):
    def test_cost(self):
        response = self.client.post(
            url_for('cost'),
            json = {'activity':'Mini-Golf', 'location':'Manchester'}
        )
        self.assert200(response)
        self.assertIn(b'15', response.data)