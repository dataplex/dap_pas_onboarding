import configparser
import os

class OnboardingConfig:
    def __init__(self, config_file, config_env, ccp_query = '', policy_out_path = ''):
        cp = configparser.ConfigParser()
        cp.read(config_file)
        config = cp[config_env]

        self.verifySsl = config['verifySsl']
        self.__account = config['account']
        self.__dapmaster = config['dap_master']
        self.__pamhost = config['pam_host']
        self.__platform_id = config['platform_id']
        self.automatic_management_enabled = config['automaticManagementEnabled']
        self.__ccp_query = ccp_query
        self.__policy_out_path = policy_out_path

    @property
    def verifySsl(self):
        return self.__verifySsl

    @verifySsl.setter
    def verifySsl(self, var):
        if var.lower() == 'yes':
            self.__verifySsl = True
        else:
            self.__verifySsl = False

    @property
    def account(self):
        return self.__account

    @property
    def dap_master(self):
        return self.__dapmaster

    @property
    def pam_host(self):
        return self.__pamhost

    @property
    def platform_id(self):
        return self.__platform_id

    @property
    def automatic_management_enabled(self):
        return self.__automgmtenabled

    @automatic_management_enabled.setter
    def automatic_management_enabled(self, var):
        if var.lower() == 'yes':
            self.__automgmtenabled = True
        else:
            self.__automgmtenabled = False

    @property
    def ccp_query(self):
        return self.__ccp_query

    @property
    def policy_out_path(self):
        return self.__policy_out_path