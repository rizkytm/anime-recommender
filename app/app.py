import streamlit as st
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender")

query = st.text_input("Enter your anime preferences:")
if query:
    with st.spinner("Fetching recommendations..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)