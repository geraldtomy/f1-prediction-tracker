import fastf1
import pandas as pd

fastf1.Cache.enable_cache('cache')

races = ['Netherlands', 'Italy', 'Spain']  # last few completed races
all_results = []

for race in races:
    session = fastf1.get_session(2026, race, 'R')
    session.load()
    results = session.results[['Abbreviation', 'Position']].copy()
    results['Race'] = race
    all_results.append(results)

combined = pd.concat(all_results)
avg_form = combined.groupby('Abbreviation')['Position'].mean().sort_values()

print(avg_form)