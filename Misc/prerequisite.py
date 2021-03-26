from sample import CTReports

def prerequisite1():
    s= CTReports.get_tests_status(['unittestsample.test_check2'])
    return s