
from flask import Flask, render_template, request
import scraper
import processor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    insights = None
    if request.method == 'POST':
        source = request.form['source']
        destination = request.form['destination']
        data = scraper.get_data(source, destination)
        insights = processor.analyze(data)
    return render_template('index.html', insights=insights)

if __name__ == '__main__':
    app.run(debug=True)
