from flask import Flask,render_template,request
import random
app = Flask(__name__)

@app.route('/')#home
def index():
    return render_template(
    'index.html',
    icons = ic(),
    title = 'pentest-info',
    email = 'email',

    )

def ic():
    iconslib = {
        1: 'play_arrow',
        2: 'done_all',
        3: 'thumbs_up_down',
        4: 'pets',
        5: 'offline_pin',
        6: 'visibility',
        7: 'vpn_key',
        8: 'forward',
        9: 'flash_on',
        10: 'vpn_lock',
    }
    generationskey = random.randint(1, 10)
    icons = iconslib.get(generationskey)
    return icons

@app.route('/litr')#literatures
def litr():
    return render_template(
    'litr.html',
    icons = ic(),
    title = 'pentest-info',
    email = 'email',
    )

@app.route('/dist')#distributiv
def dist():
    return render_template(
    'dits.html'
    )

if __name__ == '__main__':
    app.run(debug = True)
