from django.contrib.auth.models import User
from django.test import TestCase

from tastytaps.taps.models import Taproom


class TestTaproomUser(TestCase):

    def setUp(self):
        credentials = {
            'username': 'tester',
            'password': 'password',
        }

        self.user = User.objects.create(**credentials)
        self.taproom = Taproom.objects.create(name="Tasty's Taproom",
                                              num_taps=12)
        self.taproom.users.add(self.user)

    def test_relationship(self):
        assert list(self.taproom.users.all()) == [self.user]
        assert list(self.user.taprooms.all()) == [self.taproom]
