
from flask import Flask,jsonify,request,render_template
from project_app.utils import TitanicClass

import config

app = Flask(__name__)


@app.route("/")  
def hello_flask():
    return "Welcome to Titanic - Survived or Not Prediction"
    
@app.route('/test')
def titanic():
    return render_template("index.html")
        
        
@app.route('/result', methods = ['POST', 'GET'])

def get_survived_pred():
    if request.method == 'POST':
        result = request.form

        Pclass  = result['Pclass']
        Gender  = result['Gender']
        Age     = result['Age']
        SibSp   = result['SibSp']
        Parch   = result['Parch']
        Fare    = result['Fare']
        Embarked =result['Embarked']

        titanic_surv = TitanicClass(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
        prediction = titanic_surv.get_predict_survived()
        if(prediction == 1):
            return render_template("index.html", prediction = "Survived")
        else:
            return render_template("index.html", prediction = "Not Survived")
            
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)  # server start
