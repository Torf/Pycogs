
from mutagen.flac import FLAC

class BaseNode(object):

	def __init__(self, parentFolder, nodeName):
		self._parentFolderPath = parentFolder
		if not self._parentFolderPath.endswith("/"):
			self._parentFolderPath += "/"

		self._name = nodeName

	def __str__(self):
		return '<%s "%s">' % (self.__class__.__name__, self.name)

	def __repr__(self):
		return self.__str__().encode('utf-8')

	@property
	def uri(self):
		return "%s%s" % (self._parentFolderPath, self._name)

	@property
	def name(self):
		return self._name

class ArtistFolder(BaseNode):

	def __init__(self, musicFolder, folderName):
		BaseNode.__init__(self, musicFolder, folderName)


class AlbumFolder(BaseNode):

	def __init__(self, artistFolder, folderName):
		self._artistFolder = artistFolder
		BaseNode.__init__(self, artistFolder.uri, folderName)

	def __str__(self):
		return '<%s "%s" (%s)>' % (self.__class__.__name__, self._name, self._artistFolder.name)
	
class MusicFile(BaseNode):

	def __init__(self, albumFolder, fileName):
		BaseNode.__init__(self, albumFolder, fileName)

	def printTags(self):
		audio = FLAC(self.uri)
		audio.pprint()
