import subprocess
from subprocess import Popen
from io import StringIO
import sys
import os
import logging


class Apktool:

    def __init__(self,input):
        self.input = input
        self.workspace = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


    @staticmethod
    def execute(command):
        cp = subprocess.run(command,universal_newlines=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        error = cp.stderr
        output = cp.stdout
        returncode = cp.returncode

        #logger1.debug(command)
        logger1.debug(error)
        logger1.debug(output)
        logger1.debug(returncode)

        if returncode == 1:
            return error
        return output

    def fetchApk(self,path):
        package_path = self.getPackagePath()
        command = ["adb","pull",package_path,path]
        value = self.execute(command)
        return value

    def compile(self):
        command = ["java","-jar",self.workspace+"/dependency/apktool.jar","d","-f",self.input]
        value = self.execute(command)
        return value

    def decompile(self):
        command = ["java","-jar",self.workspace+"/dependency/apktool.jar","b","-f",self.input]
        value = self.execute(command)
        return value

    def sign(self):
        command =- ["jarsigner","-verbose","-sigalg","SHA1withRSA","-digestalg","SHA1","-keystore",self.workspace+"/dependency/ssl-key.keystore","-storepass","android","-keypass","android",self.value,"51j0"]
        value = self.execute(command)
        return value
