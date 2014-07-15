import discogs_client as discogs

discogs.user_agent = 'Pytest/0.1 +http://ww.abc.fr'

def searchArtistName(foldername):
  s = discogs.NewSearch(foldername, 'artist')
  result = s.results()
  
  if len(result) >= 1:
    return result[0].name
    
  return None


print searchArtistName('azealia banks')


