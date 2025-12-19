from flask import Flask, request, jsonify
import os, tempfile
from src import process

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = tempfile.gettempdir()

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    llm = request.form.get("llm")
    prompt = request.form.get("prompt")
    version = request.form.get("version")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # processa ficheiro com tua lógica
    output = process.run(file_path, llm=llm, prompt=prompt, version=version)

    return jsonify({"status": "ok", "output": output})

if __name__ == "__main__":
    app.run(debug=True)