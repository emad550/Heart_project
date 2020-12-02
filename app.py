
# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

app = Flask(__name__) # initializing a flask app
# app=application
@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try :
            #  reading the inputs given by the user
            year=float(request.form['year'])
            workclass = float(request.form['workclass'])
            fnlwgt= float(request.form['fnlwgt'])
            education = float(request.form['education'])
            educationnum= float(request.form['education-num'])
            maritalstatus= float(request.form['marital-status'])
            occupation = request.form['occupation']
            if(occupation=='Adm-clerical'):
                occupation=1
            else:
               occupation=2
            relationship= request.form['relationship']
            if (relationship == 'Not-in-family'):
                relationship = 1
            else:
                relationship = 2
            filename = 'model2rf_hp1.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            #predictions using the loaded model file
            prediction=loaded_model.predict([[year,workclass,fnlwgt,education,educationnum,maritalstatus,occupation,relationship,2,3,4,1,2]])
            #prediction = loaded_model.predict([[40, 1,1,1, 13, 1, 2, 2, 3, 4, 2174, 0, 40, 2]])
            #print('prediction is', prediction)
            # showing the prediction results in a UI
            #return render_template('results.html',prediction=round(100*prediction[0]))
            #loaded_model = pickle.load(open('Randomforest_le.pickl', 'rb'))
            #from joblib import dump, load
            #clf = load('rf_le.joblib')
            #prediction=clf.predict([[40,1,77516,1,13,1,2,2,3,4,2174,0,40,2]])
            if prediction ==0 :
                prediction='low'
            else:
                prediction='high'
            return render_template('results.html',prediction=prediction)

            #prediction = loaded_model.predict([[40.0, 1.0, 77516.0, 1.0, 13.0, 1.0, 2.0, 2.0, 3.0, 4.0, 2174.0, 0.0, 40.9, 2.0]])
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app