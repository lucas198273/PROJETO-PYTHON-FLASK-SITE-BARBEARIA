from app import app  # app onde intanciamos o objeto flask

# rota inicial , para onde o codigo sera enviado
@app.route('/')  #ENDEREÇO PADRAO DE SERVIDOR LOCAL
@app.route('/index') # ROTA ALTERNATIVA CASO O USUARIO DIGITE O NOME DO SITE \INDEX
def index():
    nome = "Lucas  dias"
    return '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bem-vindo ao Blog</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            text-align: center;
            padding: 20px;
            border-radius: 8px;
            background-color: #fff;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #f44336;
            margin-bottom: 10px;
        }
        p {
            color: #333;
        }
        strong {
            color: #388e3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bem-vindo ao Nosso Blog</h1>
        <p>Olá, prezado(a) visitante!</p>
        <p>Esperamos que você desfrute de nosso conteúdo.</p>
        <p>Fique à vontade para explorar e interagir conosco.</p>
        <p>Seu nome: <strong>{{ nome }}</strong></p>
    </div>
</body>
</html>

'''