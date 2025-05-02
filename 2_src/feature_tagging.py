import pandas as pd

# Load the enhanced dataset
df = pd.read_csv("C:/Users/shikh/Downloads/Projects/Duolingo/duolingo-analysis/0_data/cleaned/duolingo_reviews_with_length.csv")

# Define feature keywords
feature_keywords = {
    "streaks": ["streak", "streaks"],
    "hearts": ["hearts", "lives", "out of hearts"],
    "ads": ["ad", "ads", "advertisement"],
    "xp": ["xp", "experience", "points"],
    "leaderboard": ["leaderboard", "rank", "ranking"],
    "owl": ["owl", "duo", "bird"]
}

# Function to tag first mentioned feature
def tag_feature(text):
    text = str(text).lower()
    for feature, keywords in feature_keywords.items():
        if any(keyword in text for keyword in keywords):
            return feature
    return "other"

df["feature_mentioned"] = df["cleaned_content"].apply(tag_feature)

# Save new version
df.to_csv("C:/Users/shikh/Downloads/Projects/Duolingo/duolingo-analysis/0_data/cleaned/duolingo_reviews_tagged.csv", index=False)
print("✅ Feature tagging complete. Saved to duolingo_reviews_tagged.csv")
