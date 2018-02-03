
import unittest
import sys
import tempfile


sys.path.append("..")
import os, random, string
from file_management import *


def random_string(n):
    min_char = n
    max_char = 128
    allchar = string.ascii_letters + string.punctuation + string.digits
    return "".join(random.choice(allchar) for x in range( random.randint(min_char, max_char)))

class TestFileManagement(unittest.TestCase):

    def test_create_name(self):

        temp_file = tempfile.NamedTemporaryFile(suffix='.tst')
        match_name = '{0}_{1}_{2}.{3}'.format('test_pattern_hypershade', datetime.datetime.now().strftime("%y%m%d%H%M%S"), '001', 'tst')

        self.assertEqual(create_name(tmp_file=temp_file.name, version=1, name='test_pattern_hypershade'), match_name)

    def test_add_version(self):
            # standart input name
            self.assertEqual(add_version(file='name_with_multi_underscore_hash_001.tst'), 'name_with_multi_underscore_hash_002.tst')

            for n in xrange(5):
                rstring = random_string(n)
                self.assertEqual(add_version(file='{0}_hash_001.tst'.format(rstring)), '{0}_hash_002.tst'.format(rstring))



if __name__ == '__main__':
    unittest.main()

