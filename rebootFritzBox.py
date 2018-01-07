import time
import os
import yaml;

properties = 'rebootFritzBox.properties.yml'
timerTick = 60
rebootTime = '16:50'
isRunning = True
executeReboot = True

def isRebootTime():
    now = time.strftime('%H:%M')
    print ('check RebootTime: ', now)
    if now == rebootTime:
        return True
    else:
        return False

def getPassword():
    properties_path = os.path.dirname(os.path.realpath(__file__))
    properties_fullpath = os.path.join(properties_path, properties)
    with open(properties_fullpath, 'r') as properties_file:
        prop = yaml.load(properties_file)    
        return prop['authentification']['password']
    return ''

def reboot():
    print ('reboot FritzBox: ', time.strftime('%X %x'))
    pw = getPassword()
    if executeReboot == True:
        from fritzconnection import FritzConnection
        connection = FritzConnection(password=pw)
        connection.call_action('DeviceConfig', 'Reboot')
    return;

def run():
    print('reboot FritzBox: service is running')
    while isRunning == True:
        if isRebootTime():
            reboot()
        time.sleep(timerTick)

run()
