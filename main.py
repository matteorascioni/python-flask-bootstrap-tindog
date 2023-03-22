from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    current_time = datetime.now()
    year = current_time.year
    return render_template('index.html', year=year)

if __name__ == '__main__':
    app.run()