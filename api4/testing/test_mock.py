from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService3(TestBase):
    def test_hero(self):

        # considering making it a variable for neatness i.e. [] = hero_list_item then pass to data

        response = self.client.post(url_for('post_desc'), data=','.join(['Hero', 'HP: 1200 MP: 500']))
        self.assertIn(b'Strong and versatile skillset, tasked with slaying the Demon King. Special Trait: Wielder of excalibur, the only sword that can harm the Demon King.', response.data)

    def test_dragonrider(self):
        response = self.client.post(url_for('post_desc'), data=','.join(['Dragon Rider', 'HP: 1500 MP: 200']))
        self.assertIn(b'Raised by dragons, you are the right hand man of the Hero. Special Trait: Able to communicate with Dragons, Dragon Burst: Brief transformation into a dragon boosting stats. HP --> 2000 MP --> 500.', response.data)

    def test_knight(self):
        response = self.client.post(url_for('post_desc'), data=','.join(['Knight', 'HP: 2000 MP: 100']))
        self.assertIn(b'Born from nobility, you resent the Hero as you think he stole your true role as the Hero. Special Trait: Super armor on heavy attacks.', response.data)

    def test_healer(self):
        response = self.client.post(url_for('post_desc'), data=','.join(['Healer', 'HP: 600 MP: 1000']))
        self.assertIn(b'Caring and Supportive, you support the team of the Hero with healing and stat boosts. Special Trait: Any allies in a 10 meter radius of you recivies regeneration of 3 percent health per second. Special Move: Guardian Touch: All allies have their stats boosted by 50%.', response.data)

    def test_demon_king(self):
        response = self.client.post(url_for('post_desc'), data=','.join(['Demon King', 'HP: 10,000 MP: 5000']))
        self.assertIn(b'Born from Malice and Evil, your task is to kill the Hero and every other human you see. Special Trait: You cannot be harmed at all unless you are struck by excalibur, in which case you take twice the damage.', response.data)

    def test_royal_jester(self):
        response = self.client.post(url_for('post_desc'), data=','.join(['Royal Jester', 'HP: 100 MP: 1']))
        self.assertIn(b'You have no special role, your job is simply to ammuse the royal king and thus you were exiled from the castle and you joined the party of the Hero. Special Move: Laugh of the Jester, if you make your enemies laugh they turn to stone.', response.data)

    def test_thief(self):
        response = self.client.post(url_for('post_desc'), data=','.join(['Thief', 'HP: 800 MP: 250']))
        self.assertIn(b'Quick and nimble, your job is to steal from the caravan of the Hero. No special traits.', response.data)

    def test_assassin(self):
        response = self.client.post(url_for('post_desc'), data=','.join(['Assassin', 'HP: 1000 MP: 300']))
        self.assertIn(b'Silent and deadly, your role is to assassinate the royal king and other key figures you are employed to elimate. Special Trait 1: Invisibility, grants you to not be seen for a brief period of time. Special Trait 2: Slient footsteps.', response.data)

    def test_mage(self):
        response = self.client.post(url_for('post_desc'), data=','.join(['Mage', 'HP: 300 MP: 3000']))
        self.assertIn(b'A strong intellect but a frail body, you have mastered the various disciplines of magic. Special Move: Magic Burst, expend all MP in an Area Of Effect Attack, attack power scales with remaining MP i.e. 100% will give more damage than 50% MP.', response.data)

    def test_metal_slime(self):
        response = self.client.post(url_for('post_desc'), data=','.join(['Metal Slime', 'HP: 5000 MP: 0']))
        self.assertIn(b'UNLUCKY, your role is simply to provide the Hero and his party with bonus EXP that is if they can hit you! Special Traits: 80,000 EXP, extremely high evasion.', response.data)
