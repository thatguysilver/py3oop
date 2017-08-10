#! usr/bin/python3.6

import os
import shutil
import zipfile
from pathlib import Path

class ZipProcessor:
    def __init__(self, zipname):
        'Initializes by creating a zipname var and a temp dir'
        self.zipname = zipname
        self.temp_directory = Path(f'unzipped - {zipnamae[:-4]}')

        def process_zip(self):
            'Calls the functions that do the work'
            self.unzip_files()
            self.process_files()
            self.zip_files()

        def unzip_files(self):
            'Extracts the zip to the temporary directory'
            self.temp_directory.mkdir()
            with zipfile.ZipFile(self.zipname) as zip:
                zip.extractall(str(self.temp_directory))

        def zip_files(self):
            'Re-zips files.'
            with zipfile.ZipFile(self.zipname, 'w') as file:
                for filename in self.temp_directory.iterdir():
                    file.write(str(filename), filename.name)
            shutil.rmtree(str(self.temp_directory))



                
