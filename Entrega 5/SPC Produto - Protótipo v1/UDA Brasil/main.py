from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return redirect(url_for('screen1')) # Chama a função screen1 (Para sempre redirecionar para a tela de login)

@app.route('/login')
def screen1():
    return render_template('screen1.html') 

@app.route('/input')
def screen2():
    return render_template('screen2.html') 

@app.route('/rank')
def rank():
    return render_template('screen3.html')

if __name__ == "__main__":
    app.run(debug=True)
