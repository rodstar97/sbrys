
import unittest
import sys
import tempfile


sys.path.append("..")
import os, random, string
from file_management import *



class TestCreateDirDict(unittest.TestCase):
    def setUp(self):
        self.dict = create_dir_dict()


    def test_correct_dirs(self):
        self.assertEqual(os.path.dirname(os.path.realpath(__file__)), self.dict['root'])

        self.assertEqual(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp'), self.dict['tmp'])

        self.assertEqual(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'wait'), self.dict['wait'])

        self.assertEqual(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'collection'), self.dict['collection'])



class TestCreateName(unittest.TestCase):
    def test_correct_input(self):

        temp_file = tempfile.NamedTemporaryFile(suffix='.tst')
        match_name = '{0}_{1}_{2}.{3}'.format('test_pattern_hypershade', datetime.datetime.now().strftime("%y%m%d%H%M%S"), '001', 'tst')

        self.assertEqual(create_name(tmp_file=temp_file.name, version=1, name='test_pattern_hypershade'), match_name)




class TestVersion_up(unittest.TestCase):

    def random_string(sefl, n):
        min_char = n
        max_char = 128
        allchar = string.ascii_letters + string.punctuation + string.digits
        return "".join(random.choice(allchar) for x in range(random.randint(min_char, max_char)))

    def test_correct_input(self):
        # standart input name
        self.assertEqual(version_up(file='name_with_multi_underscore_hash_001.tst'), 'name_with_multi_underscore_hash_002.tst')

        for n in xrange(5):
            rstring = self.random_string(n)
            self.assertEqual(version_up(file='{0}_hash_001.tst'.format(rstring)), '{0}_hash_002.tst'.format(rstring))



if __name__ == '__main__':
    unittest.main()

