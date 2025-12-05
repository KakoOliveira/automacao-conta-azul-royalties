🤖💰 Automação Conta Azul – Royalties  
Sistema moderno em Flask para processar extratos financeiros, gerar logs e atualizar os dados de royalties de forma automatizada.

---

🔍 Sobre o Projeto

Este projeto foi criado para **automatizar o processamento de extratos do Conta Azul**, realizar tratamentos necessários e enviar os dados estruturados para uso interno.  
A automação reduz erros manuais, garante consistência e facilita o acompanhamento financeiro.

---

🚀 Tecnologias Utilizadas

- **Python 3**  
- **Flask**  
- **Subprocess** (execução do script principal)  
- **HTML/CSS**  
- **Pandas / NumPy** (usados dentro do script processador)  
- **MySQL Connector** (no script processador, quando aplicável)

---

🗂 Estrutura do Projeto

```
automacao-conta-azul-royalties/
│
├── app.py                       # Aplicação Flask
├── processa_conta_azul.py       # Script responsável pelo processamento
├── uploads/                     # Onde o arquivo enviado é salvo
├── templates/
│     ├── index.html             # Página inicial (upload + dados)
│     └── processamento.html     # Página de logs
└── README.md
```

---

🖥 Código da Aplicação (Flask)

Abaixo está o código usado na aplicação web.  
**Sem nenhum dado sensível**, pronto para colar no projeto:

```python
from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

PASSWORD = "SUA_SENHA_AQUI"  # Defina sua senha manualmente depois

os.makedirs("uploads", exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    senha = request.form.get("senha")
    usuario = request.form.get("usuario")
    setor = request.form.get("setor")

    if senha != PASSWORD:
        return "Senha incorreta!"

    if not usuario or not setor:
        return "Selecione o usuário e o setor."

    if "arquivo" not in request.files:
        return "Nenhum arquivo enviado!"

    arquivo = request.files["arquivo"]
    caminho_salvo = os.path.join("uploads", "extrato_financeiro.xls")
    arquivo.save(caminho_salvo)

    process = subprocess.Popen(
        ["python", "processa_conta_azul.py", caminho_salvo, usuario, setor],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate()
    logs = stdout if stdout else "Sem logs retornados."

    return render_template(
        "processamento.html",
        usuario=usuario,
        setor=setor,
        logs=logs
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

📦 Como Rodar o Projeto

1️⃣ Instalar dependências
```
pip install flask pandas numpy mysql-connector-python
```

2️⃣ Executar a aplicação
```
python app.py
```

3️⃣ Acessar no navegador  
```
http://127.0.0.1:5000
```

---

📁 Upload do Extrato

O sistema aceita o arquivo extrato_financeiro.xls, salva automaticamente em `/uploads` e dispara o script `processa_conta_azul.py`.

Toda a saída do processamento aparece limpa na tela final.

---

📝 Logs em Tempo Real

Após o upload, o sistema:

1. Envia o arquivo para o script principal  
2. Captura toda saída em `stdout`  
3. Exibe os logs na tela de forma organizada  

Ideal para auditoria e acompanhamento.

---

🔒 Segurança

- Senha de acesso configurável  
- Scripts isolados  
- Sem armazenamento permanente de dados  
- Extratos processados apenas localmente  

> Obs.: Lembre-se de substituir `SUA_SENHA_AQUI` pela senha real apenas no seu ambiente privado.

---

👨‍💻 Autor

Kako Oliveira  
Especialista em Automação, Dados e Desenvolvimento Python.  




