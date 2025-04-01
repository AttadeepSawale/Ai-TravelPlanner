import streamlit as st
from utils import get_travel_recommendations, get_travel_tips, get_best_travel_time

def main():
    st.set_page_config(page_title="🌍 AI Trip Guide", layout="wide")

    # Custom CSS for improved styling
    st.markdown("""
        <style>
            .title { font-size: 2.5rem; font-weight: bold; color: #16a085; text-align: center; }
            .subtitle { font-size: 1.3rem; text-align: center; color: #2980b9; }
            .stButton>button { background-color: #d35400 !important; color: white !important; font-size: 1.2rem; border-radius: 8px; }
        </style>
    """, unsafe_allow_html=True)

    # Display Title and Subtitle
    st.markdown("<div class='title'>🌎 AI-Powered Trip Guide</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Explore smarter. Travel stress-free. Get AI-powered trip insights.</div>", unsafe_allow_html=True)

    # User input form for trip planning
    with st.form("trip_form"):
        col1, col2 = st.columns(2)
        with col1:
            source = st.text_input("🌍 **Starting Location**")
        with col2:
            destination = st.text_input("📍 **Destination**")
        submitted = st.form_submit_button("🔍 Get Travel Insights")

    # Handle form submission
    if submitted:
        if source and destination:
            st.success("✨ Generating smart travel insights...")

            travel_info = get_travel_recommendations(source, destination)
            travel_tips = get_travel_tips(destination)
            best_time = get_best_travel_time(destination)

            # Display AI-generated travel recommendations
            st.markdown("### 🗺️ Best Travel Options")
            st.info(travel_info)

            # Display AI-generated travel tips
            st.markdown("### 💡 Useful Travel Tips")
            st.warning(travel_tips)

            # Display AI-generated best time to visit
            st.markdown("### 📅 Best Time to Visit")
            st.success(best_time)

        else:
            st.error("🚨 Please enter both your starting location and destination.")

# Run the Streamlit application
if __name__ == "__main__":
    main()
