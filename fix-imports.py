import os;


class FixImports:


	def __init__(self, projectPath):
		self._projectPath = projectPath;
		self._imports = [];
		self._failedImports = [];


	def read_file(self, file):
		print(file);


	def extract_imports(self):
		print('yet to be implemented');


	def try_import(self):
		print('yet to be implemented');


	def add_to_failed_imports(self):
		print('yet to be implemented');


	def download_libraries(self):
		print('yet to be implemented');


	def fix(self):
		for root, dirs, files in os.walk('.'):
			for file in files:
				if file.endswith('.py'):
					self.read_file(file);



if __name__ == '__main__':
	imports = FixImports('test.py');
	imports.fix();