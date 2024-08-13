# Python 3.12.3
from flask import Flask, template_rendered, render_template

app = Flask(__name__)

@app.route("/")
def index():
    context = {
        'title': 'Boris Isac',
    }
    return render_template('base.html', **context)

if __name__ == '__main__':
    app.run(debug=True)