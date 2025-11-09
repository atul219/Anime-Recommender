import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommnder",layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime prefernces eg. : light hearted anime with school settings")
# placeholder for results
output_placeholder = st.empty()
if query:
    with st.spinner("Fetching recommendations for you..."):
        response = pipeline.recommend(query)
        output_placeholder.empty()  # clear old output
        output_placeholder.markdown("### Recommendations")
        output_placeholder.write(response)
else:
    output_placeholder.empty()