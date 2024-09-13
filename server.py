from flask import Flask, request, jsonify, render_template
import csv

app = Flask(__name__)

@app.route('/dados')
def exibir_dados():
    with open('dados_sensores.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        dados_csv = list(reader)
        dados_csv.reverse()  # Inverter a ordem dos dados
    return render_template('dados.html', dados_csv=dados_csv)

@app.route('/atualizar_tabela')
def atualizar_tabela():
    with open('dados_sensores.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        dados_csv = list(reader)
        dados_csv.reverse()  # Inverter a ordem dos dados
    return render_template('tabela.html', dados_csv=dados_csv)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
