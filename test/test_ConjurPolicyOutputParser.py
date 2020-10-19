import unittest
import os

from .context import onboarding
from onboarding.conjurpolicyoutputparser import ConjurPolicyOutputParser

class TestConjurPolicyOutputParser(unittest.TestCase):
    def test_given_empty_output_parser_returns_empty_list(self):
        parser = ConjurPolicyOutputParser()
        expected = []
        actual = parser.hosts('')
        self.assertCountEqual(expected, actual)

    def test_given_no_hosts_returns_empty_list(self):
        input_path = 'inputs/nothing_created.json'
        input = self.read_input(input_path)

        parser = ConjurPolicyOutputParser()
        expected = []
        actual = parser.hosts(input)
        self.assertCountEqual(expected, actual)
    
    def test_given_a_single_host_parser_returns_the_host(self):
        input_path = 'inputs/single_host_created.json'
        input = self.read_input(input_path)
        expected_name = "test1"
        expected_api_key = "3nzy1wn2p0e0n02y99wkmf4xbrb3fc65nw3pvmgb11858rgcf594ey"
        expected_account = "_"
        expected_login_name = "host/test1"

        parser = ConjurPolicyOutputParser()
        actual = parser.hosts(input)
        self.verify_host(expected_name, expected_api_key, expected_account, expected_login_name, actual[0])

    def test_given_multiple_hosts_parser_returns_correct_hosts(self):
        input_path = 'inputs/multiple_hosts_created.json'
        input = self.read_input(input_path)
        expected_account = "_"
        expected_api_keys = { 
            "test1": "3nzy1wn2p0e0n02y99wkmf4xbrb3fc65nw3pvmgb11858rgcf594ey",
            "test2": "eeamx53vec0t83pnfm9y1chd39w3qx35y3earvaw87hcdc1p8yyhk",
            "test3": "3kznkfz3k8da071wkser1wdr3cs2vjqd473zg2rvc23gk8p0jqtgje",
            "test4": "26zacm91ypnbfm1pke9bx18n6g725zd92m2x2mp0z3jh9x21ywq13"
        }

        parser = ConjurPolicyOutputParser()
        actual = parser.hosts(input)

        self.verify_host('test1', expected_api_keys['test1'], expected_account, 'host/test1', actual[0])
        self.verify_host('test2', expected_api_keys['test2'], expected_account, 'host/test2', actual[1])
        self.verify_host('test3', expected_api_keys['test3'], expected_account, 'host/test3', actual[2])
        self.verify_host('test4', expected_api_keys['test4'], expected_account, 'host/test4', actual[3])

    def test_given_host_and_user_parser_only_returns_host(self):
        input_path = 'inputs/hosts_and_user_created.json'
        input = self.read_input(input_path)
        expected_account = "_"
        expected_api_key = "7z0b3vy8fdf1q6p0ck2v3nyq53r87aqc115frr93btyaddkgwvsf"
        expected_name = "test1"
        expected_login_name = "host/test1"

        parser = ConjurPolicyOutputParser()
        actual = parser.hosts(input)

        self.verify_host(expected_name, expected_api_key, expected_account, expected_login_name, actual[0])
        self.assertEqual(1, len(actual))

    def verify_host(self, expected_name, expected_api_key, expected_account, expected_login_name, actual_host):
        self.assertEqual(expected_name, actual_host.name)
        self.assertEqual(expected_api_key, actual_host.api_key)
        self.assertEqual(expected_account, actual_host.account)
        self.assertEqual(expected_login_name, actual_host.login_name)

    def read_input(self, input_filename):
        with open(os.path.join(os.path.dirname(__file__), input_filename)) as f:
           return f.read()

if __name__ == '__main__':
    unittest.main()
