# Smart Survey Analyzer

A web-based Python application that analyzes survey responses using Natural Language Processing (NLP) and visualizes results using graphs.

---

## 🚀 Features
- Web interface built using Flask
- Sentiment analysis using TextBlob
- Classifies responses as:
  - Positive
  - Negative
  - Neutral
- Displays sentiment percentage breakdown
- Generates graphical visualization of results
- Converts graph into image and displays it on the web page

---

## 🎯 Objective
To automate the analysis of survey responses using Natural Language Processing (NLP) techniques and present insights visually for better understanding.

---

## 🛠 Tech Stack
- Python
- Flask
- TextBlob
- Matplotlib (for graph generation)
- HTML/CSS (Frontend)

---

## 📊 Graph Visualization
- Sentiment results are visualized using a bar/pie chart
- Graph is generated dynamically using Python (Matplotlib)
- Saved as an image in the `static/` folder
- Displayed directly in the Flask web interface

---

## Example

### Input
Good service  
Very bad experience  
Average support  


### 📊 Output
- Positive: 1 (33.33%)  
- Negative: 1 (33.33%)  
- Neutral: 1 (33.33%)  

### 📈 Result Visualization
A bar/pie chart is generated dynamically using Python and displayed in the web interface for better insight into survey sentiment distribution.

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```
Open the application in browser.
