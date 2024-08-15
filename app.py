# Python 3.12.3
from flask import Flask, template_rendered, render_template
from form import FormContact
from config import secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

@app.route("/")
def index():
    form = FormContact()
    context = {
        'title': 'Work Shop',
        'form': form,
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)