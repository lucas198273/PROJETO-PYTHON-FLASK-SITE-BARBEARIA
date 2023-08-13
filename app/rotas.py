from app import app
from flask import render_template
from flask import request
from flask import flash # para trabalhar com preenchimento de formulario 
                            # Respostas rapidas de interação
                            # Sera nessesario definir configuração 
                            
from flask import redirect # redireciona para uma pagina html

@app.route('/')
def index():
    dados1 = {"Nome": "JP Barber", "Contato": "31992311011"}
    dados2 = {"Nome": "Carlos Andrade", "Contato": "31992311011"}
    return render_template('index.html', dados1=dados1, dados2=dados2, )

@app.route('/loja')
def loja():
    return render_template('loja.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == "lucas" and senha == "123":
        
        return redirect ('/loja') 
        
        
    else: 
        flash(" Dados invalidos") # Menssagem rapida
        flash(" login ou senha  invalidos") # Menssagem rapida
        return redirect ('/login')
    
if __name__ == '__main__':
    app.run(debug=True)
