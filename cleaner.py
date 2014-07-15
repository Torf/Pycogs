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
    if len(names) >= 3:
      return names
  
  return names

def SafeArtistSearch(artistName):
  foundArtists = SearchArtistName(artistName)
  
  for foundArtist in foundArtists:
    
    if foundArtist.strip().lower() != artistName.strip().lower():
      stop = False
      
      while not stop:
        entry = raw_input('Is %s the same ? (Y/N) :' % {'current':artistName, 'new':foundArtist})
        if entry.strip().lower() == 'y':
          return foundArtist
        
        if entry.strip().lower() == 'n':
          stop = True
    
    else:
      return foundArtist
      
  return None

def main(args):
  
  requiredRename = []
  
  for dirname in os.listdir("/medias/Musique/"):
    result = SafeArtistSearch(dirname)
    
    if result and result != dirname:
      requiredRename.append({'current':dirname, 'new':result})
      
  
  print requiredRename
      
if __name__ == "__main__":
   main(sys.argv[1:])
  
