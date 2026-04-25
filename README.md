# Smart Survey Analyzer

A web-based Python application that analyzes survey responses using sentiment analysis.

## Features
- Web interface built using Flask
- Classifies responses as positive, negative, or neutral
- Displays percentage of each sentiment
- Uses NLP (TextBlob)

## Objective
To automate the analysis of survey responses using Natural Language Processing (NLP) techniques.

## Tech Stack
- Python
- Flask
- TextBlob

## How to Run

1. Install dependencies:
pip install textblob flask

2. Run the application:
python app.py

3. Open in browser:
http://127.0.0.1:5000

## Example

### Input
Good service  
Very bad experience  
Average support  

### Output
Positive: 1 (33.33%)  
Negative: 1 (33.33%)  
Neutral: 1 (33.33%)  
