from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService3(TestBase):
    def test_hero(self):
        response = self.client.post(url_for('post_rpgrole'), data='Hero')
        self.assertIn(b'HP: 1200 MP: 500', response.data)

    def test_dragonrider(self):
        response = self.client.post(url_for('post_rpgrole'), data='Dragon Rider')
        self.assertIn(b'HP: 1500 MP: 200', response.data)

    def test_knight(self):
        response = self.client.post(url_for('post_rpgrole'), data='Knight')
        self.assertIn(b'HP: 2000 MP: 100', response.data)

    def test_healer(self):
        response = self.client.post(url_for('post_rpgrole'), data='Healer')
        self.assertIn(b'HP: 600 MP: 1000', response.data)

    def test_demon_king(self):
        response = self.client.post(url_for('post_rpgrole'), data='Demon King')
        self.assertIn(b'HP: 10,000 MP: 5000', response.data)

    def test_royal_jester(self):
        response = self.client.post(url_for('post_rpgrole'), data='Royal Jester')
        self.assertIn(b'HP: 100 MP: 1', response.data)
    
    def test_thief(self):
        response = self.client.post(url_for('post_rpgrole'), data='Thief')
        self.assertIn(b'HP: 800 MP: 250', response.data)

    def test_assassin(self):
        response = self.client.post(url_for('post_rpgrole'), data='Assassin')
        self.assertIn(b'HP: 1000 MP: 300', response.data)

    def test_mage(self):
        response = self.client.post(url_for('post_rpgrole'), data='Mage')
        self.assertIn(b'HP: 300 MP: 3000', response.data)

    def test_metal_slime(self):
        response = self.client.post(url_for('post_rpgrole'), data='Metal Slime')
        self.assertIn(b'HP: 5000 MP: 0', response.data)
