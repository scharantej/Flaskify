
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    # Process the data here
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
