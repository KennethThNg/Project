"""
File name: process.py
Python Version: 3.7
"""


class Extractor:
    """
    This class is used to extract value from textual input.
    """

    @staticmethod
    def sender_alias(content_raw):
        """
        Extraction of the alias of the sender.

        :param content_raw: the value in the csv file
        :type content_raw: string
        :return: string
        """
        for line in content_raw.splitlines():
            if line.startswith("From: ") and len(line) > 6:
                last_char = line.find('<')
                if last_char == -1:
                    alias = line[6:].strip()
                else:
                    alias = line[6:last_char]
                return alias.strip()
        return None

    @staticmethod
    def earth_area(content, area):
        """
        Check whether or not the content is related to the area based on keywords.

        :param content: content after being cleaned
        :type content: string
        :param area: kind of enumeration
        :type area: string
        :return: boolean
        """
        if area == "africa":
            countries = ["algeria", "egypt", "kenya", "libya", "morocco"]
            cities = ["benghazi"]
            people = ["kaddafi", "qaddafi"]
            words = countries + cities + people
        elif area == "central_asia":
            countries = ["afghanistan", "pakistan"]
            people = ["karzai"]
            words = countries + people
        elif area == "europe":
            countries = ["britain", "france", "germany", "italy", "spain", "switzerland"]
            organizations = ['eu', 'european union']
            cities = ["berlin", "london", "paris"]
            people = ["blair", "cameron", "holland", "merkel", "sarkozy"]
            words = countries + organizations + cities + people
        elif area == "far_east":
            countries = ["china", "japan", "korea"]
            people = ["kim jong"]
            words = countries + people
        elif area == "middle_east":
            countries = ["arabia", "irak", "iran", "iraq", "israel", "palestine", "syria", "yemen"]
            organizations = ['idf', 'hamas']
            people = ["bachar"]
            words = countries + organizations + people
        elif area == "latino":
            countries = ["brazil", "colombia", "cuba", "venezuela"]
            peoples = ["chavez"]
            words = countries + peoples
        elif area == "north_america":
            countries = ["canada", "mexico", "us", "usa"]
            words = countries
        elif area == "russia":
            countries = ["russia", "ukraine"]
            peoples = ["ianoukovytch", "putin"]
            words = countries + peoples
        else:
            raise ValueError

        for word in words:
            words_left = word + " "
            words_middle = " " + word + " "
            words_right = " " + word
            if content.startswith(words_left) or content.endswith(words_right) or words_middle in content:
                return True
        return False
