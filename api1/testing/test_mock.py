from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService1(TestBase):
    def test_hero(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Hero')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 1200 MP: 500')
            m.post('http://localhost:5003/post/desc', text='Hero,HP: 1200 MP: 500')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Hero', response.data)

    def test_dragon_rider(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Dragon Rider')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 1500 MP: 200')
            m.post('http://localhost:5003/post/desc', text='Dragon Rider,HP: 1500 MP: 200')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Dragon Rider', response.data)

    def test_knight(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Knight')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 2000 MP: 100')
            m.post('http://localhost:5003/post/desc', text='Knight,HP: 2000 MP: 100')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Knight', response.data)
    
    def test_healer(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Healer')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 600 MP: 1000')
            m.post('http://localhost:5003/post/desc', text='Healer,HP: 600 MP: 1000')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Healer', response.data)

    def test_demon_king(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Demon King')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 10,000 MP: 5000')
            m.post('http://localhost:5003/post/desc', text='Demon King,HP: 10,000 MP: 5000')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Demon King', response.data)

    def test_royal_jester(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Jester')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 100 MP: 1')
            m.post('http://localhost:5003/post/desc', text='Jester,HP: 100 MP: 1')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Jester', response.data)
    
    def test_thief(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Thief')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 800 MP: 250')
            m.post('http://localhost:5003/post/desc', text='Thief,HP: 800 MP: 250')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Thief', response.data)

    def test_assassin(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Assassin')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 1000 MP: 300')
            m.post('http://localhost:5003/post/desc', text='Assassin,HP: 1000 MP: 300')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Assassin', response.data)

    def test_metal_slime(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Metal Slime')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 5000 MP: 0')
            m.post('http://localhost:5003/post/desc', text='Metal Slime,HP: 5000 MP: 0')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Metal Slime', response.data)

    def test_mage(self):
        with requests_mock.Mocker() as m:
            m.get('http://localhost:5001/get/rpgrole', text='Mage')
            m.post('http://localhost:5002/post/rpgrole', text='HP: 300 MP: 3000')
            m.post('http://localhost:5003/post/desc', text='Mage,HP: 300 MP: 3000')
            response = self.client.get(url_for('get_rpgrole'))
            self.assertIn(b'Mage', response.data)
