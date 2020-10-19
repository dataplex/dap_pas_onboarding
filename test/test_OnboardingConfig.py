import unittest

from .context import onboarding
from onboarding.onboardingconfig import OnboardingConfig

class TestOnboardingConfig(unittest.TestCase):
    def test_config_reads_correct_section(self):
        input_file = 'test/inputs/testconfig.ini'
        input_env = 'unittest'
        input_ccp_query = 'ccp_query'
        input_policy_out = 'inputs/nothing_created.json'

        expected_verifySsl = False
        expected_account = 'testacct'
        expected_dap_master = 'master.test'
        expected_pam_host = 'pvwa.test'
        expected_platform_id = 'ConjurHostTest'
        expected_auto_mgmt = True

        config = OnboardingConfig(input_file, input_env, input_ccp_query, input_policy_out)

        self.assertEqual(expected_verifySsl, config.verifySsl)
        self.assertEqual(expected_account, config.account)
        self.assertEqual(expected_dap_master, config.dap_master)
        self.assertEqual(expected_pam_host, config.pam_host)
        self.assertEqual(expected_platform_id, config.platform_id)
        self.assertEqual(expected_auto_mgmt, config.automatic_management_enabled)

if __name__ == '__main__':
    unittest.main()
