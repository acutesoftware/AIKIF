# run_tests.py
"""
from tests import *
import unittest

if __name__ == "__main__":
    unittest.main()
 """   
 
import unittest as unittest
 
if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
    unittest.TextTestRunner().run(all_tests)    