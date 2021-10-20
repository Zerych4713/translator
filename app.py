from flask import Flask, render_template, request
from translate import Translator
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def perevod():
    if request.method =='POST':
        metper = Translator(to_lang='ru')
        resper = request.form['textftrans']
        resper = metper.translate(resper)
        return render_template('index.html',textresper=resper)
    if request.method =='GET':
        return render_template('index.html')


@app.route('/<name>')
def adress(name):
    return render_template('index.html',name=name)


if __name__ == '__main__':
    app.run()