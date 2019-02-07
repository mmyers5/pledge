def table_6():
    return (
r"""
<table style="border-collapse:separate;border-spacing:10px;" align="center">
    <tr>
        <td>
            {table_1}
        </td>
        <td>
            {table_2}
        </td>
    </tr>
    <tr>
        <td>
            {table_3}
        </td>
        <td>
            {table_4}
        </td>
    </tr>
    <tr>
        <td>
            {table_5}
        </td>
        <td>
            {table_6}
        </td>
    </tr>
</table>
"""
    )

def table_5():
    return (
r"""
<table style="border-collapse:separate;border-spacing:10px;" align="center">
    <tr>
        <td>
            {table_1}
        </td>
        <td>
            {table_2}
        </td>
    </tr>
    <tr>
        <td>
            {table_3}
        </td>
        <td>
            {table_4}
        </td>
    </tr>
    <tr>
        <td>
            {table_5}
        </td>
    </tr>
</table>
"""
    )

def table_4():
    return (
r"""
<table style="border-collapse:separate;border-spacing:10px;" align="center">
    <tr>
        <td>
            {table_1}
        </td>
        <td>
            {table_2}
        </td>
    </tr>
    <tr>
        <td>
            {table_3}
        </td>
        <td>
            {table_4}
        </td>
    </tr>
</table>
"""
    )

def table_3():
    return (
r"""
<table style="border-collapse:separate;border-spacing:10px;" align="center">
    <tr>
        <td>
            {table_1}
        </td>
        <td>
            {table_2}
        </td>
    </tr>
    <tr>
        <td>
            {table_3}
        </td>
    </tr>
</table>
"""
    )

def table_2():
    return (
r"""
<table style="border-collapse:separate;border-spacing:10px;" align="center">
    <tr>
        <td>
            {table_1}
        </td>
        <td>
            {table_2}
        </td>
    </tr>
</table>
"""
    )


def table_1():
    return (
r"""
<table style="border-collapse:separate;border-spacing:10px;" align="center">
    <tr>
        <td>
            {table_1}
        </td>
    </tr>
</table>
"""
    )


def pc_table():
    return (
r"""
<table class="pctable">
    <tr>
        <th class="pcname" colspan="2" style="font-size:{pcname_size}px;">
            {nickname} -
            <span style="font-family: Tahoma;font-weight:bold;">{gender}</span>
            <a href="{specie_link}" style="color:#000;">
                - {specie}
            </a>
        </th>
    </tr>
    <tr>
        <td class="pciconbox" rowspan="4">
            <div class="pcicondiv">
                <img style="display:block;position:absolute;max-width:125px;height:auto;max-height:125px; margin-left:0px;" src="{specie_img}">
            </div>
            <div class="pcball" style="{no_ball};">
                <img style="display:block" src="{ball_img}" title="{ball}">
            </div>
            <div class="pcitem" style="{no_item};">
                <img style="display:block" src="{held_item_img}" title="{held_item}">
            </div>
        </td>
        <td class="pccell">{type_print}</td>
    </tr>
    <tr>
        <td class="pccell">{level}</td>
    </tr>
    <tr>
        <td class="pccell">{link}</td>
    </tr>
    <tr>
        <td class="pccell" bgcolor="#ff0000">
            <a href="{ability_link}" style="color:#000;">
                {ability}
            </a>
        </td>
    </tr>
    <tr>
        <td class="pcmove1" style="background-color:{move1_bkg_color};color:#000;">
            <a href="{move1_link}" style="color:{move1_color};">
                {move1}
            </a>
        </td>
        <td class="pcmove2" style="background-color:{move2_bkg_color};color:#000">
            <a href="{move2_link}" style="color:{move2_color};">
                {move2}
            </a>
        </td>
    </tr>
    <tr>
        <td class="pcmove3" style="background-color:{move3_bkg_color};color:#000;">
            <a href="{move3_link}" style="color:{move3_color};">
                {move3}
            </a>
        </td>
        <td class="pcmove4" style="background-color:{move4_bkg_color};color:#000">
            <a href="{move4_link}" style="color:{move4_color};">
                {move4}
            </a>
        </td>
    </tr>
    <tr>
        <td colspan="2"><div class="pcdesc">{description}</div></td>
    </tr>
</table>
"""
    )


def preamble():
    return (
r"""
<style type="text/css">
    table.pctable {border-collapse: separate; border-radius:12px; -moz-border-radius:12px;width:262px; text-align:center; background-color:#bbb;border-spacing:6px;table-layout:fixed;}
    .pctable td, .pctable th {font-size:12px; height:25px;background-color:#fff;border-radius:12px; -moz-border-radius:12px;border-collapse: separate; color:#000;}
    .pcname {overflow:hidden;word-break:normal;text-align:center;letter-spacing:2px; !important;height:25px!important;font-weight:bold;}
    .pciconbox {width:100px !important;border-radius:50% !important; height:20px !important;}
    .pcicondiv {display: flex; align-items: center; justify-content: center;}
    .pciconlink {position:absolute;display:block;}
    .pcball {position:absolute;margin-top:35px;margin-left:7px;background-color:#fff;border: solid #bbb 3px;border-radius:50%; display: flex; align-items: center; justify-content: center;}
    .pcitem {position:absolute;margin-top:35px;margin-left:82px;background-color:#fff;border: solid #bbb 3px;border-radius:50%; display: flex; align-items: center; justify-content: center;}
    .pcmove1 {border-bottom-left-radius:8px !important; border-bottom-right-radius:0px !important;border-top-left-radius:50px!important;border-top-right-radius:8px!important;}
    .pcmove3 {border-bottom-left-radius:50px !important; border-bottom-right-radius:8px !important;border-top-left-radius:8px!important;border-top-right-radius:0px!important;}
    .pcmove4 {border-bottom-left-radius:8px !important; border-bottom-right-radius:50px !important;border-top-left-radius:0px!important;border-top-right-radius:8px!important;}
    .pcmove2 {border-bottom-left-radius:0px !important; border-bottom-right-radius:8px !important;border-top-left-radius:8px!important;border-top-right-radius:50px!important;}
    .pctable .pcdesc {min-height:114px;max-height:114px!important;padding:5px;overflow:hidden; }
    .pccell {line-height:20px;}
    h1 {font-size:18; font-weight:bold; letter-spacing:5px;}
</style>
"""
    )

def genders():
    return [
        '⚲',
        '♀',
        '♂'
    ]

def move_types():
    return {
        'Type': '#fff',
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

def balls():
    return {
        'No Ball': '',
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

def held_items():
    return {
        'No Item': '',
        'Amulet Coin': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/amulet_coin.png',
        'Assault Vest': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Assault_Vest_Sprite.png',
        'Big Root': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Healing_Items/energy_root.png',
        'Bright Powder': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/bright_powder.png',
        'Bug Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/bug_gem.png',
        'Bug Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/bug_memory.png',
        'Charcoal': 'http://cdn.bulbagarden.net/upload/b/b5/Bag_Charcoal_Sprite.png',
        'Choice Band': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/choice_band.png',
        'Choice Scarf': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/choice_scarf.png',
        'Choice Specs': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/choice_specs.png',
        'Cleanse Tag': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/cleanse_tag.png',
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
        'Focus Band': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/focus_band.png',
        'Focus Sash': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/focus_sash.png',
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
        "King's Rock": 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/kings_rock.png',
        'Leftovers': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/LeftoversSprite.png',
        'Life Orb': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Life_Orb_Sprite.png',
        'Light Ball': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Light_Ball_Sprite.png',
        'Mystic Water': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/mystic_water.png',
        'Normal Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/normal_gem.png',
        'Poison Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/poison_gem.png',
        'Poison Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/poison_memory.png',
        'Protective Pads': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Protective_Pads_Sprite.png',
        'Psychic Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/psychic_gem.png',
        'Psychic Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/psychic_memory.png',
        'Quick Claw': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/quick_claw.png',
        'Rock Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/rock_gem.png',
        'Rock Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/rock_memory.png',
        'Rocky Helmet': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/rocky_helmet.png',
        'Rose Incense': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Dream_Rose_Incense_Sprite.png',
        'Shell Bell': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/shell_bell.png',
        'Silk Scarf': 'https://cdn.bulbagarden.net/upload/2/2c/Bag_Silk_Scarf_Sprite.png',
        'Smoke Ball': 'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Held_Items/smoke_ball.png',
        'Soothe Bell': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/soothe_bell.png',
        'Steel Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/steel_gem.png',
        'Steel Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/steel_memory.png',
        'Thick Club': 'https://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/Thick_Club_Sprite.png',
        'Water Gem': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/water_gem.png',
        'Water Memory': 'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Held_Items/water_memory.png'
    }
