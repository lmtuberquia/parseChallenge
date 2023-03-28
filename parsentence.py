import re


class ReplaceSentence:
    """
       A class that replaces each word in a sentence based on the following rules:
       1. first letter
       2. number of distinct characters between first and last character
       3. last letter
       Conditions: Words are separated by spaces or non-alphabetic characters and these separators should be maintained
       in their original form and location in the answer.
    """

    def __init__(self):
        """
        Constructs a ReplaceSentence object with the specified sentence.
        """
        pass

    @staticmethod
    def transform_word(word):
        """
        Replaces a single word based on the following rules:

        :param word: The word to be processed.
        :type word: str
        :return: The processed word.
        :rtype: str
        """
        if len(word) <= 2:
            return word

        if not word.isalpha():
            return word  # Return non-alphabetic characters as is

        first_letter = word[0]
        last_letter = word[-1]
        distinct_chars = set(word[1:-1])
        num_distinct_chars = str(len(distinct_chars))

        return f"{first_letter}{num_distinct_chars}{last_letter}"

    def replace(self, sentence):
        """
        Replaces all the words in the sentence based on the following rules:

        :return: The processed sentence.
        :rtype: str
        """
        words = re.split(r"(\d|\b)", sentence)
        transformed_words = [self.transform_word(word) for word in words]
        return "".join(transformed_words)
