import json
import unittest

from ...__version__ import __VERSION__, __GIT_COMMIT__

from object_test_runner import ObjectTestRunner

class Report:
    '''
    Provides utility methods to convert a report object returned by
    ObjectTestRunner into json and markdown formats.

    Attributes:
        test_path:
            A string containing the path to the root folder containing
            tests for the project.
        match_pattern:
            A string containing the match pattern required for unittest to
            recursively discover tests (usually "test*.py").
        reports_path:
            A string containing the path to the reports folder where the
            test output should be written.
    '''
    def __init__(self,
                 test_path="app/test/",
                 match_pattern="test*.py",
                 reports_path="reports/"):
        self.test_path = test_path
        self.match_pattern = match_pattern
        self.reports_path = reports_path
        tests = unittest.TestLoader().discover(test_path,
                                               pattern=match_pattern)
        self.report = {
            "details": {
                "api_version": __VERSION__,
                "release_id": __GIT_COMMIT__,
                "date": int(time.time()*1000),
                "environment": {
                    "computer": os.getenv("COMPUTERNAME", "N/A"),
                    "client_name": os.getenv("CLIENTNAME", "N/A"),
                    "email": os.getenv("EMAIL", "N/A"),
                    "user_name": os.getenv("USERNAME", "N/A"),
                    "user_domain": os.getenv("USERDOMAIN", "N/A"),
                    "os": os.getenv("OS", "N/A"),
                }
            },
            "report": ObjectTestRunner().run(tests)
        }

    def generate_json_report(self):
        '''
        Outputs the report created by ObjectTestRunner as a JSON file in the
        reports directory.
        '''
        filename = f"{self.reports_path}/test-report.json"
        with open(filename) as f:
            json.dump(obj=self.report, fp=f, indent=4)
        raise NotImplementedError

    def generate_markdown_report(self):
        '''
        Outputs the report created by ObjectTestRunner as a markdown document
        in the reports directory.
        '''
        filename = f"{self.reports_path}/test-report.md"
        raise NotImplementedError