from flask import Flask, request, jsonify
import requests
import WMA
import SMA
import DEMA
import TRIMA
app = Flask(__name__)


#Trima
@app.route('/dados_financeiros_TRIMA_hight', methods=['GET'])
def listar_dados_financeiros_trima_hight():
    response = requests.get(TRIMA.base_url_trima, params=TRIMA.params_trima_hight)
    data = response.json()
    return jsonify(data)

@app.route('/dados_financeiros_TRIMA_low', methods=['GET'])
def listar_dados_financeiros_trima_low():
    response = requests.get(TRIMA.base_url_trima, params=TRIMA.params_trima_low)
    data = response.json()
    return jsonify(data)


@app.route('/dados_financeiros_TRIMA_close', methods=['GET'])
def listar_dados_financeiros_trima_close():
    response = requests.get(TRIMA.base_url_trima, params=TRIMA.params_trima_close)
    data = response.json()
    return jsonify(data)


#Dema
@app.route('/dados_financeiros_DEMA_hight', methods=['GET'])
def listar_dados_financeiros_dema_hight():
    response = requests.get(DEMA.base_url_dema, params=DEMA.params_dema_hight)
    data = response.json()
    return jsonify(data)

@app.route('/dados_financeiros_DEMA_low', methods=['GET'])
def listar_dados_financeiros_dema_low():
    response = requests.get(DEMA.base_url_dema, params=DEMA.params_dema_low)
    data = response.json()
    return jsonify(data)


@app.route('/dados_financeiros_DEMA_close', methods=['GET'])
def listar_dados_financeiros_dema_close():
    response = requests.get(DEMA.base_url_dema, params=DEMA.params_dema_close)
    data = response.json()
    return jsonify(data)

#WMA
@app.route('/dados_financeiros_WMA_hight', methods=['GET'])
def listar_dados_financeiros_wma_hight():
    response = requests.get(WMA.base_url_wma, params=WMA.params_wma_hight)
    data = response.json()
    return jsonify(data)

@app.route('/dados_financeiros_WMA_low', methods=['GET'])
def listar_dados_financeiros_wma_low():
    response = requests.get(WMA.base_url_wma, params=WMA.params_wma_low)
    data = response.json()
    return jsonify(data)


@app.route('/dados_financeiros_WMA_close', methods=['GET'])
def listar_dados_financeiros_wma_close():
    response = requests.get(WMA.base_url_wma, params=WMA.params_wma_close)
    data = response.json()
    return jsonify(data)


#SMA

@app.route('/dados_financeiros_SMA_hight', methods=['GET'])
def listar_dados_financeiros_sma_hight():
    response = requests.get(SMA.base_url_sma, params=SMA.params_sma_hight)
    data = response.json()
    return jsonify(data)
@app.route('/dados_financeiros_SMA_low', methods=['GET'])
def listar_dados_financeiros_sma_low():
    response = requests.get(SMA.base_url_sma, params=SMA.params_sma_hight)
    data = response.json()
    return jsonify(data)
@app.route('/dados_financeiros_SMA_close', methods=['GET'])
def listar_dados_financeiros_sma_close():
    response = requests.get(SMA.base_url_sma, params=SMA.params_sma_hight)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
