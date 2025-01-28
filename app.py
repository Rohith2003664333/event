from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/security')
def security():
    return render_template('security.html')

@app.route('/security_book')
def security_book():
    return render_template('security_book.html')


@app.route('/catering')
def catering():
    return render_template('catering.html')

@app.route('/photographers')
def photographers():
    return render_template('photographers.html')

@app.route('/decorators')
def decorators():
    return render_template('decorators.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
