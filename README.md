# Rick & Morty Universe Explorer

A Streamlit dashboard for exploring characters across the multiverse using the Rick & Morty API.

## Features
Real-time filtering
- Search by name, species and status

Multiverse stats
- Visualises character distribution by origin

Jerry Mode
- A specialised, highly safe interface for the less adventurous

## Setup and Installation
1. Clone the repo
```bash
git clone https://github.com/lukeai-tan/rick-and-morty-dashboard.git
```

2. Install dependencies
```bash
pip install streamlit plotly pandas requests
```

3. Run the app
```bash
streamlit run app.py
```

## Tech Stack
- Frontend: Streamlit
- Data visualisation: Plotly Express
- API: [The Rick and Morty API](https://rickandmortyapi.com/)


## Architecture & Approach
The app follows a functional modular architecture to ensure the UI is decoupled from the data logic:

- `api_manager.py`: A dedicated wrapper class handling all REST API logic, pagination, and conversion to Pandas DataFrames.

- `app.py`: The main entry point, structured into distinct stages:
    - Initialisation: Setting up page configs.
    - Data Layer: Using @st.cache_data to prevent redundant API pings.
    - State Management: Handling sidebar inputs and filtering logic.
    - View Layer: Modular functions (render_visuals, render_table) for a clean UI


## Testing Instructions
### Searching
Type `Morty` in the search bar. The character table should instantly filter to only show all results with the keyword `Morty`.
Type `morty` (lowercase) to check for the case-insensitive logic.

### Filter Logic
Select `Alive` in the Status filter and `Alien` in Species. Verify that the bar chart updates its counts to reflect only living aliens.

### Empty State
Type some gibberish name like `asdamsdhgfkajh`. The app should display the `No characters found` message instead of crashing.

### Jerry Mode
Click the `Jerry mode` button. The screen will clear, balloons appear and the Jerry GIF loads. Click "I'm bored, take me back to Rick" to ensure the app state resets.


## Assumptions & Challenges
### Assumptions
I treated the Rick and Morty character set as static. The application fetches the entire character database once and caches it. This helps to prioritse filtering speed and reduces API overhead, assuming that new characters are not added to the upstream API in real time during a user session.

### Challenges
Pagination loop:
The API doesn't give me all the characters at once. Instead it gives them in chunks of 20. I had to write a `while` loop in my `api_manager` to follow the breadcrumbs until the end is reached.

API Rate Limiting:
To ensure that every user interaction doesn't trigger a new API call, I used `@st.cache_data` on the `get_all_characters` function to take a snapshot of the whole multiverse at once and keep it in memory.



