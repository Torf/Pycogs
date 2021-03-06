import os
from mutagen.flac import FLAC

class BaseNode(object):

	def __init__(self, parentFolder, nodeName):
		self._parentFolderPath = parentFolder
		if not self._parentFolderPath.endswith("/"):
			self._parentFolderPath += "/"

		self._isDir = False
		self._name = nodeName

	def __str__(self):
		return '<%s "%s">' % (self.__class__.__name__, self.name)

	def __repr__(self):
		return self.__str__().encode('utf-8')

	@property
	def uri(self):
		return "%s%s%s" % (self._parentFolderPath, self._name, ("/" if self._isDir else ""))

	@property
	def name(self):
		return self._name

class ArtistFolder(BaseNode):

	def __init__(self, musicFolder, folderName):
		BaseNode.__init__(self, musicFolder, folderName)
		self._isDir = True


class AlbumFolder(BaseNode):

	def __init__(self, artistFolder, folderName):
		self._artistFolder = artistFolder
		BaseNode.__init__(self, artistFolder.uri, folderName)
		self._isDir = True

	def __str__(self):
		return '<%s "%s" (%s)>' % (self.__class__.__name__, self._name, self._artistFolder.name)
	
class MusicFile(BaseNode):

	def __init__(self, albumFolder, fileName):
		BaseNode.__init__(self, albumFolder.uri, fileName)
		
		if fileName.endswith(".flac") and not os.path.isdir(self.uri):
			self._tags = self._loadTags()

	def _loadTags(self):
		try:
			audio = FLAC()
			audio.load(self.uri)
			return audio.tags
		except Exception, e:
			return None

	@property
	def tags(self):
		return self._tags

