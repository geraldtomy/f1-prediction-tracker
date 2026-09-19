import fastf1
fastf1.Cache.enable_cache('cache')

quali = fastf1.get_session(2026, 'Spain', 'Q')
quali.load()

print(quali.results[['Position', 'Abbreviation', 'TeamName']])