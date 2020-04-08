import re

class ConfigurationParser:

    deviceConfig = ''

    def readConfig():
        with open('config.cfg', 'r') as config_file:
            deviceConfig = config_file.read()
    #deviceConfig = open('config.cfg', 'r').read()

    @classmethod
    def parseCustomerNames(self):
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, deviceConfig)
        return customerNames
