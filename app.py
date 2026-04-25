from flask import Flask, render_template, request
from textblob import TextBlob
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    graph_url = None

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

        # 📊 Create graph
        labels = ['Positive', 'Negative', 'Neutral']
        values = [positive, negative, neutral]

        plt.figure()
        plt.bar(labels, values)

        # Save image to memory
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        graph_url = base64.b64encode(img.getvalue()).decode()

    return render_template('index.html', result=result, graph_url=graph_url)

if __name__ == "__main__":
    app.run(debug=True)
