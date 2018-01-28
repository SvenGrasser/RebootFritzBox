import time
import os
import yaml;

class Property:
    propertyFile = 'rebootFritzBox.properties.yml'
    iRunning = False
    executeReboot = False
    rebootTime = ''
    password = ''
    def __init__(self):
        properties_path = os.path.dirname(os.path.realpath(__file__))
        properties_fullpath = os.path.join(properties_path, self.propertyFile)
        with open(properties_fullpath, 'r') as properties_file:
            prop = yaml.load(properties_file)
            self.isRunning = prop['options']['isRunning']   
            self.executeReboot = prop['options']['executeReboot']     
            self.rebootTime = prop['options']['reboot']    
            self.password = prop['authentication']['password']

def isRebootTime(p):
    now = time.strftime('%H:%M')
    print ('check RebootTime: ', now)
    if now == p.rebootTime:
        return True
    else:
        return False

def reboot(p):
    print ('reboot FritzBox: ', time.strftime('%X %x'))
    if p.executeReboot == True:
        from fritzconnection import FritzConnection
        connection = FritzConnection(password=p.password)
        connection.call_action('DeviceConfig', 'Reboot')

def run():
    print('reboot FritzBox: service is running')  
    
    p = Property()
    while p.isRunning == True:
        if isRebootTime(p):
            reboot(p)
        time.sleep(60)

run()
