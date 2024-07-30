from flask import Flask, render_template, request, send_from_directory, send_file
import os
import maine

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('page1.html')

@app.route('/copyfile', methods=['POST'])
def copy_file():
    file = request.files['file']
    folder_path = 'boool'
    file.save(os.path.join(folder_path, file.filename))
    return 'File copied successfully.'

@app.route('/mp4_mp3')
def nur2_page():
    return render_template('mp4_mp3.html')
@app.route('/mp3_text')
def nur3_page():
    return render_template('mp3_text.html')
@app.route('/mp4_text')
def nur4_page():
    return render_template('mp4_text.html')
@app.route('/nur5')
def nur5_page():
    maine.remove()
    maine.convert_mp4_to_mp3()
    return render_template('download1.html')
@app.route('/nur6')
def nur6_page():
    # maine.remove()
    maine.MP3_text()
    return render_template('download2.html')
# def nur7_page():
#     maine.convert_mp4_to_mp3()
#     return render_template('download3.html')

@app.route('/view_report')

def view_report():
    folder_path = 'data'
    items = os.listdir(folder_path)
    first_item = os.path.join(folder_path, items[0])
    file_path = first_item
    a = send_file(file_path)
    return a
if __name__ == '__main__':
    app.run(port=5001)
    
