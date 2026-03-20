import requests
import pandas as pd
import streamlit as st
from character import Character

class RickAndMortyAPI:
    """
    A class to interface with the Rick and Morty REST API.
    Handles data fetching, pagination, and transformation into tabular formats.
    """

    BASE_URL = "https://rickandmortyapi.com/api/character"

    @st.cache_data
    def get_all_characters(_self):
        """Iterates through every page of the API to fetch all characters."""
        all_characters = []
        url = _self.BASE_URL
        
        while url:
            response = requests.get(url).json()
            results = response.get('results', [])
            
            all_characters.extend([Character(data) for data in results])
            
            url = response.get('info', {}).get('next')
            
        return all_characters


    @staticmethod
    def to_dataframe(characters):
        """Converts a list of Character objects into a Pandas DataFrame."""
        return pd.DataFrame([vars(c) for c in characters])