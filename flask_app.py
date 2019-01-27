import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
from flask import Flask, request, render_template
import json
import egg_maker as em

app = Flask(__name__)
app.config["DEBUG"] = True

def word_count(text):
    text.split()
    words = re.findall(r"[\w']+", text.lower())
    return len(words)

class jcinkPage():
    def __init__(self, url):
        self.url = url

    @property
    def posts(self):
        tag = 'div'
        attrs = {
            'class': 'postcolor'
        }
        return self.soup.find_all(tag, attrs)

    @property
    def users(self):
        tag = 'span'
        attrs = {
            'class': 'postdetails'
        }
        return self.soup.find_all(tag, attrs)[1::2]

    @property
    def soup(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.text, 'html.parser')

    @property
    def current_page(self):
        tag = 'span'
        attrs = {
            'class': 'pagination_current'
        }
        return self.soup.find(tag, attrs).get_text()

    @property
    def user_order(self):
        return [self.user_name(i) for i in self.users]

    @property
    def posts_per_user(self):
        return Counter(self.user_order)

    @property
    def words_per_post(self):
        post_counter = []
        for post in self.posts:
            self.remove_edits(post)
            text = post.get_text()
            nwords = word_count(text)
            post_counter.append(nwords)
        return post_counter

    @property
    def words_per_user(self):
        users = {name: 0 for name in set(self.user_order)}
        for name, nwords in zip(self.user_order, self.words_per_post):
            users[name] += nwords
        return users

    def remove_edits(self, post):
        tag = 'span'
        attrs = {
            'class': 'edit'
        }
        edited = post.find(tag, attrs)
        if edited:
            edited.replace_with('')

    def user_name(self, user):
        user_text = user.get_text()
        return user_text.split('posted')[-2].strip()


class jcinkThread():
    def __init__(self, url):
        self.url = url

    @property
    def n_pages(self):
        page = jcinkPage(self.url)
        tag = 'a'
        last_attrs = {
            'class': 'pagination_last'
        }
        norm_attrs = {
            'class': 'pagination_page'
        }
        pagination_last = page.soup.find(tag, last_attrs)
        if pagination_last:
            num = int(re.search('\d+', pagination_last.get('title')).group(0))
        elif page.soup.find(tag, norm_attrs):
            all_found_pages = page.soup.find_all(tag, norm_attrs)
            pages = {int(i.get_text()) for i in all_found_pages}
            num = max(set(pages))
        else:
            num = 1
        return num

    def main(self):
        words_per_user = Counter()
        posts_per_user = Counter()
        for i in range(self.n_pages):
            url = '{}&st={}'.format(self.url, 20*i)
            page = jcinkPage(url)
            page_wpu = Counter(page.words_per_user)
            page_ppu = Counter(page.posts_per_user)
            words_per_user.update(page_wpu)
            posts_per_user.update(page_ppu)
        return [words_per_user, posts_per_user]

@app.route('/butts', methods=['GET'])
def butts():
    thread_num = request.args['thread_num']
    url = 'http://pokemonpledge.jcink.net/index.php?showtopic={}'.format(
        thread_num
    )
    thread = jcinkThread(url)
    results = thread.main()
    return json.dumps(results)

def butts2(thread_num):
    #thread_num = request.args['thread_num']
    url = 'http://pokemonpledge.jcink.net/index.php?showtopic={}'.format(
        thread_num
    )
    thread = jcinkThread(url)
    results = thread.main()
    users = list(results[0].keys())
    post_count = results[1]
    word_count = results[0]
    total_post_count = sum(post_count.values())
    total_word_count = sum(word_count.values())
    return users, post_count, word_count, total_post_count, total_word_count

def get_thread_num(url='http://pokemonpledge.jcink.net/index.php?showtopic=6051&view=getnewpost'):
    showtopic = re.search('showtopic=\d*', url).group(0)
    thread_num = showtopic.split('=')[-1]
    return int(thread_num)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        post_count = {'test': 1}
        word_count = {'test': 2}
        return render_template("main_page.html")
    contents = request.form["contents"]
    try:
        thread_num = int(contents)
    except:
        thread_num = get_thread_num(url=contents)
    users, post_count, word_count, total_post_count, total_word_count = butts2(thread_num)
    return render_template(
        "showtopic_summary.html", users=users, post_count=post_count, word_count=word_count,
        total_post_count=total_post_count, total_word_count=total_word_count)

@app.route("/codemybutt/", methods=["GET"])
def codemybutt():
    return render_template(
        "mod_code.html")

@app.route("/egg/", methods=["GET"])
def showme():
    return render_template("egg.html")
