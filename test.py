from logging import debug
from flask import Flask , render_template,request
import joblib
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

#loading the model
sc = StandardScaler()
Model=joblib.load('hiring_model.pkl')

@app.route('/')
def welcome():
    return render_template('base.html')

@app.route('/predict' , methods = ['POST'])
def predict():

    exp = request.form.get('experience')
    score = request.form.get('test_score')
    interview_score = request.form.get('interview_score')

    # data = sc.transform([[5,2,1,100,1,1,1,8,1,1,9]])

    prediction = Model.predict([[int(exp) , int(score) , int(interview_score)]])

    output = round(prediction[0] , 2)

    return render_template('base.html' , prediction_text = f"Employee Salary will be $ {output}")


if __name__=='__main__':
    app.run(debug=True)





""" #pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <PACKAGE NAME>

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def welcome():
    return render_template('base.html')
# ‘/’ URL is bound with hello_world() function.
@app.route('predict',methods =['post'])
def predict():
    return 'Your form is submitted'

  
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)

 """