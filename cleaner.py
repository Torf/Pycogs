import discogs_client as discogs

discogs.user_agent = 'Pytest/0.1 +http://ww.abc.fr'

s = discogs.Search('azealia banks')

print s
print s.exactresults
