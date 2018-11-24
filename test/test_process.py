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

    def test_content_lemmatization(self):
        raw = """
            From: Mills, Cheryl D <MillsCD@state.gov>
            Cc: Abedin, Huma
            U.S. Department of State
            STATE DEPT. - PRODUCED TO HOUSE SELECT BENGHAZI COMM.
            RELEASE IN FULL
            STATE DEPT
            SUBJECT TO AGREEMENT ON SENSITIVE INFORMATION
            Sent: Wednesday, September 12, 2012 10:16 AM
            This should be the content. Some words will be filtered out. Let's see what happens to plural nouns.
        """
        expected = "let see happens plural noun"
        self.assertEqual(Process.content(raw, True), expected)

    def test_content_with_email_lemmatization(self):
        raw = "Hi! My name is John, you can contact me at john@service.com anytime this week.\n" + \
            "Companies are getting more money with the new legislation."
        expected = "name john contact anytime week|company getting money new legislation"
        self.assertEqual(Process.content(raw, True), expected)

    def test_content_stemming(self):
        raw = """
            From: Mills, Cheryl D <MillsCD@state.gov>
            Cc: Abedin, Huma
            U.S. Department of State
            STATE DEPT. - PRODUCED TO HOUSE SELECT BENGHAZI COMM.
            RELEASE IN FULL
            STATE DEPT
            SUBJECT TO AGREEMENT ON SENSITIVE INFORMATION
            Sent: Wednesday, September 12, 2012 10:16 AM
            This should be the content|Some words will be filtered out. Let's see what happens to plural noons.
        """
        expected = "let see happen plural noon"
        self.assertEqual(Process.content(raw, False), expected)

    def test_content_with_email_stemming(self):
        raw = "Hi! My name is John 99, you can contact me at john@service.com anytime this week.\n" + \
              "Companies are getting more money with the new legislation."
        expected = "name john contact anytim week|compani get money new legisl"
        self.assertEqual(Process.content(raw, False), expected)

    def test_content_sentence_token(self):
        raw = "Hi, Jason is likely to die tonight? This is not a joke, I swear it to you I am really serious!"
        expected = "hi jason likely die tonight|joke swear really serious"
        self.assertEqual(Process.content(raw, True), expected)


if __name__ == '__main__':
    unittest.main()
