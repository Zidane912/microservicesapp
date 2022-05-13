from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService2(TestBase):
    def test_hero(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Hero', response.data)

    def test_dragonr(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Dragon Rider', response.data)

    def test_knight(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Knight', response.data)

    def test_healer(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Healer', response.data)

    def test_demon_king(self):
        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Demon King', response.data)

    def test_royal_jester(self):
        with patch('random.randint') as r:
            r.return_value = 5
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Royal Jester', response.data)

    def test_thief(self):
        with patch('random.randint') as r:
            r.return_value = 6
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Thief', response.data)

    def test_assassin(self):
        with patch('random.randint') as r:
            r.return_value = 7
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Assassin', response.data)

    def test_mage(self):
        with patch('random.randint') as r:
            r.return_value = 8
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Mage', response.data)
    
    def test_metal_slime(self):
        with patch('random.randint') as r:
            r.return_value = 9
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Metal Slime', response.data)



# if pytest --cov=application doesnt work
# use py.test --cov=application
# 90% test coverage atm
# probably need to test the repsonse too
# like self.assertEqual(response.status_code, 200)