from flask import Flask, render_template
from extraction import Submit, DownloadCSVData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extraction/', methods=['GET', 'POST'])
def extraction():
    form = Submit()
    if form.validate_on_submit():
        return DownloadCSVData()()
    return render_template('extraction.html', form=form)

app.run()