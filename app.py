from flask import Flask,flash,request,redirect,send_file,render_template
from werkzeug.utils import secure_filename
from dynaconf import settings
import os 
from script_API import mapbox_API # local
from db import save_to_db # local

# Inicia app flask
app = Flask(__name__)

# Página principal - upload arquivo
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Checar se o post request possui o arquivo de envio
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        # caso o usuário não selecione o arquivo, o browser mantém
        # na pág principal
        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            new_file = mapbox_API(file) # Chamar script_API
            filename = "Resultado_final.xlsx"
            new_file.save(os.path.join(settings.UPLOAD_FOLDER, filename))
            print("saved file successfully")
            # Chamar função para guardar dados no db
            save_to_db()

        # enviar nome de arquivo como parametro para download
            return redirect('/downloadfile/'+ filename)
    return render_template('index.html')

# Página de Download 
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download.html',value=filename)
@app.route('/return-files/<filename>') # Rota para download do arquivo
def return_files_tut(filename):
    file_path = settings.UPLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

# Executar flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
