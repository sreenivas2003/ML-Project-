import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Take user input and analyze sentiment
text = input("Enter a sentence to analyze sentiment: ")

# Get sentiment scores
scores = analyzer.polarity_scores(text)

# Display the result
print("\nSentiment Scores:")
for k, v in scores.items():
    print(f"{k.capitalize()}: {v}")

# Interpret the result
if scores['compound'] >= 0.05:
    print("Overall Sentiment: Positive 😊")
elif scores['compound'] <= -0.05:
    print("Overall Sentiment: Negative 😠")
else:
    print("Overall Sentiment: Neutral 😐")



output:
Enter a sentence to analyze sentiment:  i hate you

Sentiment Scores:
Neg: 0.787
Neu: 0.213
Pos: 0.0
Compound: -0.5719
Overall Sentiment: Negative 😠

Enter a sentence to analyze sentiment:  i love this product

Sentiment Scores:
Neg: 0.0
Neu: 0.323
Pos: 0.677
Compound: 0.6369
Overall Sentiment: Positive 😊
