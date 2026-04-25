from textblob import TextBlob
import matplotlib.pyplot as plt

print("Welcome to Smart Survey Analyzer\n")

responses = []

n = int(input("Enter number of responses: "))

for i in range(n):
    text = input(f"Response {i+1}: ")
    responses.append(text)

positive = 0
negative = 0
neutral = 0

for r in responses:
    analysis = TextBlob(r)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        positive += 1
    elif polarity < 0:
        negative += 1
    else:
        neutral += 1

total = len(responses)

print("\n--- Analysis Result ---")
print(f"Positive: {positive} ({(positive/total)*100:.2f}%)")
print(f"Negative: {negative} ({(negative/total)*100:.2f}%)")
print(f"Neutral: {neutral} ({(neutral/total)*100:.2f}%)")

# Bar chart
labels = ['Positive', 'Negative', 'Neutral']
values = [positive, negative, neutral]

plt.bar(labels, values)
plt.title("Survey Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Responses")
plt.show()
