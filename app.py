from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        text = request.form['responses']
        responses = text.split('\n')

        positive = 0
        negative = 0
        neutral = 0

        for r in responses:
            polarity = TextBlob(r).sentiment.polarity
            if polarity > 0:
                positive += 1
            elif polarity < 0:
                negative += 1
            else:
                neutral += 1

        total = len(responses)

        result = {
            "positive": positive,
            "negative": negative,
            "neutral": neutral,
            "positive_pct": round((positive/total)*100,2),
            "negative_pct": round((negative/total)*100,2),
            "neutral_pct": round((neutral/total)*100,2)
        }

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
