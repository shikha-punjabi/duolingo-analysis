from google_play_scraper import Sort, reviews
import pandas as pd
import os

# Create directory if it doesn't exist
os.makedirs("../0_data/raw", exist_ok=True)

# Fetch 2000 reviews from Duolingo app on Google Play (English, US)
result, _ = reviews(
    'com.duolingo',
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=2000
)

# Convert to DataFrame
df = pd.DataFrame(result)

# Save to CSV
csv_path = "C:/Users/shikh/Downloads/Projects/Duolingo/duolingo-analysis/0_data/raw/duolingo_reviews_raw.csv"
df.to_csv(csv_path, index=False)
print(f"✅ Saved {len(df)} reviews to {csv_path}")
