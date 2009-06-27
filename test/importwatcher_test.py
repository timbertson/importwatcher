from unittest import TestCase
import os, sys
from importwatcher import ImportWatcher

def add_fixture_path():
	fixture_path = 'fixtures'
	full_fixture_path = os.path.join(os.path.dirname(__file__), fixture_path)
	if full_fixture_path not in sys.path:
		sys.path.append(full_fixture_path)
		print sys.path[-1]

class ImportWatcherTest(TestCase):
	def setUp(self):
		add_fixture_path()
		self.initial_state = ImportWatcher()
	
	def tearDown(self):
		self.initial_state.restore()
		
	def test_should_save_initial_import_list(self):
		import md5
		state = ImportWatcher()
		self.assertTrue('md5' in state)
		import fixture1
		self.assertFalse('fixture1' in state)
	
	def test_should_restore_import_list(self):
		self.assertFalse(imported('fixture2'))
		import fixture2
		self.initial_state.restore()
		self.assertFalse(imported('fixture2'))
	
	def test_should_return_the_difference_between_saved_and_current_state(self):
		import fixture3
		import fixture2
		diff = self.initial_state.diff()
		self.assertEqual(diff, {'fixture2':fixture2, 'fixture3':fixture3})
	
	def test_should_return_the_difference_when_restoring_states(self):
		import fixture3
		import fixture2
		diff = self.initial_state.restore()
		self.assertEqual(diff, {'fixture2':fixture2, 'fixture3':fixture3})
	
	def test_should_not_include_nested_but_unimported_modules(self):
		import nested
		print nested.__path__
		state = ImportWatcher()
		self.assertRaises(AttributeError, lambda: nested.unimported)
		self.assertTrue('nested' in state)
		self.assertTrue('nested.imported' in state)
		self.assertFalse('nested.unimported' in state)
	
	def test_should_include_dynamically_loaded_modules(self):
		__import__('fixture1')
		state = ImportWatcher()
		self.assertTrue('fixture1' in state)
	
def imported(modname):
	return modname in sys.modules

