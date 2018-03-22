import json
import os


# To access the model, we need to tell django where the project settings are
def load_json_setup():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mineral_catalog.settings")

    # And we need to start up the apps
    from django.core.wsgi import get_wsgi_application
    get_wsgi_application()


def load_json_to_db():
    # Then we can finally import the model from the app
    from minerals.models import Mineral

    # Load minerals json as dictionary
    minerals = json.load(open('./minerals/fixtures/minerals.json'))
    for mineral in minerals:
        # Adds mineral to database, adding an empty string if the key isn't
        # in the particular mineral dictionary
        Mineral(
            name=mineral.get('name', ''),
            image_filename=mineral.get('image filename', ''),
            image_caption=mineral.get('image caption', ''),
            group=mineral.get('group', ''),
            category=mineral.get('category', ''),
            formula=mineral.get('formula', ''),
            strunz_classification=mineral.get('strunz classification', ''),
            color=mineral.get('color', ''),
            crystal_system=mineral.get('crystal system', ''),
            unit_cell=mineral.get('unit cell', ''),
            crystal_symmetry=mineral.get('crystal symmetry', ''),
            cleavage=mineral.get('cleavage', ''),
            mohs_scale_hardness=mineral.get('mohs scale hardness', ''),
            luster=mineral.get('luster', ''),
            streak=mineral.get('streak', ''),
            diaphaneity=mineral.get('diaphaneity', ''),
            optical_properties=mineral.get('optical properties', ''),
            refractive_index=mineral.get('refractive index', ''),
            crystal_habit=mineral.get('crystal habit', ''),
            specific_gravity=mineral.get('specific gravity', ''),
        ).save()

if __name__ == "__main__":
    load_json_setup()
    load_json_to_db()
