#!/usr/bin/env python3

import sys
import configparser

from onboarding.onboardingconfig import OnboardingConfig
from onboarding.conjurpolicyoutputparser import ConjurPolicyOutputParser
from onboarding.serviceshelper import ServicesHelper

def main(argv):
    if len(argv) < 4:
        print("Usage: onboard.py <config.ini> <config_env> <ccp_query> <policy_out_file>")
        exit(1)

    config_file = argv[0]
    config_env = argv[1]
    ccp_query = argv[2]
    policy_out_path = argv[3]

    config = OnboardingConfig(config_file, config_env, ccp_query, policy_out_path)

    outputParser = ConjurPolicyOutputParser()
    svcHelper = ServicesHelper(config, outputParser)
    svcHelper.onboard()

if __name__ == "__main__":
   main(sys.argv[1:])
