import fastf1

fastf1.Cache.enable_cache('cache')  # speeds up repeated requests

session = fastf1.get_session(2026, 'Spain', 'R')
session.load()

print(session.results[['Position', 'Abbreviation', 'TeamName']].head(10))