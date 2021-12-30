import unittest
import os
import sys
import inspect

from stats import *

#class TestModule(unittest.TestCase):

    # def testIntInputs(self):
    #     ''' function should fail on non-int inputs '''
    #     self.assertRaisesRegex(TypeError, 'Expected int inputs', pagination, 'a', 2, 3, 4)
    #     self.assertRaisesRegex(TypeError, 'Expected int inputs', pagination, 1, 'a', 3, 4)
    #     self.assertRaisesRegex(TypeError, 'Expected int inputs', pagination, 1, 2, 'a', 4)
    #     self.assertRaisesRegex(TypeError, 'Expected int inputs', pagination, 1, 2, 3, 'a')
    #     self.assertRaisesRegex(TypeError, 'Expected int inputs', pagination, 1., 2, 3, 4)
    #
    # def testInputsSanityChecks(self):
    #     ''' function should fail on non-int inputs '''
    #     self.assertRaisesRegex(IndexError, 'Current Page should be a positive number', pagination, 0, 2, 3, 4)
    #     self.assertRaisesRegex(IndexError, 'Total Pages should be a positive number', pagination, 1, 0, 3, 4)
    #     self.assertRaisesRegex(IndexError, 'Boundaries input should be a positive number', pagination, 1, 2, 0, 4)
    #     self.assertRaisesRegex(IndexError, 'Around input should be a positive number', pagination, 1, 2, 3, -1)
    #     self.assertRaisesRegex(IndexError, 'Current Page should be between 1 and Total Pages', pagination, 3, 2, 3, 2)
    #
    # def testBoundaryPages(self):
    #     ''' testing boundary pages function '''
    #     self.assertEqual(boundary_pages(10, 2), [1, 2, 9, 10])
    #     self.assertEqual(boundary_pages(10, 1), [1, 10])
    #     self.assertEqual(boundary_pages(3, 1), [1, 3])
    #     self.assertEqual(boundary_pages(3, 2), [1, 2, 3])
    #     self.assertEqual(boundary_pages(3, 999), [1, 2, 3])
    #     self.assertEqual(boundary_pages(10, 12), list(range(1, 11)))
    #     self.assertEqual(boundary_pages(10, 5), list(range(1, 11)))
    #     self.assertEqual(boundary_pages(11, 5), list(range(1, 6)) + list(range(7, 12)))
    #
    # def testBoundaryPages(self):
    #     ''' testing around pages function '''
    #     self.assertEqual(around_pages(5, 2), [3, 4, 5, 6, 7])
    #     self.assertEqual(around_pages(5, 1), [4, 5, 6])
    #     self.assertEqual(around_pages(5, 0), [5])
    #
    # def testExample1(self):
    #     ''' testing on the input data for example 1'''
    #     self.assertEqual(pagination(4, 5, 1, 0), [1, THREE_DOTS, 4, 5])
    #
    # def testExample2(self):
    #     ''' testing on the input data for example 2'''
    #     self.assertEqual(pagination(4, 10, 2, 2), [1, 2, 3, 4, 5, 6, THREE_DOTS, 9, 10])
    #
    # def testExample3(self):
    #     ''' testing on the input data for example 3'''
    #     self.assertEqual(pagination(14, 1400, 10, 10),
    #                      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
    #                       THREE_DOTS, 1391, 1392, 1393, 1394, 1395, 1396,
    #                       1397, 1398, 1399, 1400])


if (__name__ == "__main__"):
    unittest.main()
