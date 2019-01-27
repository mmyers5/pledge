import re
from collections import Counter
from flask import Flask, request, render_template
from topic import jcinkThread

app = Flask(__name__)
app.config["DEBUG"] = True

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html")
    contents = request.form["thread"]
    try:
        thread_num = int(contents)
    except:
        thread_num = get_thread_num(url=contents)
    users, wpu, ppu = topic_counter(thread_num)
    return render_template(
        "showtopic_summary.html",
        users=users,
        post_count=ppu,
        word_count=wpu,
        total_post_count=sum(ppu.values()),
        total_word_count=sum(wpu.values())
    )
