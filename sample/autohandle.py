# autohandle.py
#	Provides smart file I/O functionality in both class & function form.
#	credit : https://docs.python-guide.org/writing/structure/#structure-of-the-repository

from contextlib import contextmanager

class autohandler(object) : 
	def __init__( self , filename ) :
		self.file = open(filename)
	def __enter__(self) :
		return self.file
	def __exit__(self,ctx_type,ctx_value,ctx_traceback) :
		self.file = close()

def autohandle( filename ):
	file = open(filename)
	try:
		yield file
	finally:
		file.close()

