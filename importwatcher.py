import sys

class ImportWatcher(object):
	def __init__(self):
		self.modules = {}
		self.keys = set()
	
	def save(self):
		self.modules = sys.modules.copy()
		self.keys = set(self.modules.keys())

	@classmethod
	def save_state(cls):
		instance = cls()
		instance.save()
		return instance
	
	def __contains__(self, item):
		return item in self.keys
	
	def __getitem__(self, item):
		print "\n".join(sorted(self.keys))
		print self.diff()
		return self.modules[item]

	def restore(self):
		def _del(modname):
			del sys.modules[modname]
		return self._diff(_del)
	
	def diff(self):
		return self._diff()
	
	def _diff(self, callback=None):
		result = {}
		for modname, mod in sys.modules.items():
			if modname not in self:
				result[modname] = mod
				if callback is not None:
					callback(modname)
		return result

