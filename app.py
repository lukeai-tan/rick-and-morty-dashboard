import streamlit as st
import plotly.express as px
from api_manager import RickAndMortyAPI


def init_app():
    st.set_page_config(page_title="Rick & Morty Universe Explorer", layout="wide")
    return RickAndMortyAPI()


@st.cache_data
def load_data(_api_instance):
    """Fetches data and converts to DF. Cached to save API hits."""
    all_characters = _api_instance.get_all_characters()
    return _api_instance.to_dataframe(all_characters)


def render_sidebar(df):
    st.sidebar.header("Search & Filters")
    
    search = st.sidebar.text_input("Search Character Name", "")
    
    statuses = sorted(df['status'].unique())
    species = sorted(df['species'].unique())
    
    selected_status = st.sidebar.multiselect("Status", statuses, default=statuses)
    selected_species = st.sidebar.multiselect("Species", species, default=species)
    
    return search, selected_status, selected_species


def filter_data(df, search, statuses, species):
    """
    Filters the character DataFrame based on user input.
    """

    return df[
        (df['name'].str.contains(search, case=False)) &
        (df['status'].isin(statuses)) &
        (df['species'].isin(species))
    ]


def render_visuals(df):
    st.subheader("Origin Universe Distribution")
    if not df.empty:
        counts = df['origin'].value_counts().reset_index()
        fig = px.bar(counts, x='origin', y='count', labels={'count': 'Count'})
        st.plotly_chart(fig, width='stretch')
    else:
        st.warning("No characters found with those filters.")


def render_table(df):
    st.subheader("Characters")
    cols = ['name', 'species', 'status', 'origin', 'current']
    st.dataframe(df[cols], width='stretch')

def apply_jerry_mode():
    st.sidebar.markdown("---")
    if st.sidebar.button("Jerry Mode"):
        st.balloons()
        
        st.empty()
        st.title("JERRY-FRIENDLY INTERFACE")
        st.subheader("Don't touch anything. Just look at the nice colors.")
        
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2RpdjlnaW9leXc5bzU3d2E2OWg2ZTR6MmRqbHFodmF0Z25vNWRwcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VsGwZzPlmmpR3AY2PP/giphy.gif", caption="Life is effortless!")
        
        if st.button("I'm bored, take me back to Rick"):
            st.rerun()
            
        st.stop()


def main():
    api = init_app()
    
    with st.spinner('Accessing the Citadel of Ricks...'):
        df = load_data(api)

    search, selected_status, selected_species = render_sidebar(df)

    apply_jerry_mode()

    filtered_df = filter_data(df, search, selected_status, selected_species)
    
    st.title("Rick & Morty Universe Explorer")
    render_visuals(filtered_df)
    render_table(filtered_df)


if __name__ == "__main__":
    main()