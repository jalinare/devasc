import re


class ConfigurationParser:

    def __init__(self):
        self.deviceConfig = ''
        self.readConfig('config.cfg')

    def readConfig(self, stream):
        with open(stream, 'r') as config_file:
            self.deviceConfig = config_file.read()

    def parseCustomerNames(self):
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        return customerNames
