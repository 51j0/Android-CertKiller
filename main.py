#/Volumes/InfinityStone/Reality/Projects/tools
#!/usr/bin/python
import sys, getopt, inspect, os, subprocess, re, time
from codetamper import mainfestdebuggable
from codetamper import usercertificate

millis              = str(int(round(time.time() * 1000)))
AUTOMATION          = 1
MANNUAL             = 2
verbose             = False
debuggable_mode     = False

def myworkspace():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def myCommand_silent(command):
    #global verbose
    if verbose == False:
        FNULL = open(os.devnull, 'w')
        process = subprocess.call(command, shell=True,stdout=FNULL, stderr=subprocess.STDOUT)
    else:
        print (command)
        process = subprocess.call(command, shell=True)
        print '------------------------------'



def myCommand(text,command,second):
    print text
    #global verbose
    if verbose == False:
        FNULL = open(os.devnull, 'w')
        process = subprocess.call(command, shell=True,stdout=FNULL, stderr=subprocess.STDOUT)
    else:
        print '------------------------------'
        process = subprocess.call(command, shell=True)
        print '*******************************'
    print second
    print '------------------------------'

def terminate(var):
    print var
    sys.exit(2)

def intro(var):
    print '\n***************************************'
    print 'Android CertKiller (v0.1)'
    print '***************************************\n'
    print var
    print '---------------------------------'



def getRealPackageName(package_name):
    #SEARCHING FOR PACKAGE

    command = "adb shell pm list packages -f "+package_name
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    orginal_package_name = output[0]
    counts = orginal_package_name.count('\n')

    if counts > 1:
        print orginal_package_name
        print "\n---------------------------------------"
        print "Found "+str(counts)+" packages"
        text = raw_input("Enter the correct package name: ")
        if text == '':
            terminate("Ending script")
        else:
            orginal_package_name = getRealPackageName(text);
    elif counts == 0:
        print "\n---------------------------------------"
        text = raw_input("No application found with the given package name.\nEnter a correct package name: ")
        if text == '':
            terminate("Ending script")
        else:
            orginal_package_name = getRealPackageName(text);


    start_index = 8
    final_index = orginal_package_name.rfind('=')
    package_path = orginal_package_name[start_index:final_index]
    package_path = package_path.replace("\n", "")
    package_path = package_path.replace("\r", "")
    return package_path;

def runwizard():
    intro('CertKiller Wizard Mode')
    os.system("adb devices")
    os.system("echo '---------------------------------\n'")
    package_name = raw_input("Enter Application Package Name: ")
    package_name = getRealPackageName(package_name)
    os.system("echo '\nPackage: "+package_name+"\n'")
    extracting(package_name,'A')
    decompileApplication()
    if debuggable_mode == True:
        mainfestdebuggable()
    usercertificate()
    compileApplication()
    signApplication("base/dist/base.apk",1)
    installApplication()
    sys.exit(2)

def extracting(package_name,workspace):
    first   = '1. Intitaing APK extraction from device'
    second  = '   complete'
    command = "adb pull "+package_name
    myCommand(first,command,second)


def decompileApplication():
    first   = '2. Decompiling'
    second  = '   complete'
    command = "java -jar "+myworkspace()+"/dependency/apktool.jar d -f base.apk"
    myCommand(first,command,second)


def compileApplication():
    first   = '4. Building New APK'
    second  = '   complete'
    command = "java -jar "+myworkspace()+"/dependency/apktool.jar b -f base"
    myCommand(first,command,second)

def signApplication(path,mode):
    global millis
    first   = '5. Sigining APK'
    second  = '   complete'
    command = "jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore dependency/ssl-key.keystore -storepass android -keypass android "+path+" 51j0"
    myCommand(first,command,second)

    f=open("base/AndroidManifest.xml", "r")
    contents = f.read()
    package = re.findall('package="(.*?)"', contents)
    f.close()


    if mode == AUTOMATION:
        print
        command = 'mkdir unpinnedapk/'+package[0]+millis+'/'
        myCommand_silent(command)
        command = 'mkdir workspace/'+package[0]+millis+'/'
        myCommand_silent(command)
        command = "mv -f base/dist/base.apk unpinnedapk/"+package[0]+millis+"/base.apk"
        myCommand_silent(command)
        command = "mv -f base workspace/"+package[0]+millis+"/"
        myCommand_silent(command)
        command = "mv -f base.apk workspace/"+package[0]+millis+"/base.apk"
        myCommand_silent(command)
        text = raw_input("Would you like to install the APK on your device(y/N): ")
        if text == 'y' or text == "Y":
            installApplication(package[0])
        else:
            terminate("Thank you")


def installApplication(package):
    global millis
    print '------------------------------------\n Installing Unpinned APK'
    command = "adb shell pm list packages | grep "+package
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    orginal_package_name = output[0]
    counts = orginal_package_name.count('\n')
    if counts == 1:
        command = "adb uninstall "+package
        myCommand_silent(command)
    command = "adb install unpinnedapk/"+package+millis+"/base.apk"
    myCommand_silent(command)
    print '------------------------------'
    print 'Finished'
    sys.exit(2)

def usage():
    print ''
    print 'root$ python main.py -w (Wizard Mode)'
    print 'root$ python main.py -p /destop/base.apk  (Manual Mode)'
    print ''
    print  '\r -w  --wizard\t        Extract APK From device'
    print  '\r -v  --verbose\t        Verbose Mode'
    print  '\r -p  --Path\t        APK path'
    print  '\r -d  --debuggable mode\tSettng androd:debuggable flag to true'
    print ''

def main(argv):
    global verbose
    global debuggable_mode
    path = ''
    wizard = True
    output_folder = 'A'
    try:
        opts, args = getopt.getopt(argv,"hvdwp:",["help","path=","verbose","debuggable-mode","wizard"])
    except getopt.GetoptError as err:
        usage()
        print (err)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(2)
        elif opt in ("-w", "--Wizard"):
            wizard = True
        elif opt in ("-p", "--path"):
            path = arg
            wizard = False
        elif opt in ("-v", "--verbose", "v"):
            verbose = True
        elif opt in ("-d", "--debuggable-mode", "d"):
            debuggable_mode = True


    if(len(opts) == 0):
        print "\nRunning in default mode:\n"
        runwizard()


    if wizard == True :
        runwizard()
    else:
        intro('CertKiller Mannual Mode')
        command = "cp "+path+" ."
        myCommand_silent(command)
        decompileApplication()
        usercertificate()
        compileApplication()
        signApplication("base/dist/base.apk",1)
        installApplication()
        sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])
