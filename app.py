import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

app = Flask(__name__)
rf= joblib.load(open('rf.pickle', 'rb'))
gnb= pickle.load(open('gnb.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    avghum = float(request.form.get("hum"))
    avgtemp = float(request.form.get("temp"))
    month= float(request.form.get("month"))
    maxhum=avghum
    minhum=0
    mintemp=avgtemp
    
    val=[[avghum,avgtemp,maxhum,minhum,mintemp]]
    arr=np.array(val)
    predic=rf.predict(arr)
    p=round(predic[0],2)
    p2=float(p)
    
    val1=[[avgtemp,avghum,p2,month]]
    arr1=np.array(val1)
    predict=gnb.predict(arr1)
    output=round(predict[0],2)
    
    if output==0:
        output="It may not rain today";
    else:
        output="It may rain today"

    

    return render_template('index.html',output=output)


if __name__ == "__main__":
    app.run(debug=True)