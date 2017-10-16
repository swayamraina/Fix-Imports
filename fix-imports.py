class FixImports:

	_projectPath;
	_imports;
	_failedImports;


	def __init__(self, projectPath):
		self._projectPath = projectPath;
		self._imports = [];
		self._failedImports = [];