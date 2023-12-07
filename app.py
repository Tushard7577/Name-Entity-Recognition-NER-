from flask import Flask, render_template, request, jsonify
import spacy

app = Flask(__name__)

# Load the spaCy NER model
nlp_ner = spacy.load("model-best")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    if request.method == 'POST':
        text = request.form['text']
        doc = nlp_ner(text)
        colors = {"PAYMENT TERM": "#F67DE3"}
        options = {"colors": colors}
        html = spacy.displacy.render(doc, style="ent", options=options, page=True)
        return html

if __name__ == '__main__':
    app.run(debug=True)
