from flask import Flask, render_template, request
import pickle
import webbrowser
import threading

app = Flask(__name__)

# মডেল লোড
model = pickle.load(open('Titanic Prediction.pk1', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    Pclass = int(request.form['Pclass'])
    Sex = int(request.form['Sex'])
    Age = float(request.form['Age'])
    SibSp = int(request.form['SibSp'])
    Parch = int(request.form['Parch'])
    Fare = float(request.form['Fare'])
    
    embarked = request.form['Embarked']
    Embarked_C = 1 if embarked == 'C' else 0
    Embarked_Q = 1 if embarked == 'Q' else 0

    features = [[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked_C, Embarked_Q]]
    prediction = model.predict(features)[0]
    result = "Survived ✅" if prediction == 1 else "Did not survive ❌"

    return render_template('index.html', prediction=result)

#  ব্রাউজার অটো ওপেন করার ফাংশন
def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)
