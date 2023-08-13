from app import app # variavel onde instanciamos o flask
import os
    # no TERMINAL  pip install python-dotenv 
    #      PARA PODER CRIAR VARIAVEIS DE HAMBIENTE
if __name__=='main':
    port = int(os.getenv('PORT'),'5000')
    app.run(host='0.0.0.0',port=port)

