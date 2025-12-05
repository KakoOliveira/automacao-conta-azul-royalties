⚙️ Automação Conta Azul — Extrato Financeiro → Royalties | Campsoft

Automação avançada desenvolvida para processar o **extrato financeiro do Conta Azul**, validar dados, realizar limpeza inteligente, detectar duplicidades, gerar hash único por transação e **inserir os resultados diretamente no banco de dados MySQL do Tocalivros** para uso no painel de **Royalties**.  

> 🔒 Aplicação com upload seguro + autenticação + logs detalhados  
> 🟦 Desenvolvido em Python + Flask  
> 🗄️ Integração com MySQL  
> 📊 Otimizada para uso interno da Campsoft  

---

🚀 Funcionalidades Principais

🔹 Upload seguro do arquivo `.xls`
O usuário faz o upload do extrato e o sistema renomeia automaticamente para `extrato_financeiro.xls`.

🔹 Execução automática do processador
O Flask roda o script:

```
processa_conta_azul.py <arquivo> <usuario> <setor>
```

🔹 Logs completos
A interface exibe todos os logs retornados pelo script:
- registros processados  
- duplicidades encontradas  
- dados inseridos  
- datas e hash únicos  

🔹 Controle de acesso
Senha padrão configurada:

```
PASSWORD = "Campsoft123"
```

(ambiente real recomenda usar variáveis de ambiente 🔐)

---

🧠 Estrutura do Projeto

```
automacao-conta-azul-royalties/
│
├── app.py                     # Servidor Flask
├── processa_conta_azul.py     # Script principal de processamento
│
├── uploads/                   # Pasta onde o extrato é salvo
│
├── templates/
│   ├── index.html             # Página de upload
│   ├── processamento.html     # Exibição dos logs
│
└── README.md
```

---

🖥️ Código Completo do Servidor Flask

```python
from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

PASSWORD = "Campsoft123"

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

    # Executa o script e captura logs
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

🛠️ Como Rodar Localmente

1️⃣ Instalar dependências
```
pip install flask mysql-connector-python pandas tkinterdnd2
```

2️⃣ Iniciar o servidor
```
python app.py
```

3️⃣ Acessar no navegador
```
http://localhost:5000
```

---

## 🔒 Segurança Recomendada
Substituir a senha fixa por variável de ambiente:

```python
PASSWORD = os.getenv("SENHA_AUTOMACAO")
```

E no Windows PowerShell:
```
setx SENHA_AUTOMACAO "MinhaSenhaUltraSegura"
```

---

🧑‍💻 Autor

Kako Oliveira 
Desenvolvedor Python | Automações | Integrações Campsoft  
📍 Mauá — SP  
🐙 GitHub: https://github.com/KakoOliveira

---

## 📌 Licença

Uso interno — Campsoft / Tocalivros.

