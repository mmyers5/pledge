from pc_jenny_templates import genders, move_types, balls, held_items
from pc_jenny_templates import preamble, pc_table
import pc_jenny_templates
import re

def create_pcs(pcs):
    n_pcs = len(pcs)
    tables = {}
    for t in range(n_pcs):
        t_name = 'table_{}'.format(t+1)
        print(pcs[t].__dict__)
        tables[t_name] = pc_table().format(**pcs[t].__dict__)
        print(tables)
    pc_tables = getattr(pc_jenny_templates, t_name)().format(**tables)
    return '\n'.join([preamble(), pc_tables])

def parse_multiple(pc, form):
    n = len(pc)
    for i in range(n):
        suffix = '_{}'.format(i)
        i_form = { 
            ''.join(i.split(suffix)[:-1]): form[i] for i in form if i.endswith(suffix)
        }
        print(i_form)
        pc[i].parse_args(i_form)
        print(pc[i].specie)
    return pc


class PCPokemon:
    def __init__(self):
        self.set_defaults()

    def set_defaults(self):
        self.pcname_size = '16'
        self.specie = ''
        self.nickname = ''
        self.gender = '⚲',
        self.specie_img = (
            'https://play.pokemonshowdown.com/sprites/xyani/pokemon.gif'
        )
        self.specie_link = (
            'https://bulbapedia.bulbagarden.net/wiki/_(Pok%C3%A9mon)'
        )
        self.type = ''
        self.level = ''
        self.link = ''
        self.ability = ''
        self.ability_link = 'https://bulbapedia.bulbagarden.net/wiki/_(Ability)'
        self.ball = 'Pokéball'
        self.ball_img = (
            'http://pokemonpledge.b1.jcink.com/uploads/pokemonpledge/Shop_Icons/Pokeballs/pokeball.png'
        )
        self.held_item = 'Lucky Egg'
        self.held_item_img = (
            'http://files.jcink.net/uploads/pokemonpledge/Shop_Icons/Unbuyables/lucky_egg.png'
        )
        self.move1 = ''
        self.move2 = ''
        self.move3 = ''
        self.move4 = ''
        self.move1_link = 'https://bulbapedia.bulbagarden.net/wiki/_(move)'
        self.move2_link = 'https://bulbapedia.bulbagarden.net/wiki/_(move)'
        self.move3_link = 'https://bulbapedia.bulbagarden.net/wiki/_(move)'
        self.move4_link = 'https://bulbapedia.bulbagarden.net/wiki/_(move)'
        self.move1_color = '#000'
        self.move2_color = '#000'
        self.move3_color = '#000'
        self.move4_color = '#000'
        self.move1_bkg_color = '#fff'
        self.move2_bkg_color = '#fff'
        self.move3_bkg_color = '#fff'
        self.move4_bkg_color = '#fff'
        self.description = ''

        self.shiny = "False"
        self.no_item = 'display:none;'
        self.no_ball = 'display:none;'
        self.type_print = ''

    def set_specie(self, specie):
        self.specie = specie.strip('-f').strip('-m').capitalize()
        self.specie_link = (
            'https://bulbapedia.bulbagarden.net/wiki/{}_(Pok%C3%A9mon)'.format(
                self.specie
            )
        )
        if self.shiny == "True":
            self.specie_img = (
                'https://play.pokemonshowdown.com/sprites/xyani-shiny/{}.gif'.format(
                    specie.lower()
                )
            )
        elif self.shiny == "False":
            self.specie_img = (
                'https://play.pokemonshowdown.com/sprites/xyani/{}.gif'.format(
                    specie.lower()
                )
            )

    def set_ball(self, ball):
        self.ball = ball
        self.ball_img = balls()[ball]

    def set_held_item(self, held_item):
        self.held_item = held_item
        self.held_item_img = held_items()[held_item]

    def set_type(self, type):
        if type=='':
            return
        if '/' in type:
            types = [':{}:'.format(i) for i in type.lower().strip().split('/')]
            type_print = ' / '.join(types)
        else:
            type_print = ':{}:'.format(type.lower().strip())
        self.type = type
        self.type_print = type_print

    def set_ability(self, ability):
        self.ability = ability
        self.ability_link = (
            'https://bulbapedia.bulbagarden.net/wiki/{}_(Ability)'.format(
                ability.title()
            )
        )

    def set_move(self, move_entry, move, move_type):
        setattr(self, move_entry, move)
        setattr(
            self, 
            '{}_link'.format(move_entry), 
            'https://bulbapedia.bulbagarden.net/wiki/{}_(move)'.format(
                move.title()
            )
        )
        setattr(
            self,
            '{}_color'.format(move_entry),
            '#fff'
        )
        setattr(
            self,
            '{}_type'.format(move_entry),
            move_type
        )
        setattr(
            self,
            '{}_bkg_color'.format(move_entry),
            move_types()[move_type]
        )

    def parse_args(self, form):
        changes = []
        for i in form:
            try:
                curr_data = getattr(self, i)
            except:
                pass
            else:
                if form[i] != curr_data:
                    changes.append(i)
        if 'shiny' in changes:
            self.shiny = form['shiny']
        if 'gender' in changes:
            self.gender = form['gender']
        if 'ball' in changes:
            self.set_ball(form['ball'])
        if 'held_item' in changes:
            self.set_held_item(form['held_item'])
        if 'specie' in changes:
            self.set_specie(form['specie'])
        if 'nickname' in changes:
            self.nickname = form['nickname']
        if 'type' in changes:
            self.set_type(form['type'])
        if 'pcname_size' in changes:
            if form['pcname_size']=='':
                pass
            else:
                self.pcname_size = form['pcname_size']
        if 'level' in changes:
            self.level = form['level']
        if 'link' in changes:
            self.link = form['link']
        if 'ability' in changes:
            self.set_ability(form['ability'])
        if 'description' in changes:
            self.description = form['description']

        for move_entry in ['move1', 'move2', 'move3', 'move4']:
            if move_entry in changes:
                self.set_move(
                    move_entry,
                    form[move_entry],
                    form['{}_type'.format(move_entry)]
                )
        if self.held_item == 'No Item':
            self.no_item = 'display:none;'
        else:
            self.no_item = ''
        if self.ball == 'No Ball':
            self.no_ball = 'display:none;'
        else:
            self.no_ball = ''

        self.type = re.sub(':+', ':', self.type) 
