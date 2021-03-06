#import joblib
from flask import Flask, request, jsonify, render_template
import pickle

model = pickle.load(open('model_pkl','rb'))
app = Flask(__name__)

#model = joblib.load('model.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    a=request.form["rm"]
    c=request.form["pm"]
    d=request.form["am"]
    g=request.form["conm"]
    h=request.form["cpm"]
    y=[[h,d,a,c,g]]        
    output = model.predict(y)
    if (output == 0):
    #if output == 0:
        res_val="benign(non-cancerous)"
        return render_template('Boutputpositive.html',predict='Your symtoms are {}'.format(res_val))
    else:
        res_val=" malignant breast cancer"
        return render_template('Boutputpositive.html',predict='Sorry:( You may have {}'.format(res_val))
        
    #return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
