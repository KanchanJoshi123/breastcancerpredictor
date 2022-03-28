import joblib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
#trans=joblib.load('Scalar.save')
model = joblib.load('model.save')

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
    y=[[float(h),float(d),float(a),float(c),float(g)]]        
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
