import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---- Load Data ----
real_df = pd.read_csv("../duolingo-analysis/0_data/exports/duolingo_final_dataset.csv")
sim_df = pd.read_csv("../duolingo-analysis/0_data/exports/duolingo_simulated_dataset.csv")

# ---- Sidebar ----
st.sidebar.title("🔧 Filters")
use_simulation = st.sidebar.radio("View Mode", ["Real Data", "Simulated Fix (No Hearts)"])
feature = st.sidebar.selectbox("Feature Mentioned", real_df['feature_mentioned'].unique())

# Select dataset
df = sim_df if use_simulation == "Simulated Fix (No Hearts)" else real_df
filtered = df[df['feature_mentioned'] == feature]

# ---- Title & Intro ----
st.title("📊 Duolingo Review Explorer Dashboard")
st.markdown(f"""
This interactive dashboard analyzes over 2,000 Duolingo app reviews to explore how users respond to key gamified features like **hearts**, **streaks**, and **leaderboards**.  
Use the sidebar to filter reviews by feature and view either real or simulated results.
""")

# ---- KPIs ----
st.header(f"📌 Feature: '{feature}'")
col1, col2, col3 = st.columns(3)
col1.metric("Avg. Sentiment", round(filtered['sentiment_score'].mean(), 2))
col2.metric("Churn Risk", f"{round(filtered['churn_risk'].mean() * 100, 1)}%")
col3.metric("Total Reviews", len(filtered))

# ---- Histogram ----
st.subheader("📈 Sentiment Score Distribution")
fig = px.histogram(filtered, x='sentiment_score', nbins=20, title="Sentiment Histogram", color_discrete_sequence=['#4C78A8'])
st.plotly_chart(fig, use_container_width=True)

# ---- Sample Reviews ----
st.subheader("💬 Sample User Reviews")
st.dataframe(filtered[['content', 'score', 'sentiment_label']].sample(min(5, len(filtered))), use_container_width=True)


# ---- Footer ----
st.markdown("---")
st.caption("Built with ❤️ by a Data Science Master's student | NLP • ML • Product Strategy")
