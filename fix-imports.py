import os;


class FixImports:

	
	_SCRIPT_NAME = 'fix-imports.py';


	def __init__(self, project_path):
		self._project_path = project_path;
		self._files = [];
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
						pkg = words[index].split('.')[0];
						if len(pkg) > 0:
							if pkg.endswith(';'):
								imports.append(pkg[:-1]);
							else:
								imports.append(pkg);
						break;
		return imports;


	def remove_local_packages(self):
		for file in self._files:
			if file in self._imports:
				self._imports.remove(file);


	def try_imports(self):
		for import_pkg in self._imports:
			try:
				__import__(import_pkg);
			except ImportError as error:
				print(error);
				self._failed_imports.append(import_pkg);


	def download_libraries(self):
		try:
			import pip;
		except ImportError as error:
			print(error);
			return ;
		for import_pkg in self._failed_imports:
			try:
				pip.main(['install',import_pkg,'--user']);
			except SystemExit as error:
				print(error);


	def fix(self):
		for root, dirs, files in os.walk(self._project_path):
			for file in files:
				if file.strip().endswith('.py') and (file != self._SCRIPT_NAME):
					self._files.append(file.strip()[:-3]);
					file_content = self.read_file(root + '/' + file);
					for import_pkg in self.extract_imports(file_content):
						if import_pkg not in self._imports:
							self._imports.append(import_pkg);
		self.remove_local_packages();
		self.try_imports();
		self.download_libraries();



if __name__ == '__main__':
	imports = FixImports(os.getcwd());
	imports.fix();