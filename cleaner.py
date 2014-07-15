import discogs_client as discogs

discogs.user_agent = 'Pytest/0.1 +http://ww.abc.fr'

s = discogs.NewSearch('azealia banks', 'artist')

print s._uri

print s.results()
