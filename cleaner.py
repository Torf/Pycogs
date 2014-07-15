import discogs_client as discogs

discogs.user_agent = 'TestPyCleaner/0.1 +http://adb.example.com'

s = discogs.Search('azealia banks')

print s
print s.exactresults
