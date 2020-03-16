from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def principale():
    return render_template('pageprincipale.html')


@app.route('/message')
def message():
    return render_template('message.html')

@app.route('/accueil')
def home():
    return render_template('accueil.html')

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  c = result['niveau']
  m = result['matiere']
  t = result['message']
  return render_template("resultat.html", nom=n, prenom=p, niveau=c, matiere=m, message=t)


if __name__ == '__main__':
    app.run(debug=True)