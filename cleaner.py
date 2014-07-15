import discogs_client as discogs
import sys
import os

discogs.user_agent = 'Pytest/0.1 +http://ww.abc.fr'

def SearchArtistName(foldername):
  print 'Searching artist: %s' % foldername
  
  s = discogs.NewSearch(foldername, 'artist')
  result = s.results()
  
  if len(result) >= 1:
    found = result[0].name
    return found
    
  return None

def SafeArtistSearch(artistName):
  foundArtist = SearchArtistName(artistName)
  
  if foundArtist.strip().lower() != artistName.strip().lower():
    while True:
      entry = raw_input('Is "%s" (current) and "%s" (new) the same ? (Y/N) :' % (artistName, foundArtist))
      if entry.strip().lower() == 'y':
        return foundArtist
      
      if entry.strip().lower() == 'n':
        return None
  
  else:
    return foundArtist

def main(args):
  if len(args) < 1:
    print 'help: cleaner.py <artistSearch>'
    return

  for dirname in os.listdir("/medias/Musique/"):
    result = SafeArtistSearch(dirname)
    
    if result == None:
      print "Artist %s unknown." % dirname
    
    if result != dirname:
      print "Result %s differes from foldername %s." % (result, dirname)

if __name__ == "__main__":
   main(sys.argv[1:])
  
