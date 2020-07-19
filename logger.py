import logging
import os

config = {
  "apktool": "dependency/apktool.jar",
  "adb":"adb",
  "keystore": "dependency/ssl-key.keystore",
  "network": "dependency/networkSecurityConfig.xml",
}

if(os.path.isfile('dependency/apktool.jar')):
    abspath = os.getcwd()+"/"
    config['apktool'] = abspath + "dependency/apktool.jar"
    config['keystore'] = abspath + "dependency/ssl-key.keystore"
    config['network'] = abspath + "dependency/networkSecurityConfig.xml"
elif (os.path.isfile('/usr/bin/andi')):
    abspath = os.readlink("/usr/bin/andi")[:-4]
    config['apktool'] = abspath + "dependency/apktool.jar"
    config['keystore'] = abspath + "dependency/ssl-key.keystore"
    config['network'] = abspath + "dependency/networkSecurityConfig.xml"



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=abspath+'/certkiller.log',
                    filemode='w')


console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)



#with open('config.json', 'r') as f:
#    config = json.load(f)
