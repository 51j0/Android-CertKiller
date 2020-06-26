import subprocess
from subprocess import Popen
from io import StringIO
import sys
import os
import inspect
from logger import logging

class Apktool:

    def __init__(self,input):
        self.input = input
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
        return 0

    def compile(self):
        command = ["java","-jar","dependency/apktool.jar","b","-f",self.input]
        value = self.execute(command)
        return value

    def decompile(self):
        command = ["java","-jar","dependency/apktool.jar","d","-f",self.input]
        value = self.execute(command)
        return value

    def sign(self):
        command = ["jarsigner","-verbose","-sigalg","SHA1withRSA","-digestalg","SHA1","-keystore","dependency/ssl-key.keystore","-storepass","android","-keypass","android",self.input,"51j0"]
        value = self.execute(command)
        return value
