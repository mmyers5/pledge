def parse_specie(specie, params):
    params['specie'] = specie
    params['specie_link'] = (
        'https://bulbapedia.bulbagarden.net/wiki/{}_(Pok%C3%A9mon)'.format(
            specie.capitalize()
        )
    )
    params['icon_img'] = (
        'https://play.pokemonshowdown.com/sprites/xyani/{}.gif'.format(
            specie.lower()
        )
    )
    return params

def parse_ball(ball, params):
    item_list = {
        'Pokeball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/pokeball.png',
        'Cherish Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/cherishball.png',
        'Dive Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/diveball.png',
        'Dusk Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/duskball.png',
        'Fast Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/fastball.png',
        'Friend Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/friendball.png',
        'Great Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/greatball.png',
        'Heal Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/healball.png',
        'Heavy Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/heavyball.png',
        'Level Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/levelball.png',
        'Love Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/loveball.png',
        'Lure Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/lureball.png',
        'Luxury Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/luxuryball.png',
        'Moon Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/moonball.png',
        'Nest Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/nestball.png',
        'Net Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/netball.png',
        'Premier Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/premierball.png',
        'Quick Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/quickball.png',
        'Repeat Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/repeatball.png',
        'Timer Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/timerball.png',
        'Ultra Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/ultraball.png'
    }
    params['ball'] = ball
    params['ball_img'] = item_list[ball]
    return params

def parse_item(item, params):
    if item == 'No Item':
        params['no_item'] = 'display:none;'
        return params

    item_list = {
        'Amulet Coin': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/amulet_coin.png',
        'Assault Vest': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Assault_Vest_Sprite.png',
        'Big Root': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Healing_Items/energy_root.png',
        'Bright Powder': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/bright_powder.png',
        'Bug Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/bug_gem.png',
        'Bug Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/bug_memory.png',
        'Charcoal': 'http://cdn.bulbagarden.net/upload/b/b5/Bag_Charcoal_Sprite.png',
        'Dark Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/dark_gem.png',
        'Dark Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/dark_memory.png',
        'Dragon Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/dragon_gem.png',
        'Dragon Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/dragon_memory.png',
        'Electric Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/electric_gem.png',
        'Electric Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/electric_memory.png',
        'Eviolite': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/eviolite.png',
        'Fairy Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fairy_gem.png',
        'Fairy Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fairy_memory.png',
        'Fighting Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fighting_gem.png',
        'Fighting Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fighting_memory.png',
        'Fire Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fire_gem.png',
        'Fire Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fire_memory.png',
        'Flying Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/flying_gem.png',
        'Flying Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/flying_memory.png',
        'Ghost Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ghost_gem.png',
        'Ghost Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ghost_memory.png',
        'Grass Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/grass_gem.png',
        'Grass Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/grass_memory.png',
        'Ground Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ground_gem.png',
        'Ground Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ground_memory.png',
        'Heat Rock': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/heat_rock.png',
        'Ice Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ice_gem.png',
        'Ice Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ice_memory.png',
        'Icy Rock': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/icy_rock.png',
        'Leftovers': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/LeftoversSprite.png',
        'Life Orb': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Life_Orb_Sprite.png',
        'Light Ball': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Light_Ball_Sprite.png',
        'Normal Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/normal_gem.png',
        'Poison Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/poison_gem.png',
        'Poison Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/poison_memory.png',
        'Protective Pads': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Protective_Pads_Sprite.png',
        'Psychic Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/psychic_gem.png',
        'Psychic Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/psychic_memory.png',
        'Rock Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/rock_gem.png',
        'Rock Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/rock_memory.png',
        'Rocky Helmet': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/rocky_helmet.png',
        'Rose Incense': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Dream_Rose_Incense_Sprite.png',
        'Silk Scarf': 'https://cdn.bulbagarden.net/upload/2/2c/Bag_Silk_Scarf_Sprite.png',
        'Smoke Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/smoke_ball.png',
        'Steel Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/steel_gem.png',
        'Steel Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/steel_memory.png',
        'Thick Club': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Thick_Club_Sprite.png',
        'Water Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/water_gem.png',
        'Water Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/water_memory.png'
    }
    params['item'] = item
    params['item_img'] = item_list[item]
    params['no_item'] = ''
    return params

def parse_type(type, params):
    if '/' in type:
        types = [':{}:'.format(i) for i in type.lower().strip().split('/')]
        type = '/'.join(types)
    else:
        type = ':{}:'.format(type.lower().strip())
    params['type'] = type
    return params

def parse_ability(ability, params):
    params['ability'] = ability
    params['ability_link'] = (
        'https://bulbapedia.bulbagarden.net/wiki/{}_(Ability)'.format(
            ability.title()
        )
    )
    return params

def parse_moves(move_entry, move, move_type, params):
    params[move_entry] = move
    params['{}_link'.format(move)] = (
        'https://bulbapedia.bulbagarden.net/wiki/{}_(move)'.format(
            move.title()
        )
    )
    params['{}_color'.format(move_entry)] = '#fff'

    move_types = {
        'N/A': '#fff',
        'Bug': '#A8B820',
        'Dark': '#705848',
        'Dragon': '#7038F8',
        'Electric': '#F8D030',
        'Fairy': '#EE99AC',
        'Fighting': '#C03028',
        'Fire': '#F08030',
        'Flying': '#A890F0',
        'Ghost': '#705898',
        'Grass': '#78C850',
        'Ground': '#E0C068',
        'Ice': '#98D8D8',
        'Normal': '#A8A878',
        'Poison': '#A040A0',
        'Psychic': '#F85888',
        'Rock': '#B8A038',
        'Steel': '#B8B8D0',
        'Water': '#6890F0'
    }
    params['{}_bkg_color'.format(move_entry)] = move_types[move_type]
    return params

def parse_args(form, params):
    changes = [i for i in form]
    if 'specie' in changes:
        params = parse_specie(form['specie'], params)
    if 'ball' in changes:
        params = parse_ball(form['ball'], params)
    if 'item' in changes:
        params = parse_item(form['item'], params)
    if 'type' in changes:
        params = parse_type(form['type'], params)

    if 'level' in changes:
        params['level'] = form['level']
    if 'link' in changes:
        params['link'] = form['link']

    if 'ability' in changes:
        params = parse_ability(form['ability'], params)
    for move in ['move1', 'move2', 'move3', 'move4']:
        if move in changes:
            params = parse_moves(
                move,
                form[move],
                form['{}_bkg_color'.format(move)],
                params
            )

    if 'description' in changes:
        params['description'] = form['description']

    if 'girlboy' in changes:
        params['girlboy'] = form['girlboy']
    if 'nickname' in changes:
        params['nickname'] = form['nickname']

    return params

def defaults():
    return {
        'nickname': '???',
        'girlboy': '♀/♂',
        'specie_link': (
            'https://bulbapedia.bulbagarden.net/wiki/_(Pok%C3%A9mon)'
        ),
        'specie': '???',
        'icon_img': (
            'https://play.pokemonshowdown.com/sprites/xyani/pokemon.gif'
        ),
        'ball_img': (
            'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/pokeball.png'
        ),
        'ball': 'Pokéball',
        'item_img': (
            'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/lucky_egg.png'
        ),
        'item': 'Lucky Egg',
        'type': 'Type',
        'level': 'Level',
        'link': 'Link',
        'ability_link': (
            'https://bulbapedia.bulbagarden.net/wiki/_(Ability)'
        ),
        'ability': 'Ability',
        'move1_link': 'https://bulbapedia.bulbagarden.net/wiki/_(move)',
        'move1_color': '#000',
        'move1_bkg_color': '#fff',
        'move1': '---',
        'move2_link': 'https://bulbapedia.bulbagarden.net/wiki/_(move)',
        'move2_color': '#000',
        'move2_bkg_color': '#fff',
        'move2': '---',
        'move3_link': 'https://bulbapedia.bulbagarden.net/wiki/_(move)',
        'move3_color': '#000',
        'move3_bkg_color': '#fff',
        'move3': '---',
        'move4_link': 'https://bulbapedia.bulbagarden.net/wiki/_(move)',
        'move4_color': '#000',
        'move4_bkg_color': '#fff',
        'move4': '---',
        'description': 'Description',
        'balls': balls(),
        'items': items(),
        'no_item': 'display:none;',
        'move_types': move_types()
    }

def items():
    return {
        'No Item': '',
        'Amulet Coin': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/amulet_coin.png',
        'Assault Vest': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Assault_Vest_Sprite.png',
        'Big Root': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Healing_Items/energy_root.png',
        'Bright Powder': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/bright_powder.png',
        'Bug Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/bug_gem.png',
        'Bug Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/bug_memory.png',
        'Charcoal': 'http://cdn.bulbagarden.net/upload/b/b5/Bag_Charcoal_Sprite.png',
        'Dark Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/dark_gem.png',
        'Dark Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/dark_memory.png',
        'Dragon Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/dragon_gem.png',
        'Dragon Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/dragon_memory.png',
        'Electric Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/electric_gem.png',
        'Electric Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/electric_memory.png',
        'Eviolite': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/eviolite.png',
        'Fairy Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fairy_gem.png',
        'Fairy Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fairy_memory.png',
        'Fighting Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fighting_gem.png',
        'Fighting Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fighting_memory.png',
        'Fire Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fire_gem.png',
        'Fire Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/fire_memory.png',
        'Flying Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/flying_gem.png',
        'Flying Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/flying_memory.png',
        'Ghost Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ghost_gem.png',
        'Ghost Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ghost_memory.png',
        'Grass Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/grass_gem.png',
        'Grass Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/grass_memory.png',
        'Ground Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ground_gem.png',
        'Ground Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ground_memory.png',
        'Heat Rock': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/heat_rock.png',
        'Ice Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ice_gem.png',
        'Ice Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/ice_memory.png',
        'Icy Rock': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/icy_rock.png',
        'Leftovers': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/LeftoversSprite.png',
        'Life Orb': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Life_Orb_Sprite.png',
        'Light Ball': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Light_Ball_Sprite.png',
        'Normal Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/normal_gem.png',
        'Poison Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/poison_gem.png',
        'Poison Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/poison_memory.png',
        'Protective Pads': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Protective_Pads_Sprite.png',
        'Psychic Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/psychic_gem.png',
        'Psychic Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/psychic_memory.png',
        'Rock Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/rock_gem.png',
        'Rock Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/rock_memory.png',
        'Rocky Helmet': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/rocky_helmet.png',
        'Rose Incense': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Dream_Rose_Incense_Sprite.png',
        'Silk Scarf': 'https://cdn.bulbagarden.net/upload/2/2c/Bag_Silk_Scarf_Sprite.png',
        'Smoke Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/smoke_ball.png',
        'Steel Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/steel_gem.png',
        'Steel Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/steel_memory.png',
        'Thick Club': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Thick_Club_Sprite.png',
        'Water Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/water_gem.png',
        'Water Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/water_memory.png'
    }

def balls():
    return {
        'Pokeball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/pokeball.png',
        'Cherish Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/cherishball.png',
        'Dive Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/diveball.png',
        'Dusk Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/duskball.png',
        'Fast Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/fastball.png',
        'Friend Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/friendball.png',
        'Great Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/greatball.png',
        'Heal Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/healball.png',
        'Heavy Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/heavyball.png',
        'Level Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/levelball.png',
        'Love Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/loveball.png',
        'Lure Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/lureball.png',
        'Luxury Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/luxuryball.png',
        'Moon Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/moonball.png',
        'Nest Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/nestball.png',
        'Net Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/netball.png',
        'Premier Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/premierball.png',
        'Quick Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/quickball.png',
        'Repeat Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/repeatball.png',
        'Timer Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/timerball.png',
        'Ultra Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/ultraball.png'
    }

def move_types():
    return {
        'N/A': '#fff',
        'Bug': '#A8B820',
        'Dark': '#705848',
        'Dragon': '#7038F8',
        'Electric': '#F8D030',
        'Fairy': '#EE99AC',
        'Fighting': '#C03028',
        'Fire': '#F08030',
        'Flying': '#A890F0',
        'Ghost': '#705898',
        'Grass': '#78C850',
        'Ground': '#E0C068',
        'Ice': '#98D8D8',
        'Normal': '#A8A878',
        'Poison': '#A040A0',
        'Psychic': '#F85888',
        'Rock': '#B8A038',
        'Steel': '#B8B8D0',
        'Water': '#6890F0'
}
