from flask import Flask, render_template, url_for, g, redirect, request

app = Flask(__name__)

@app.template_filter('in_paragraphs')
def in_paragraphs(text):
   para_text = text.split('\n\n')
   return '\n'.join([f'<p id={index+1}>{para}</p>' for index, para in 
                                                    enumerate(para_text)])

@app.before_request
def load_contents():
    with open('book_viewer/data/toc.txt') as f:
        g.contents  = f.readlines()

@app.route("/")
def home():
    return render_template('home.html', contents = g.contents)

@app.route("/chapters/<page_num>")
def chapter(page_num):
    if page_num.isdigit() and (1 <= int(page_num) <= len(g.contents)):
        chapter_title = f"Chapter {page_num}"

        with open(f'book_viewer/data/chp{page_num}.txt') as f:
            chapter_content = f.read()

        chapter_name = g.contents[int(page_num) - 1]
        return render_template('chapter.html', contents = g.contents, 
                                                chapter_content = chapter_content,
                                                chapter_title = chapter_title,
                                            chapter_name = chapter_name)
    else:
        return redirect('/')                                    

@app.route("/search")
def search():
    query = request.args.get('query', '')
    results = search_term_in_contents(query)
    return render_template('search.html', query = query, results = results,
                                            contents = g.contents)

def search_term_in_contents(search_term):
    results = {}
    for index, chapter in enumerate(g.contents):
        with open(f'book_viewer/data/chp{index + 1}.txt') as f:
            chapter_content = f.read()
        if chapter_content.find(search_term) != -1:
            paragraphs = get_paragraph_with_search_term(chapter_content, 
                                                        search_term)
            results[chapter] = {}
            results[chapter]['index'] = index + 1
            results[chapter]['paragraphs'] = paragraphs 
    return results

def get_paragraph_with_search_term(content, search_term):
    sel_paras = {}
    all_paras = content.split('\n\n')
    for index, para in enumerate(all_paras):
        if para.find(search_term) != -1:
            sel_paras[index] = para
    return sel_paras
    
@app.template_filter('highlight')
def highlight(text, term):
    return text.replace(term, f'<strong>{term}</strong>')

@app.errorhandler(404)
def redirect_to_home(_error):
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5003)
