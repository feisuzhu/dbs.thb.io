# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
import graphene as gh

# -- own --
from game.schema import GameQuery
from page.schema import PageQuery

# -- code --
Query = type('Query', (
    GameQuery,
    PageQuery
), {})

schema = gh.Schema(query=Query)
