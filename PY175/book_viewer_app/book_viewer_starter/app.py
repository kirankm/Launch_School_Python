from flask import Flask, render_template, g, redirect, request

app = Flask(__name__)

def in_paragraphs(text):
    lines = "".join(text).split("\n\n")
    paragraphs = [f"<p>{line}</p>" for line in lines if line]
    return ''.join(paragraphs)

app.jinja_env.filters['in_paragraphs'] = in_paragraphs


@app.before_request
def load_contents():
    with open("book_viewer/data/toc.txt", 'r') as f:
        g.contents = f.readlines()

@app.route("/")
def index():
    return render_template('home.html', contents = g.contents)

@app.route("/chapters/<page_num>")
def chapter(page_num):
    if page_num.isdigit() and (1 <= int(page_num) <= len(g.contents)):
        with open(f"book_viewer/data/chp{page_num}.txt", 'r') as f:
            chapter = f.read()
        chapter_title = f"Chapter {page_num}: {g.contents[int(page_num) - 1]}"
        return render_template('chapter.html', contents = g.contents, 
                                        chapter = chapter, 
                                        chapter_title = chapter_title)
    else:
        return redirect("/")
    
@app.route("/search")
def search():
    query = request.args.get('query', '')
    if query:
        return render_template('search_failed.html', query = query)
    else:
        return render_template('search.html', query = query)

@app.errorhandler(404)
def page_not_found(error):
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5003)