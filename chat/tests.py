from django.test import TestCase

from .models import ChannelMessage, UserChannel, Channel
from django.contrib.auth import get_user_model

User = get_user_model()

class ChannelTestCase(TestCase):
    def setUp(self):
        self.usuario_a = User.objects.create(username= 'luisa', password= 'hola123')
        self.usuario_b = User.objects.create(username= 'samuel', password= 'hola456')
        self.usuario_c = User.objects.create(username= 'miguel', password= 'hola789')

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 3)