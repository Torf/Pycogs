
class BaseFolder(object):

	def __init__(self, folderName):
        self._name = folderName

    def __str__(self):
        return '<%s "%s">' % (self.__class__.__name__, self._name)

    def __repr__(self):
        return self.__str__().encode('utf-8')


class ArtistFolder(BaseFolder):

	def __init__(self, folderName):
		BaseFolder.__init__(self, folderName)


class AlbumFolder(BaseFolder):

	def __init__(self, folderName, artistFolder):
		self._artistFolder = artistFolder
		BaseFolder.__init__(self, folderName)

	def __str__(self):
        return '<%s "%s (%s)">' % (self.__class__.__name__, self._name, self._artistFolder)
    
