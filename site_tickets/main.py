from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os
from conex_sql_sever import consulta_sqlserver
from dados_ticket import quant_ticket_abertos, quant_total, lista_atendimentos_cliente, nome_cliente, endereco_cliente, bairro_cliente, numero_cliente, email_cliente

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        senha = request.form.get('senha')
        
        consulta = f"SELECT * FROM cliente WHERE login='{codigo}' AND senha={senha}" #Verfica o ususario
        resultado = consulta_sqlserver(consulta)
        print(resultado)
        
        if resultado:
            session['logged_in'] = True
            session['codigo_cliente'] = resultado[0][0]  
            session['username'] = resultado[0][1]  
            return redirect(url_for('home'))
        else:
            session.pop('logged_in', None)
            return render_template('login.html')
    
    return render_template('login.html')

@app.route("/home")
def home():
    if 'logged_in' in session:
        codigo_cliente = session.get('codigo_cliente')
        username = nome_cliente(codigo_cliente)
        quant_tickets_abertos = quant_ticket_abertos(codigo_cliente)
        quant_total_tickets = quant_total(codigo_cliente)
        atendimentos_cliente = lista_atendimentos_cliente(codigo_cliente)
        endereco = endereco_cliente(codigo_cliente)
        bairro = bairro_cliente(codigo_cliente)
        numero = numero_cliente(codigo_cliente)
        email = email_cliente(codigo_cliente)
        
        return render_template('home.html', username=username, quant_tickets_abertos=quant_tickets_abertos, quant_total_tickets=quant_total_tickets, atendimentos_cliente=atendimentos_cliente, endereco=endereco, bairro=bairro, numero=numero, email=email)
    else:
        return redirect(url_for('index'))
    
@app.route("/detalhes_atendimento/<int:cod_atendimento>")
def detalhes_atendimento(cod_atendimento):
    # Consultar o banco de dados para obter as informações do atendimento com o código fornecido
    consulta = f"SELECT FP_Atendimento.Solicitacao, FP_Atendimento.Execucao FROM FP_Atendimento WHERE FP_Atendimento.CodAtendimento = {cod_atendimento}"
    resultado = consulta_sqlserver(consulta)
    if resultado:
        informacoes = {
            "Solicitacao": resultado[0][0],
            "Execucao": resultado[0][1]
        }
        return render_template('detalhes_atendimento.html', informacoes=informacoes)
    else:
        return render_template('error.html', message="Atendimento não encontrado"), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
