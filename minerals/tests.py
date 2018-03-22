from django.test import TestCase

import load_from_json
from minerals.models import Mineral


class MineralTestCase(TestCase):
    def setUp(self):
        load_from_json.load_json_setup()
        load_from_json.load_json_to_db()

    def test_database_creation(self):
        minerals = Mineral.objects.all()
        self.assertEqual(len(minerals), 874)
        first_mineral = minerals.first()
        self.assertEqual(first_mineral.id, 1)
