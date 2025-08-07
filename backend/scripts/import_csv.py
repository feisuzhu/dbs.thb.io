import os, django
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbs.settings")
django.setup()

from django.db import IntegrityError, transaction

BASE = Path(__file__).parent


from game import models
import csv

reader = csv.DictReader(open(BASE / 'EP03.csv'))


with transaction.atomic():
    for ent in reader:
        print(ent)
        build, _ = models.Build.objects.get_or_create(sku=ent['sku'].split('-')[0])
        ty, _ = models.Type.objects.get_or_create(name=ent['type1'])

        print(ent['sku'])

        sc = models.Spellcard.objects.create(
            sku=ent['sku'],
            build=build,
            type=ty,
            title=ent['title'],
            gorgeousness=ent['gor1'],
            cost=ent['cost'],
            # lsc=ent['lsc'],
            lsc=0,
            effect=ent['effect'],
            intensity=ent['intensity'],
            basic_constraint=ent['con'],
        )

        ill, _ = models.Illustrator.objects.get_or_create(name=ent['ill1'])

        ver = sc.versions.create(
            version="经典",
            rarity=ent['r'],
            line=ent['line'],
            illustrator=ill,
            image='card/' + ent['sku'] + '.png',
        )

        for t in ent['feat'].split(','):
            t = t.strip()
            if not t:
                continue
            tr, _ = models.Trait.objects.get_or_create(name=t)
            sc.traits.add(tr)

        for t in ent['pack'].split(','):
            t = t.strip()
            if not t:
                continue
            ep, _ = models.Episode.objects.get_or_create(sku=t)
            ver.episodes.add(ep)

        sc.save()
