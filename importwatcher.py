import sys

class ImportWatcher(object):
	def __init__(self):
		"""create a new watcher based on the current sys.modules state"""
		self.modules = sys.modules.copy()
		self.keys = set(self.modules.keys())

	def __contains__(self, item):
		return item in self.keys
	
	def __getitem__(self, item):
		return self.modules[item]

	def restore(self):
		"""
		delete all modules that were loaded after this
		watcher was created.
		Returns a dict of the format module_name: module_object
		containing all deleted modules
		"""
		
		def _del(modname):
			del sys.modules[modname]
		return self._diff(_del)
	
	def diff(self):
		"""
		return the difference between the initial snapshot and the
		currently loaded modules
		"""
		return self._diff()
	
	def _diff(self, callback=None):
		result = {}
		for modname, mod in sys.modules.items():
			if modname not in self:
				result[modname] = mod
				if callback is not None:
					callback(modname)
		return result

