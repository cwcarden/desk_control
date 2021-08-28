from flask import Flask, render_template, redirect, url_for, request
import relays


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('up') == 'up':
            relays.up()

        elif request.form.get('stop_up') == 'stop':
            relays.stop_up()

        if request.form.get('down') == 'down':
            relays.down()

        elif request.form.get('stop_down') == 'stop':
            relays.stop_down()

        else:
            return render_template('index.html', title='Desk Control')
    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)
