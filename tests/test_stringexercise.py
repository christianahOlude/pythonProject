import unittest

from classwork.stringexercise import number_of_characters, two_seperated_words, returns_ce


class TestStringExercise(unittest.TestCase):
    def test_number_of_characters(self):
        words = 'semicolon.africa'
        actual = number_of_characters(words)
        expected = ['s','e','m','i','c','o','l','o','n','.','a','f','r','i','c','a']
        self.assertEqual(actual, expected)

    def test_number_of_characters_2(self):
        words = 'christianah'
        actual = number_of_characters(words)
        expected = ['c','h','r','i','s','t','i','a','n','a','h']
        self.assertEqual(actual, expected)

    def test_merge_characters(self):
        word1 = 'abc'
        word2 = 'xyz'
        actual = two_seperated_words(word1, word2)
        expected = 'yzcxab'
        self.assertEqual(expected,actual)

    def test_two_seperated_words(self):
        word1 = 'bcd'
        word2 = 'oop'
        actual = two_seperated_words(word1, word2)
        expected = 'opdobc'
        self.assertEqual(expected,actual)


    def test_add_ce_to_word(self):
        word = "helloo"
        actual = returns_ce(word,"ce")
        expected = "helceloo"
        self.assertEqual(expected,actual)