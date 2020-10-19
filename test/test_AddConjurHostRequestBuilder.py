import unittest
import json

from .context import onboarding
from onboarding.addconjurhostrequestbuilder import AddConjurHostRequestBuilder
from onboarding.conjurrole import ConjurRole
from onboarding.onboardingconfig import OnboardingConfig

class TestAddConjurHostRequestBuilder(unittest.TestCase):
    def test_given_config_and_host_builder_creates_correct_json(self):
        input_config = 'test/inputs/testconfig.ini'
        input_config_env = 'unittest'

        input_object_name = 'host-testhost'
        input_host_type = 'host'
        input_host_name = 'testhost'
        input_host_login = 'host/testhost'
        input_host_account = 'testaccount'
        input_host_api_key = 'api_123_456'

        
        config = OnboardingConfig(input_config, input_config_env, ccp_query='', policy_out_path='')
        host = ConjurRole(input_host_account, input_host_type, input_host_name, input_host_api_key)

        request_body = AddConjurHostRequestBuilder(config, host).build()
        actual = json.loads(request_body)

        self.assertEqual(input_object_name, actual['name'])
        self.assertEqual(input_host_name, actual['safeName'])
        self.assertEqual(input_host_login, actual['userName'])
        self.assertEqual(input_host_api_key, actual['secret'])

        self.assertEqual(input_host_account, actual['platformAccountProperties']['ConjurAccount'])