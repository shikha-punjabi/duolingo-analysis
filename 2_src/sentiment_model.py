import pandas as pd
import re
import os

# Load raw review data
input_path = "../0_data/raw/duolingo_reviews_raw.csv"
df = pd.read_csv(input_path)

# Keep only relevant columns
df = df[['userName', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion', 'at']]

# Drop missing reviews
df = df.dropna(subset=['content'])

# Clean review text
def clean_text(text):
    text = re.sub(r"http\S+", "", text)                    # remove URLs
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)             # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()               # remove extra spaces
    return text.lower()

df['cleaned_content'] = df['content'].apply(clean_text)

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (only needed once)
nltk.download('vader_lexicon')

# Initialize analyzer
sid = SentimentIntensityAnalyzer()

# Apply sentiment scoring
df['sentiment_score'] = df['cleaned_content'].apply(lambda x: sid.polarity_scores(x)['compound'])

# Optional: Categorize sentiment
def label_sentiment(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

df['sentiment_label'] = df['sentiment_score'].apply(label_sentiment)

# Save cleaned version
output_path = "C:/Users/shikh/Downloads/Projects/Duolingo/duolingo-analysis/0_data/cleaned/duolingo_reviews_cleaned.csv"
df.to_csv(output_path, index=False)

print(f"✅ Cleaned data saved to {output_path}")



