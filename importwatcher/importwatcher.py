# Copyright (c) 2009, Tim Cuthbertson 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#     * Neither the name of the organisation nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
# AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
# WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

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

