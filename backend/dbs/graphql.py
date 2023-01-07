# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
import graphene as gh
import graphql

# -- own --
from game.schema import GameQuery
from page.schema import PageQuery

# -- code --
Query = type('Query', (
    GameQuery,
    PageQuery
), {})

schema = gh.Schema(query=Query)
