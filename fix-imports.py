import os;


class FixImports:

	
	_SCRIPT_NAME = 'fix-imports.py';


	def __init__(self, projectPath):
		self._projectPath = projectPath;
		self._imports = [];
		self._failedImports = [];


	def read_file(self, file_path):
		try:
			file = open(file_path, 'r');
		except FileNotFoundError as error:
			print(error);
			return [];
		return file.readlines();


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
				if file.endswith('.py') and (file != self._SCRIPT_NAME):
					content = self.read_file(root + '/' + file);



if __name__ == '__main__':
	imports = FixImports('');
	imports.fix();