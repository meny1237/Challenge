import unittest
import uniqueNameCounter


class TestStringMethods(unittest.TestCase):

    def test_all_equal(self):
        self.assertEqual(uniqueNameCounter.count_unique_names('Deborah', 'Egli',
                                                              'Deborah', 'Egli', 'Deborah Egli'), 1)

    def test_nicknames(self):
        self.assertEqual(uniqueNameCounter.count_unique_names('Deborah', 'Egli',
                                                              'Debbie', 'Egli', 'Debbie Egli'), 1)

    def test_typo(self):
        self.assertEqual(uniqueNameCounter.count_unique_names('Deborah', 'Egni',
                                                              'Deborah', 'Egli', 'Deborah Egli'), 1)

    def test_middle_name(self):
        self.assertEqual(uniqueNameCounter.count_unique_names('Deborah S', 'Egli',
                                                              'Deborah', 'Egli', 'Egli Deborah'), 1)

    def test_diff_ship_name(self):
        self.assertEqual(uniqueNameCounter.count_unique_names('Michele', 'Egli',
                                                              'Deborah', 'Egli', 'Michele Egli'), 2)

if __name__ == '__main__':
    unittest.main()
