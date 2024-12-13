from flask import Flask, render_template, request
import os

app = Flask(__name__)


# Página inicial, onde o formulário será exibido
@app.route('/')
def index():
    return render_template('form.html')


# Rota que recebe o formulário quando o usuário envia
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Coletando os dados do formulário
        full_name = request.form['full_name']
        address = request.form['address']
        materials = request.form['materials']
        installation_location = request.form['installation_location']
        motor_quantity = request.form['motor_quantity']

        # Exibindo os dados no console (ou você pode enviar para um email ou outro destino)
        print(f'Nome Completo: {full_name}')
        print(f'Endereço: {address}')
        print(f'Materiais/Serviços: {materials}')
        print(f'Local de Instalação: {installation_location}')
        print(f'Quantidade de Motores: {motor_quantity}')

        # Você pode retornar uma resposta simples ou redirecionar para outra página
        return f'Obrigado, {full_name}! Seu formulário foi enviado com sucesso!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))