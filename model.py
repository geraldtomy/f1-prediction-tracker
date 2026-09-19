import pandas as pd

# Placeholder — replace with real Azerbaijan quali results once available
quali_positions = {
    'ANT': 1, 'NOR': 2, 'RUS': 3, 'PIA': 4, 'VER': 5,
    'LEC': 6, 'HAM': 7, 'LAW': 8, 'GAS': 9, 'LIN': 10,
}

# Your actual recent-form data from before
recent_form = {
    'ANT': 1.33, 'NOR': 2.67, 'RUS': 3.33, 'PIA': 6.33, 'LAW': 9.0,
    'VER': 9.0, 'LIN': 9.67, 'GAS': 9.67, 'LEC': 10.33, 'HAM': 10.67,
}

df = pd.DataFrame({
    'Driver': quali_positions.keys(),
    'QualiPosition': quali_positions.values(),
})
df['RecentForm'] = df['Driver'].map(recent_form)

# Simple model: average of grid position and recent form, lower = better predicted finish
df['ModelScore'] = (df['QualiPosition'] + df['RecentForm']) / 2
df = df.sort_values('ModelScore')

print(df)w
