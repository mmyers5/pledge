import re
import time
from flask import Flask, request, render_template, redirect, url_for
from topic import jcinkThread
from egg_maker import EggGenerator, hex_to_rgba
import pc_jenny
import pc_jenny_templates

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = False

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}'.format(
    username='y2kekse',
    password='100%Link',
    hostname='y2kekse.mysql.pythonanywhere-services.com',
    databasename='y2kekse$modlog',
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

IMAGE_DIR = '/images'
BASE_FILE = '/home/y2kekse/images/BaseEgg.png'
LIGHTING_FILE = '/home/y2kekse/images/Base-Eggwith-Shadowand-Highlight.png'

def get_thread_num(url):
    thread_num = re.findall(r'showtopic=(\d+)', url)[0]
    return int(thread_num)

def topic_counter(thread_num):
    url = 'http://pokemonpledge.jcink.net/index.php?showtopic={}'.format(
        thread_num
    )
    thread = jcinkThread(url)
    users = thread.users
    # words per user, posts per user
    wpu, ppu = thread.main()
    return users, wpu, ppu

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main_page.html')
    contents = request.form['thread']
    try:
        thread_num = int(contents)
    except:
        thread_num = get_thread_num(url=contents)
    users, wpu, ppu = topic_counter(thread_num)
    return render_template(
        'showtopic_summary.html',
        users=users,
        post_count=ppu,
        word_count=wpu,
        total_post_count=sum(ppu.values()),
        total_word_count=sum(wpu.values())
    )

@app.route('/egg/', methods=['GET', 'POST'])
def egg():
    if request.method == 'GET':
        return render_template(
            'egg.html',
            egg_image='/images/BaseEgg.png',
            base_hex='#fff6de',
            pattern_hex='#9ccd83',
            pattern_file=''
        )
    base_hex = request.form['base_hex']
    pattern_file = request.form['pattern_file']
    pattern_hex = request.form['pattern_hex']
    jenny = EggGenerator('', BASE_FILE, LIGHTING_FILE)
    # apply transparency separately
    image = jenny.create_specific_egg(
        hex_to_rgba(base_hex),
        '/home/y2kekse/images/'+pattern_file,
        hex_to_rgba(pattern_hex)
    ).image
    posix = int(time.time())
    image_temp = '/home/y2kekse/images/{}.png'.format(posix)
    image.save(image_temp)
    return render_template(
        'egg.html',
        base_hex=base_hex,
        pattern_file=pattern_file,
        pattern_hex=pattern_hex,
        egg_image='/images/{}.png'.format(posix)
    )

class ModLog(db.Model):

    __tablename__ = "mod_log"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    mod_name = db.Column(db.String(4096))
    action_name = db.Column(db.String(4096))
    member_name = db.Column(db.String(4096))
    notes = db.Column(db.String(4096))
    url = db.Column(db.String(4096))

class Actions(db.Model):

    __tablename__ = "actions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))

@app.route('/mod_log/', methods=['GET', 'POST'])
def mod_log():
    if request.method == 'GET':
        return render_template(
            'mod_log.html',
            logs=ModLog.query.all(),
            actions=Actions.query.all(),
            timestamp=datetime.now()
        )
    insert_into_table(ModLog, request.form)
    return redirect(url_for('mod_log'))

@app.route('/log_actions/', methods=['GET', 'POST'])
def log_actions():
    if request.method == 'GET':
        return render_template(
            'log_actions.html',
            actions=Actions.query.all(),
            timestamp=datetime.now()
        )
    row = Actions(name=request.form['name'])
    db.session.add(row)
    db.session.commit()
    return redirect(url_for('log_actions'))


def insert_into_table(table, form):
        row = table(
            mod_name=form['mod_name'],
            member_name=form['member_name'],
            action_name=form['action_name'],
            created=datetime.now(),
            notes=form['notes'],
            url=form['my_url']
        )
        db.session.add(row)
        db.session.commit()

pcs = [pc_jenny.PCPokemon()]
balls = pc_jenny_templates.balls()
held_items = pc_jenny_templates.held_items()
genders = pc_jenny_templates.genders()
move_types = pc_jenny_templates.move_types()

@app.route('/pc_jenny1/', methods=['GET', 'POST'])
def pc_jenny1():
    pc = pc_jenny.PCPokemon()
    created_pc = pc_jenny.create_pcs([pc])
    if request.method == 'GET':
        return render_template(
            'pc_jenny1.html',
            balls=balls,
            held_items=held_items,
            genders=genders,
            move_types=move_types,
            created_pc=created_pc,
            pc=pc
        )
    pc.parse_args(request.form) 
    created_pc = pc_jenny.create_pcs([pc])
    return render_template(
        'pc_jenny1.html',
        balls=balls,
        held_items=held_items,
        genders=genders,
        move_types=move_types,
        created_pc=created_pc,
        pc=pc
    )

@app.route('/pc_jenny2/', methods=['GET', 'POST'])
def pc_jenny2():
    pc = [pc_jenny.PCPokemon() for i in range(2)]
    created_pc = pc_jenny.create_pcs(pc)
    if request.method == 'GET':
        return render_template(
            'pc_jenny2.html',
            balls=balls,
            held_items=held_items,
            genders=genders,
            move_types=move_types,
            created_pc=created_pc,
            pc=pc
        )
    pc = pc_jenny.parse_multiple(pc, request.form)
    created_pc = pc_jenny.create_pcs(pc)
    return render_template(
        'pc_jenny2.html',
        balls=balls,
        held_items=held_items,
        genders=genders,
        move_types=move_types,
        created_pc=created_pc,
        pc=pc
    )
