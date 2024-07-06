from flask import Flask, render_template, request

from LearnWord import LearnWord
from Training import Training
from OpenAIService import OpenAIService

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/api/words')
def submit():
    form = request.form
    training = Training(form['motherLanguage'], form['learningLanguage'], form['wordCount'], form['subjects'])
    result = OpenAIService().generateWords(training.motherLanguage, training.learningLanguage, training.wordCount, training.subjects)
    words = []
    csv_string = result # assuming result is the CSV compatible string returned by OpenAIService().generateWords()
    lines = csv_string.split('\n')
    for line in lines:
        if line:
            word_data = line.split(',')
            word = LearnWord(word_data[0], word_data[1], OpenAIService().generateImage(word_data[0]))
            words.append(word)
    return render_template('result.html', words=words), 201

@app.get('/test')
def test():
    myword = "Hallo Python is toll"
    return render_template('test.html', myword=myword)