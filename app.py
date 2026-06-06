from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def index():
    titulo = "Jessenia V en Python con Flask"
    return render_template('index.html', titulo=titulo)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)