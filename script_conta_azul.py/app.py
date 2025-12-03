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
