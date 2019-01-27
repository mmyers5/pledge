import re
from flask import Flask, request, render_template
from topic import jcinkThread
from egg_maker import EggGenerator, hex_to_rgba

app = Flask(__name__)
app.config['DEBUG'] = True

IMAGE_DIR = '/images'
BASE_FILE = 'BaseEgg.png'
LIGHTING_FILE = 'Base-Eggwith-Shadowand-Highlight.png'

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
            pattern_hex='#9ccd83'
        )
    base_hex = request.form['base_hex']
    pattern_file = request.form['pattern_file']
    pattern_hex = request.form['pattern_hex']
    jenny = EggGenerator(IMAGE_DIR, BASE_FILE, LIGHTING_FILE)
    # apply transparency separately
    image = jenny.create_specific_egg(
        hex_to_rgba(base_hex),
        pattern_file,
        hex_to_rgba(pattern_hex)
    )
    posix = int(time.time())
    image_temp = '/images/{}.png'.format(posix)
    image.save(image_temp.format(posix))
    return render_template(
        'egg.html',
        base_hex=base_hex,
        pattern_file=pattern_file,
        pattern_hex=pattern_hex,
        egg_image=image_temp
    )
