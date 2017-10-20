import os;


class FixImports:

	
	_SCRIPT_NAME = 'fix-imports.py';


	def __init__(self, project_path):
		self._project_path = project_path;
		self._imports = [];
		self._failed_imports = [];


	def read_file(self, file_path):
		try:
			file = open(file_path, 'r');
		except FileNotFoundError as error:
			print(error);
			return [];
		return file.readlines();


	def extract_imports(self, file_content):
		imports = [];
		for line_content in file_content:
			line_content = line_content.strip();
			if not line_content.startswith('#'):
				words = line_content.split(' ');
				for index in range(len(words)):
					if words[index] == 'from' or words[index] == 'import':
						index = index + 1;
						while words[index] == '':
							index = index + 1;
						if words[index].endswith(';'):
							imports.append(words[index][:-1]);
						else:
							imports.append(words[index]);
						break;
		return imports;


	def try_imports(self):
		for import_pkg in self._imports:
			try:
				__import__(import_pkg);
			except ImportError as error:
				print(error);
				self._failed_imports.append(import_pkg);


	def download_libraries(self):
		print('yet to be implemented');


	def fix(self):
		for root, dirs, files in os.walk('.'):
			for file in files:
				if file.endswith('.py') and (file != self._SCRIPT_NAME):
					file_content = self.read_file(root + '/' + file);
					for import_pkg in self.extract_imports(file_content):
						if import_pkg not in self._imports:
							self._imports.append(import_pkg);
		self.try_imports();



if __name__ == '__main__':
	imports = FixImports(os.getcwd());
	imports.fix();