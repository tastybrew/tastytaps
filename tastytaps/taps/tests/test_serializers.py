# -*- coding: utf-8 -*-
from django.test import TestCase

from tastytaps.taps.models import Taps
from tastytaps.taps.serializers import TapsSerializer


class TestTapsSerializer(TestCase):
    def setUp(self):
        super(TestTapsSerializer, self).setUp()

        self.data = {
            'name': 'Duchesse de Bourgogne',
            'style': 'Flanders Red Ale',
            'summary': 'A wonderful Flanders Red Ale',
            'brewery_name': 'Brouwerij Verhaeghe',
            'brewery_country': 'Belgium',
            'prices': [
                {'size': 'Glass', 'price': '3.50'},
                {'size': 'Pint', 'price': '5.00'},
            ],
        }

    def serializer(self, data=None):
        return TapsSerializer(data=data or self.data)

    def test_serialize(self):
        serializer = self.serializer()
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

    def test_required_fields(self):
        required_fields = ('name', 'style', 'summary', 'prices')
        for field in required_fields:
            data = self.data.copy()
            del data[field]
            serializer = self.serializer(data)
            self.assertFalse(serializer.is_valid())
            self.assertEqual(serializer.errors,
                             {field: ['This field is required.']})

    def test_name(self):
        del self.data['prices']
        taps = Taps(**self.data)
        serializer = TapsSerializer(instance=taps)
        self.assertEqual(serializer.data['name'], u'Duchesse de Bourgogne')

    def test_price_not_string(self):
        for cast_type in (str, int):
            data = self.data.copy()
            data['prices'] = [
                {'size': 'Glass', 'price': cast_type(3.00)}
            ]
            serializer = self.serializer(data)
            self.assertTrue(serializer.is_valid())
            validated_price = serializer.validated_data['prices'][0]['price']
            self.assertEqual(validated_price, 3.00)

    def test_one_price_invalid(self):
        data = self.data.copy()
        data['prices'].append({'size': 'Growler'})  # Price missing.
        serializer = self.serializer(data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors,
            {'prices': [{}, {}, {'price': ['This field is required.']}]})

    def test_unicode(self):
        data = self.data.copy()
        data['name'] = u'Löwenbräu'
        serializer = self.serializer(data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], data['name'])
