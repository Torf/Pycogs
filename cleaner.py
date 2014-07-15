import discogs_client as discogs
import sys
import os

discogs.user_agent = 'Pytest/0.1 +http://ww.abc.fr'

def SearchArtistName(foldername):
  print { "infos": 'Searching artist: %s' % foldername }
  
  s = discogs.NewSearch(foldername, 'artist')
  result = s.results()
  
  names = []
  
  for artist in result:
    names.append(artist.name)
  
  return names

def SafeArtistSearch(artistName):
  foundArtists = SearchArtistName(artistName)
  
  for foundArtist in foundArtists:
    
    if foundArtist.strip().lower() != artistName.strip().lower():
      while True:
        entry = raw_input('Is "%s" (current) and "%s" (new) the same ? (Y/N) :' % (artistName, foundArtist))
        if entry.strip().lower() == 'y':
          return foundArtist
        
        if entry.strip().lower() == 'n':
          continue
    
    else:
      return foundArtist
      
  return None

def main(args):
  
  for dirname in os.listdir("/medias/Musique/"):
    result = SafeArtistSearch(dirname)
    
    if result == None:
      print { "infos": "Artist %s unknown." % dirname }
    
    elif result != dirname:
      print { "infos": "Result %s differes from foldername %s." % (result, dirname) }

if __name__ == "__main__":
   main(sys.argv[1:])
  
