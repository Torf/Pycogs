import discogs_client as discogs
import sys

discogs.user_agent = 'Pytest/0.1 +http://ww.abc.fr'

def searchArtistName(foldername):
  print 'Searching artist: %s' % foldername
  
  s = discogs.NewSearch(foldername, 'artist')
  result = s.results()
  
  if len(result) >= 1:
    found = result[0].name
    return found
    
  return None

def SafeArtistSearch(artistName):
  foundArtist = searchArtistName(artistName)
  
  if foundArtist.strip().lower() != artistName.strip().lower():
    while True:
      entry = input('Is "%s" and "%s" the same ? (Y/N) :')
      if entry.trim().lower() == 'y':
        return foundArtist
      
      if entry.trim().lower() == 'n':
        return None
  
  else:
    return foundArtist

def main(args):
  if len(args) < 1:
    print 'help: cleaner.py <artistSearch>'
    return

  print "Final Result: %s" % SafeArtistSearch(args[0])
        

if __name__ == "__main__":
   main(sys.argv[1:])
  
