from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    with open("book_viewer/data/toc.txt", 'r') as f:
        contents = f.readlines()
    return render_template('home.html', contents = contents)

@app.route("/chapters/1")
def chapter():
    with open("book_viewer/data/chp1.txt", 'r') as f:
        chapter = f.read()
    with open("book_viewer/data/toc.txt", 'r') as f:
        contents = f.readlines()
    chapter_name = "Chapter 1"
    return render_template('chapter.html', contents = contents, 
                                    chapter = chapter, 
                                    chapter_name = chapter_name)

if __name__ == "__main__":
    app.run(debug=True, port=5003)