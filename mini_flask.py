import os
from flask import Flask, redirect, url_for, request, render_template, send_from_directory
from werkzeug import secure_filename
from models.chexnet_graph import ChexNetDeploy

# folder to upload pictures
UPLOAD_FOLDER = './uploads/'
# what files can upload
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# start + config
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS']=ALLOWED_EXTENSIONS
model = ChexNetDeploy("http://127.0.0.1:9000")

# main route
@app.route('/')
def index():
    return render_template('upload.html')

# is file allowed to be uploaded?
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# result of model prediction
@app.route('/classification/<result>')
def classification(result):
    return render_template('result.html', result=result)

# file upload route
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # remove unsupported chars etc
        filename = secure_filename(file.filename)
        #save path
        save_to=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(save_to)
        #save file
        file.save(save_to)
        n_crops, preprocessed_image = model.preprocessing(save_to)
        model.predict(preprocessed_image)
        final_result = model.process_result(n_crops)
        #show if photo is a photo of hotdog 
        return redirect(url_for('classification', result=final_result))
        

#file show route (not using now)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/switch_model')
def background_process_test():
    return "nothing"


if __name__ == '__main__':
   app.run()
   #python mini_flask.py