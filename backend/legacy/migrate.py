from pathlib import Path
import sys
sys.path.insert(0, str(Path('..').resolve()))

import yaml
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbs.settings")
django.setup()

from game import models


models.Trait.objects.all().delete()
models.Episode.objects.all().delete()
models.Spellcard.objects.all().delete()
models.Character.objects.all().delete()
models.Build.objects.all().delete()
models.Type.objects.all().delete()
models.Illustrator.objects.all().delete()

# attributes
attrs = yaml.load(open('data/attributes.yaml').read(), Loader=yaml.FullLoader)
models.Trait.objects.all().delete()
for k, v in attrs.items():
    models.Trait.objects.create(name=k.strip(), description=v.strip(), bgcolor='#66ccff')


# episodes
episodes = yaml.load(open('data/episodes.yaml').read(), Loader=yaml.FullLoader)
models.Episode.objects.all().delete()
for ep in episodes:
    models.Episode.objects.create(
        title=ep['title'].strip(),
        description=ep['desc'].strip(),
        subtitle=ep['meta'].strip(),
        image=f'episode/{ep["id"]}.jpg',
        sort=0,
    )


# characters
characters = yaml.load(open('data/characters.yaml').read(), Loader=yaml.FullLoader)

for ch in characters:
    print(ch['name'])
    build = models.Build.objects.create(
        sku=ch['id'].strip(),
        name=ch['name'].strip(),
        intro=ch['meta'].strip(),
        image=f'build/{ch["id"]}.jpg',
        sort=0,
    )

    for chc in ch['cards']:
        print(ch['name'], chc['sku'])
        ill, cr = models.Illustrator.objects.get_or_create(name=chc['illustrator'].strip())
        character = build.characters.create(
            sku=chc['sku'].strip(),
            title=chc['title'].strip(),
            build=build,
            sort=0,
        )
        character.versions.create(
            version='经典',
            rarity=chc['rarity'].strip(),
            line=chc['line'].strip(),
            image=f'card/{chc["sku"]}.jpg',
            illustrator=ill,
        )
        for sk in chc['skills']:
            character.skills.create(
                type=sk['type'].strip(),
                name=sk['name'].strip(),
                description=sk['desc'].strip(),
                sort=0,
            )

    build.save()


# spellcards
import glob

files = glob.glob('data/cards/*.yaml')
models.Spellcard.objects.all().delete()
for f in files:
    cards = yaml.load(open(f).read(), Loader=yaml.FullLoader)
    basename = f.split('.')[0]
    _, *_, sku = basename.split('-')
    print(f, sku)
    for c in cards:
        print(c)
        faq = '\n'.join([i['answer'] for i in c['faq']])
        sc = models.Spellcard.objects.filter(sku=c['sku']).first()
        if not sc:
            sc = models.Spellcard.objects.create(
                sku=c['sku'].strip(),
                build=models.Build.objects.get(sku=sku),
                title=c.get('title', 'MISSING!').strip(),
                effect=c['effect'].strip(),
                type=models.Type.objects.get_or_create(name=c['type'].strip())[0],
                gorgeousness=c['gorgeousness'] if isinstance(c['gorgeousness'], int) else 0,
                cost=0 if not isinstance(c['cost'], int) else c['cost'],
                intensity=c['intensity'] if isinstance(c['intensity'], int) else 0,
                basic_constraint=c.get('basic', 'SUPPORT'),
                faq=faq.strip(),
                sort=0,
            )

            for nn in c.get('attributes', []):
                if nn.startswith('五行'):
                    for a in '金木水火土':
                        if a in nn:
                            sc.traits.add(models.Trait.objects.get(name=f'五行/{a}'))
                else:
                    import re
                    for n in re.split('[、， ,]', nn):
                        sc.traits.add(models.Trait.objects.get_or_create(name=n.strip())[0])

            if c['cost'] == 'LSC':
                sc.traits.add(models.Trait.objects.get_or_create(name='终符')[0])
            elif c['cost'] in ('NULL', 'nul'):
                sc.traits.add(models.Trait.objects.get_or_create(name='NULLITY')[0])
            elif not c['cost'] or c['cost'] == 0 or int(c['cost']) == 0:
                pass
            elif not isinstance(c['cost'], int):
                raise Exception(f'Invalid cost: {c["cost"]} {type(c["cost"])}')

            for v in c.get('special', []):
                sc.extended_constraints.create(
                    type='额外限制',
                    effect=v.strip(),
                )

        sc.versions.create(
            version=c['version'] or '经典',
            rarity=c['rarity'],
            line=c.get('line', '-').strip(),
            episode=None,
            illustrator=models.Illustrator.objects.get_or_create(name=c['illustrator'].strip())[0],
            image=f'card/{c["sku"]}.jpg',
        )
