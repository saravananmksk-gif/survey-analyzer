from textblob import TextBlob

print("Welcome to Smart Survey Analyzer\n")

responses = []

n = int(input("Enter number of responses: "))

for i in range(n):
    text = input(f"Response {i+1}: ")
    responses.append(text)

positive = 0
negative = 0

for r in responses:
    analysis = TextBlob(r)
    if analysis.sentiment.polarity > 0:
        positive += 1
    else:
        negative += 1

print("\n--- Analysis Result ---")
print(f"Positive responses: {positive}")
print(f"Negative responses: {negative}")