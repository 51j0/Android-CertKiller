import logging
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='certkiller.log',
                    filemode='w')


console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


if(os.path.isfile('dependency/apktool.jar')):
    abspath = os.getcwd()
elif (os.path.isfile('/usr/bin/andi')):
    abspath = os.readlink("/usr/bin/andi")[:-5]
else:
    abspath = ''



config['apktool'] = abspath + 'dependency/apktool.jar'
config['keystore'] = abspath + 'dependency/ssl-key.keystore'

#with open('config.json', 'r') as f:
#    config = json.load(f)
