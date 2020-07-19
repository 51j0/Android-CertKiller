import sys
import re
import os
from logger import logging,config

class Bypass:

    def __init__(self,input):
        self.input = input
        self.logger = logging.getLogger('adb')

    def udpateNetworkSecurityConfig(self):
        print("I: Searching AndroidManifest")
        if(self.validFolder()):
            print("I: Updating AndroidManifest")
            f=open(self.input+"/AndroidManifest.xml", "r")
            contents = f.read()
            if "android:networkSecurityConfig" not in contents:
                contents = contents.replace("<application", "<application android:networkSecurityConfig=\"@xml/networkSecurityConfig\"")
            else:
                result = re.sub('android:networkSecurityConfig="(.*?)"',  'android:networkSecurityConfig="@xml/networkSecurityConfig"',    contents)
                contents = result
            f.close()
            f=open(self.input+"/AndroidManifest.xml", "w+")
            f.write(contents)
            f.close()
            print("I: AndroidManifest Updated")

            dirName = self.input+"/res/xml"
            if not os.path.exists(dirName):
                os.mkdir(dirName)

            print("I: Updating networkSecurityConfig")
            f=open(config['network'], "r")
            contents = f.read()
            f.close()
            f=open(self.input+"/res/xml/networkSecurityConfig.xml", "w+")
            f.write(contents)
            f.close()
            print("I: Complete")

    def mainfestdebuggable(self):
        print("I: Searching AndroidManifest")
        if(self.validFolder()):
            print("I: Updating AndroidManifest")
            f=open(self.input+"/AndroidManifest.xml", "r")
            contents = f.read()
            if "android:debuggable" not in contents:
                contents = contents.replace("<application", "<application android:debuggable=\"true\"")
            elif "android:debuggable=\"false\"" in contents:
                contents = contents.replace("android:debuggable=\"false\"", "android:debuggable=\"true\"")
            f.close()
            f=open(self.input+"base/AndroidManifest.xml", "w+")
            print("I: AndroidManifest Updated")
            print("I: android:debuggable flag added")
            f.write(contents)
            f.close()

    def validFolder(self):
        f=open(self.input+"/AndroidManifest.xml", "r")
        if f.mode != 'r':
            print("Error l100000x.2")
            return False
        f.close()
        return True
