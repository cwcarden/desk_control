from flask import Flask, render_template, redirect, url_for, request
import down, up

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Desk Control')

@app.route('/up', methods=['POST'])
def up():
    if request.method == 'POST':
        if request.form.get('up') == 'true':
            up()
            print(request.method)
            return redirect(url_for('home'))

@app.route('/down', methods=['POST'])
def down():
    if request.method == 'POST':
        if request.form.get('down') == 'true':
            down()
            print(request.method)
            return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000, debug=True)
