from flask import Flask, render_template, abort
import os

app = Flask(__name__)


CONTENT_DIR = 'posts'

@app.route('/')
def index():
    pages = []
    for folder_name in os.listdir(CONTENT_DIR):
        folder_path = os.path.join(CONTENT_DIR, folder_name)
        if os.path.isdir(folder_path) and 'content.txt' in os.listdir(folder_path):
            pages.append(folder_name)
    return render_template('index.html', pages=pages)

@app.route('/page/<title>')
def show_page(title):
    file_path = os.path.join(CONTENT_DIR, title, 'content.txt')
    if not os.path.exists(file_path):
        abort(404)
    with open(file_path, 'r') as f:
        content = f.read()
    return render_template('page.html', title=title, content=content)

if __name__ == '__main__':
    app.run(debug=True)