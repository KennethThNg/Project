import unittest
from src.extractor import Extractor
from src.process import Process


class TestExtractor(unittest.TestCase):

    def test_sender_alias(self):
        content_sam = "Some text\nFrom: Sam"
        email = "From: sullivan jacob j <sullivanjj@state.gov>"
        content_empty = "Some text\nFrom: "
        content_none = "Some text"
        self.assertEqual(Extractor.sender_alias(content_sam), "Sam")
        self.assertEqual(Extractor.sender_alias(email), "sullivan jacob j")
        self.assertIsNone(Extractor.sender_alias(content_empty))
        self.assertIsNone(Extractor.sender_alias(content_none))

    def test_destination_alias(self):
        content_sam = "Some text\nTo: Sam"
        email = "To: sullivan jacob j <sullivanjj@state.gov>"
        content_empty = "Some text\nTo: "
        content_none = "Some text"
        self.assertEqual(Extractor.destination_alias(content_sam), "Sam")
        self.assertEqual(Extractor.destination_alias(email), "sullivan jacob j")
        self.assertIsNone(Extractor.destination_alias(content_empty))
        self.assertIsNone(Extractor.destination_alias(content_none))

    def test_detect_central_africa(self):
        algeria = "i would like to bomb algeria"
        egypt = "there is revolution in egypt and it is not a joke"
        kaddafi = "qaddafi will die in the near future"
        bengazi = "we have people we know in benghazi"
        nothing = "this message does not contain any reference"
        self.assertTrue(Extractor.earth_area(algeria, "africa"))
        self.assertTrue(Extractor.earth_area(egypt, "africa"))
        self.assertTrue(Extractor.earth_area(kaddafi, "africa"))
        self.assertTrue(Extractor.earth_area(bengazi, "africa"))
        self.assertFalse(Extractor.earth_area(nothing, "africa"))

    def test_detect_central_asia(self):
        karzai = "karzai is our puppet but we are worry"
        pakistan = "we are violating international laws with our drones in pakistan"
        nothing = "this message does not contain any reference"
        self.assertTrue(Extractor.earth_area(karzai, "central_asia"))
        self.assertTrue(Extractor.earth_area(pakistan, "central_asia"))
        self.assertFalse(Extractor.earth_area(nothing, "central_asia"))

    def test_detect_europe(self):
        eu = "the eu will hurt our companies with their new laws"
        us = "the united states should not appear in europe"
        self.assertTrue(Extractor.earth_area(eu, "europe"))
        self.assertFalse(Extractor.earth_area(us, "europe"))

    def test_detect_far_east(self):
        china = "my clothes are made in china"
        japan = "The movie has been bought by a company based in japan"
        korea = "I love kim jong un"
        nothing = "this message does not contain any reference"
        self.assertTrue(Extractor.earth_area(china, "far_east"))
        self.assertTrue(Extractor.earth_area(japan, "far_east"))
        self.assertTrue(Extractor.earth_area(korea, "far_east"))
        self.assertFalse(Extractor.earth_area(nothing, "far_east"))

    def test_detect_far_east(self):
        bachar = "bachar is not about to go"
        iraq = "iraq is not a safe place anymore"
        iran = "iran is not affected by our pressure"
        israel = "israel is our only ally"
        nothing = "this message does not contain any reference"
        self.assertTrue(Extractor.earth_area(bachar, "middle_east"))
        self.assertTrue(Extractor.earth_area(iraq, "middle_east"))
        self.assertTrue(Extractor.earth_area(iran, "middle_east"))
        self.assertTrue(Extractor.earth_area(israel, "middle_east"))
        self.assertFalse(Extractor.earth_area(nothing, "middle_east"))

    def test_detect_latino(self):
        chavez = "cia killed chavez"
        nothing = "this message does not contain any reference"
        self.assertTrue(Extractor.earth_area(chavez, "latino"))
        self.assertFalse(Extractor.earth_area(nothing, "latino"))

    def test_detect_north_america(self):
        canada = "this country canada is a nato member"
        mexico = "coca-cola takes its water from mexico"
        nothing = "this message does not contain any reference"
        self.assertTrue(Extractor.earth_area(canada, "north_america"))
        self.assertTrue(Extractor.earth_area(mexico, "north_america"))
        self.assertFalse(Extractor.earth_area(nothing, "north_america"))

    def test_detect_russia(self):
        putin = "we need to kill putin somehow"
        ukraine = "viktor ianoukovytch is not the president anymore"
        nothing = "this message does not contain any reference"
        self.assertTrue(Extractor.earth_area(putin, "russia"))
        self.assertTrue(Extractor.earth_area(ukraine, "russia"))
        self.assertFalse(Extractor.earth_area(nothing, "russia"))


if __name__ == '__main__':
    unittest.main()
