
from flask import Flask, request, jsonify
import pickle
app = Flask(__name__)


with open('trained_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/price_pred', methods=['POST'])
def lin_req():
    data = request.json
    area = data['area']
    
    price= loaded_model.predict([[area]])
    
    return jsonify({"price":price[0][0]*10000})
    return "API WORKING!"

app.run(debug=True,port=5000)

