import json
from pathlib import Path

import pandas as pd

def load_latest_raw():
    """this function loads the latest raw data from the data/raw directory, 
parses it as JSON, and returns a DataFrame of players and a dictionary of teams."""
    #list files
    latest = sorted(Path("data/raw").glob("bootstrap_*.json"))[-1]
    #take the latest and parse as JSON
    data = json.loads(latest.read_text())
    #build a DataFrame from the "elements" key (players)
    players = pd.DataFrame(data["elements"])
    #build a teams table
    teams = pd.DataFrame(data["teams"])[["id","name"]].set_index("id").to_dict()["name"]
    return players, teams


def select_columns(df, columns):
    """this function selects columns from a DataFrame."""
    return df[columns]
def convert_types(df, column_types):
    for column, dtype in column_types.items():
        df[column] = df[column].astype(dtype)
    return df
def add_labels(df, teams):
    return df.replace
def filter_minutes(df, min_minutes):
    return df[df['minutes'] >= min_minutes]
if __name__ == "__main__":
    players, teams = load_latest_raw()
    print(players.shape)
    print(list(teams.items())[:3])