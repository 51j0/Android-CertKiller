import sys, getopt, inspect, os, subprocess, re


def ifTestOnlyAPK(file):

    val = True;
    f=open(file, "r")
    if f.mode != 'r':
        print 'Something went wrong'
        sys.exit(2)

    contents = f.read()
    if "android:testOnly" not in contents:
        val = False;
    f.close()
    return val

def mainfestdebuggable():
    print 'I: Setting android:debuggable flag to true'
    f=open("base/AndroidManifest.xml", "r")
    if f.mode != 'r':
        print 'Something went wrong'
        sys.exit(2)
    contents = f.read()
    if "android:debuggable" not in contents:
        contents = contents.replace("<application", "<application android:debuggable=\"true\"")
    elif "android:debuggable=\"false\"" in contents:
        contents = contents.replace("android:debuggable=\"false\"", "android:debuggable=\"true\"")
    f.close()
    f=open("base/AndroidManifest.xml", "w+")
    f.write(contents)
    f.close()
    print '   complete'
    print '------------------------------'


def usercertificate():
    print 'I: Applying SSL bypass'
    f=open("base/AndroidManifest.xml", "r")
    if f.mode != 'r':
        print 'Something went wrong'
        sys.exit(2)
    contents = f.read()
    if "android:networkSecurityConfig" not in contents:
        contents = contents.replace("<application", "<application android:networkSecurityConfig=\"@xml/networkSecurityConfig\"")
    else:
        result = re.sub('android:networkSecurityConfig="(.*?)"',  'android:networkSecurityConfig="@xml/networkSecurityConfig"',    contents)
        contents = result
        #print(result)
    f.close()
    f=open("base/AndroidManifest.xml", "w+")
    f.write(contents)
    f.close()
    createConfigFile()
    print '   complete'
    print '------------------------------'

def createConfigFile():
    dirName = "base/res/xml"
    if not os.path.exists("base/res/xml"):
        os.mkdir(dirName)
        print("I: Directory '"+dirName+"' Created")

    f=open("dependency/networkSecurityConfig.xml", "r")
    contents = f.read()
    f.close()
    f=open("base/res/xml/networkSecurityConfig.xml", "w+")
    f.write(contents)
    f.close()


def main(argv):
    mainfestdebuggable()
    usercertificate()

if __name__ == "__main__":
   main(sys.argv[1:])
