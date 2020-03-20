from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def principale():
    return render_template('pageprincipale.html')


@app.route('/message')
def message():
    return render_template('message.html')

@app.route('/voir',methods = ['GET', 'POST'])
def voir():
    v={}
    if request.method == 'GET':
        return render_template('voir.html')
    else:
        result = request.form
        v["n"]=result['nom']
        v["p"]=result['prenom']
        v["c"]=result['niveau']
        v["m"]=result['matiere']
        v["t"]=result['message']
        return render_template("voir.html", nom=v.get("n"), prenom=v.get("p"), niveau=v.get("c"), matiere=v.get("m"), message=v.get("t"))


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

