import discogs_client as discogs
import sys
import os

discogs.user_agent = 'Pytest/0.1 +http://ww.abc.fr'

toAsk = []

def SearchArtistName(foldername):
  print { "infos": 'Searching artist: %s' % foldername }
  
  s = discogs.NewSearch(foldername, 'artist')
  result = s.results()
  
  names = []
  
  for artist in result:
    if artist.name.strip().lower() == foldername.strip().lower():
      names.insert(0, artist.name)
    elif len(names) < 3:
      names.append(artist.name)
  
  return names

def SafeArtistSearch(artistName):
  foundArtists = SearchArtistName(artistName)
  
  haveToAsk = False
  resultArtist = None
  
  for foundArtist in foundArtists:
    
    if foundArtist.strip().lower() != artistName.strip().lower():
      haveToAsk = True
    else:
      resultArtist = foundArtist
    
    break
      
  if haveToAsk:
    toAsk.append({'current':artistName, 'results':foundArtists})
    return None
  
  return resultArtist


def Ask(question):
  
  for foundArtist in question['results']:
    stop = False

    while not stop:
      entry = raw_input('Is %s the same ? (Y/N) :' % {'current':question['current'], 'new':foundArtist})
      if entry.strip().lower() == 'y':
        return foundArtist
        stop = True
  
      elif entry.strip().lower() == 'n':
        stop = True
    
  return None


def main(args):
  
  toAsk = []
  requiredRename = []
  notFound = []
  
  for dirname in os.listdir("/medias/Musique/"):
    result = SafeArtistSearch(dirname)
    
    if not result:
      notFound.append({ 'name': dirname })
    
    elif result != dirname:
      requiredRename.append({'current':dirname, 'new':result})
  
  
  for question in toAsk:
    r = Ask(question)
    
    if r and r != toAsk['current']:
      requiredRename.append({'current':toAsk['current'], 'new':r})
  
  
  print requiredRename
  
  print "Not Found: %s" % notFound
      
if __name__ == "__main__":
   main(sys.argv[1:])
  
