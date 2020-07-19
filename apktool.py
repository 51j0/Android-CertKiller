import subprocess
from subprocess import Popen
from io import StringIO
import sys
import os
import inspect
from logger import logging,config

class Apktool:

    def __init__(self,value):
        self.value = value
        self.workspace = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.logger = logging.getLogger('apktool')

    def execute(self,command):
        print(" ".join(command))
        output = subprocess.run(command,shell=False)
        self.logger.debug(" ".join(command))
        self.logger.debug(output)
        self.logger.debug(output.returncode)
        if output.returncode != 0:
             return "error"
        return "Success"

    def compile(self):
        command = ["java","-jar",config['apktool'],"b","-f",self.value]
        value = self.execute(command)
        return value

    def decompile(self):
        if self.value.endswith('.apk'):
            command = ["java","-jar",config['apktool'],"d","-f",self.value]
            output = self.execute(command)
        else:
            output = "%s doesn't look like a valid APK"%self.value
        return output

    def sign(self):
        if self.value.endswith('.apk'):
            command = ["jarsigner","-verbose","-sigalg","SHA1withRSA","-digestalg","SHA1","-keystore",config['keystore'],"-storepass","android","-keypass","android",self.value,"51j0"]
            output = self.execute(command)
        else:
            output = "%s doesn't look like a valid APK"%self.value
        return output
