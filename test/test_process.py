import unittest
from src.process import Process


class TestExtractor(unittest.TestCase):

    def test_alias(self):
        john = "John Locke"
        abedin = "Abedin, Huma "
        email = "Russorv@state.gov"
        partial_email = "jake.sullivan@"
        with_dot = "daniel.baer"
        self.assertEqual(Process.alias(john), "john locke")
        self.assertEqual(Process.alias(abedin), "abedin huma")
        self.assertEqual(Process.alias(email), "russorv@state.gov")
        self.assertEqual(Process.alias(partial_email), "jake sullivan")
        self.assertEqual(Process.alias(with_dot), "daniel baer")

    def test_content(self):
        raw = """
            From: Mills, Cheryl D <MillsCD@state.gov>
            Cc: Abedin, Huma
            U.S. Department of State
            STATE DEPT. - PRODUCED TO HOUSE SELECT BENGHAZI COMM.
            RELEASE IN FULL
            STATE DEPT
            SUBJECT TO AGREEMENT ON SENSITIVE INFORMATION
            Sent: Wednesday, September 12, 2012 10:16 AM
            This should be the content. But some words will be filtered out.
        """
        expected = "content words filtered"
        self.assertEqual(Process.content(raw), expected)


if __name__ == '__main__':
    unittest.main()
