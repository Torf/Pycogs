
class BaseFolder(object):

	def __init__(self, musicFolder, folderName):
		self._musicFolderPath = musicFolder
		if not self._musicFolderPath.endswith("/"):
     		self._musicFolderPath += "/"

        self._name = folderName

    def __str__(self):
        return '<%s "%s">' % (self.__class__.__name__, self.name)

    def __repr__(self):
        return self.__str__().encode('utf-8')

	@property
	def uri():
		return "%s%s" % (self._musicFolderPath, self._name)

	@property
	def name():
		return self._name

class ArtistFolder(BaseFolder):

	def __init__(self, folderName):
		BaseFolder.__init__(self, folderName)


class AlbumFolder(BaseFolder):

	def __init__(self, folderName, artistFolder):
		self._artistFolder = artistFolder
		BaseFolder.__init__(self, folderName)

	def __str__(self):
        return '<%s "%s (%s)">' % (self.__class__.__name__, self._name, self._artistFolder.name)

     @property
     def uri():
     	return "%s%s/%s" % (self._musicFolderPath, artistFolder.name, self._name)
