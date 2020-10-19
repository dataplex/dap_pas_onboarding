import requests
import json
from .addconjurhostrequestbuilder import AddConjurHostRequestBuilder

class ServicesHelper:
    def __init__(self, config, policyOutputParser):
        self.__config = config
        self.__policyOutputParser = policyOutputParser

    def onboard(self):
        policy_out = self.policy_output_raw()
        hosts_to_onboard = self.__policyOutputParser.hosts(policy_out)
        self.onboard_hosts(hosts_to_onboard)

    def policy_output_raw(self):
       with open(self.__config.policy_out_path) as f:
           return f.read()

    def onboard_hosts(self, hosts_to_onboard):
        if len(hosts_to_onboard) == 0:
            return 0

        creds_from_ccp = self.pas_rest_credentials()
        auth_header = self.pas_rest_authenticate(creds_from_ccp)

        url = f'https://{self.__config.pam_host}/PasswordVault/API/Account'
        headers = { "Content-Type": "application/json", "Authorization": auth_header }

        for conjur_host in hosts_to_onboard:
            add_body = AddConjurHostRequestBuilder(self.__config, conjur_host).build()
            requests.post(url, headers=headers, data=add_body, verify=self.__config.verifySsl)

    def pas_rest_credentials(self):
        r = requests.get(self.__config.ccp_query, verify=self.__config.verifySsl)
        resp_json = r.json()
        return json.dumps({ 'username': resp_json["UserName"], 'password': resp_json["Content"] })

    def pas_rest_authenticate(self, ccp_credentials):
        url = f"https://{self.__config.pam_host}/PasswordVault/API/auth/Cyberark/Logon"

        headers = { "Content-Type": "application/json" }

        response = requests.post(url, data=ccp_credentials, headers=headers, verify=self.__config.verifySsl)
        return response.json()["CyberArkLogonResult"]