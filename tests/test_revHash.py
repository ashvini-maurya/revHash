from nose.tools import *
import unittest
#from revHash.revHash import ReverseHash
from ..revHash import reverseHash

class TestDrivenForReverseHash(unittest.TestCase):

	def setUp(self):
		self.rev = ReverseHash()

	def test_revHash_returns_correct_result(self):
		result = self.rev.rev_hash(680131659347)
		self.assertEqual('leepadg', result)

	def test_revHash_returns_error_if_arg_is_not_number(self):
		self.assertRaises(ValueError, self.rev.rev_hash, 'abcdefgh')

	def test_revHash_returns_error_if_arg_is_empty(self):
		self.assertRaises(ValueError, self.rev.rev_hash, ' ')


	def test_revHash_returns_error_if_arg_type_mismatch(self):
		self.assertRaises(TypeError, self.rev.rev_hash)


if __name__ == '__main__':
	unittest.main()
