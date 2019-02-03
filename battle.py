"""This is a test battle calculator."""

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
    return attacker[attack_type], defender['attack_type']

def battle(attacker, defender, move, **modifiers):
    """Run a battle."""
    level = attacker['level']
    power = move['power']
    a_stat, d_stat = get_stat(attacker, defender, move)
    modifier = get_modifiers(attacker, defender, move, modifiers)
    damage = damage(level, power, a_stat, d_stat, modifier)
    return damage
