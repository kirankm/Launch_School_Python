from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    with open("book_viewer/data/toc.txt", 'r') as f:
        contents = f.readlines()
    return render_template('home.html', contents = contents)

@app.route("/chapters/<page_num>")
def chapter(page_num):
    with open(f"book_viewer/data/chp{page_num}.txt", 'r') as f:
        chapter = f.read()
    with open("book_viewer/data/toc.txt", 'r') as f:
        contents = f.readlines()
    chapter_num = f"Chapter {page_num}"
    chapter_title = contents[int(page_num) - 1]
    return render_template('chapter.html', contents = contents, 
                                    chapter = chapter, 
                                    chapter_num = chapter_num,
                                    chapter_title = chapter_title)

@app.route("/show/<name>")
def show(name):
    return name

if __name__ == "__main__":
    app.run(debug=True, port=5003)