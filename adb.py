import subprocess
from subprocess import Popen
from logger import logging
from io import StringIO
import sys
import os

class Adb:

    def __init__(self,value):
        self.value = value
        self.logger = logging.getLogger('adb')

    def execute(self,command):
        cp = subprocess.run(command,universal_newlines=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        error = cp.stderr
        output = cp.stdout
        returncode = cp.returncode

        #logger1.debug(command)
        self.logger.debug(error)
        self.logger.debug(output)
        self.logger.debug(returncode)

        if returncode == 1:
            return error
        return output

    def packagename(self):
        command = ["adb","shell","pm","list","package","-f",self.value]
        value = self.execute(command)
        start_index = value.rfind('base.apk=')+9
        final_index = len(value)
        package = value[start_index:final_index]
        package = package.replace("\n", "").replace("\r", "")
        return package

    def getPackagePath(self):
        command = ["adb","shell","pm","list","package","-f",self.value]
        value = self.execute(command)
        start_index = 8
        final_index = value.rfind('base.apk=')+8
        package_path = value[start_index:final_index]
        package_path = package_path.replace("\n", "").replace("\r", "")
        return package_path

    def inputext(self):
        command = ["adb","shell","input","text",self.value]
        self.execute(command)

    def fetchApk(self,path):
        package_path = self.getPackagePath()
        command = ["adb","pull",package_path,path]
        value = self.execute(command)
        return value

    def uninstall(self):
        packagename = self.packagename()
        if(packagename != ''):
            text = input("Would you like to uninstall %s from your device (y/N): "%packagename)
            if text == 'y' or text == "Y":
                command = ["adb","uninstall",packagename]
                value = self.execute(command)
            else:
                sys.exit(2)
        else:
            print("Error couldn't find any package")
        return value

    def install(self):
        if self.value.endswith('.apk'):
            command = command = ["adb","install",self.value]
            value = self.execute(command)
        else:
            value = "%s doesn't look like a valid APK"%value
        return value
