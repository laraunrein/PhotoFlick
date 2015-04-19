#!/usr/bin/env python

# Imports #####################################################################
import unittest

from PhotoFlick import PhotoFlick as PF


###############################################################################
class SanityTest(unittest.TestCase):
    def test_init(self):
        '''Verify object creation works/fails correctly'''

        # verify valid file creates object
        self.assertTrue(isinstance(PF(), PF))


###############################################################################
if __name__ == "__main__":
    unittest.main()
