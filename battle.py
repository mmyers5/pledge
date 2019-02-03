"""This is a test battle calculator.
Presumably attacker, defender, and move are dicts as follows:

    attacker = {
        'name': 'Slowpoke',
        'attack': 10,
        'defense': 10,
        'special_attack': 10,
        'special_defense': 10,
        'speed': 1,
        'level': 10
    }
    
    move = {
        'name': Tackle,
        'power': 35,
        'attack_type': 'physical',
        'type': 'Normal'
    }

"""

def damage(level, power, a_stat, d_stat, modifier):
    # See https://bulbapedia.bulbagarden.net/wiki/Damage
    return (
        (
            (
                (
                    ( (2 * level) / 5)
                    + 2
                )
                * power
                * (a_stat/d_stat)
            )
            / 50
        )
        + 2
    ) * modifier


def resolve_weather(*args):
    pass

def resolve_critical(*args):
    pass

def resolve_random(*args):
    pass

def resolve_stab(*args):
    pass

def resolve_etc(*args):
    pass

def get_modifiers(attacker, defender, move, modifiers):
    # will be complicated, haven't decided how to implement
    modifier = 0
    modifier_funcs = {
        'weather': resolve_weather,
        'critical': resolve_critical,
        'random': resolve_random,
        'stab': resolve_stab,
        'etc': resolve_etc
    }
    for mod in modifiers:
        modifier += modifier_funcs[mod](attacker, defender, move)
    return modifier

def get_stat(attacker, defender, move):
    """Given a move, get relevant stats from pokemon."""
    attack_type = move['attack_type']
    if attack_type == 'physical':
        return attacker['attack'], defender['defense']
    elif attack_type == 'special':
        return attacker['special_attack'], defender['special_defense']
    else:
        raise Exception("Did not recognize attack type.")

def battle(attacker, defender, move, **modifiers):
    """Run a battle."""
    level = attacker['level']
    power = move['power']
    a_stat, d_stat = get_stat(attacker, defender, move)
    modifier = get_modifiers(attacker, defender, move, modifiers)
    damage = damage(level, power, a_stat, d_stat, modifier)
    return damage
