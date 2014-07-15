import discogs_client as discogs
import sys

discogs.user_agent = 'Pytest/0.1 +http://ww.abc.fr'

def searchArtistName(foldername):
  print 'Searching artist %s' % foldername
  
  s = discogs.NewSearch(foldername, 'artist')
  result = s.results()
  
  if len(result) >= 1:
    return result[0].name
    
  return None

def main(args):
  if len(args) < 1:
    print 'help: cleaner.py <artistSearch>'
    return

  print searchArtistName(args[0])


if __name__ == "__main__":
   main(sys.argv[1:])
  
