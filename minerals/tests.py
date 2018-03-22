from django.test import Client, TestCase

import load_from_json
from minerals.models import Mineral


class MineralTestCase(TestCase):
    def setUp(self):
        load_from_json.load_json_setup()
        load_from_json.load_json_to_db()
        self.c = Client()

    def test_database_creation(self):
        minerals = Mineral.objects.all()
        self.assertEqual(len(minerals), 874)
        first_mineral = minerals.first()
        self.assertEqual(first_mineral.id, 1)

    def test_welcome_page(self):
        resp = self.c.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_list_return(self):
        resp = self.c.get('/minerals/')
        self.assertEqual(len(resp.context.get('minerals')), 874)
        self.assertEqual(resp.status_code, 200)

    def test_detail_return(self):
        resp = self.c.get('/minerals/1/')
        self.assertIsNotNone(resp.context.get('mineral'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context.get('mineral').get('name'), 'Abelsonite')

    def test_random_detail_return(self):
        mineral_ids = set()
        # Run the random mineral page 20 times, as it's unlikely that 20 random
        # integers from a pool of 850 will all be the same
        for _ in range(20):
            resp = self.c.get('/minerals/random/')
            mineral_ids.add(resp.context.get('mineral').get('id'))
        self.assertGreater(len(mineral_ids), 1)
