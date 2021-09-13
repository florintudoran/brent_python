import unittest
from tests.home.login_yp_myprofile_tests_multiple import LoggedTestsMultiple
from tests.home.login_myprofile_csv_data_test import LoginMyprofileCSVDataTest

# Get all test from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoggedTestsMultiple)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginMyprofileCSVDataTest)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
