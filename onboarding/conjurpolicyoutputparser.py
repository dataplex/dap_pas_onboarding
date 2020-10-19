import json
from .conjurrole import ConjurRole

class ConjurPolicyOutputParser:
    def hosts(self, policy_output):
        dap_hosts = []
        if not policy_output:
            return dap_hosts

        policy_json = json.loads(policy_output)
        for created_role in policy_json["created_roles"]:
            crole = policy_json["created_roles"][created_role]
            api_key = crole["api_key"]

            crolesplit = crole["id"].split(':')
            cr_acct = crolesplit[0]
            cr_type = crolesplit[1]
            cr_name = crolesplit[2]

            if cr_type == "host":
                dap_hosts.append(ConjurRole(cr_acct, cr_type, cr_name, api_key))

        return dap_hosts
