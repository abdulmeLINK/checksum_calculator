# test_checksum_verification.py

import unittest
from checksum_algorithms import calculate_checksum_xor, calculate_checksum_mod, calculate_checksum_mod_scaled
from checksum_verification import verify_checksum

class TestChecksumVerification(unittest.TestCase):

    def test_verify_checksum_xor(self):
        # Test with a small text file
        checksum = calculate_checksum_xor('test.txt', 7)
        result = verify_checksum('test.txt', bin(checksum)[2:].zfill(7), 'xor', 7, 'binary', False)
        self.assertEqual(result, True)

    def test_verify_checksum_mod(self):
        # Test with a small text file
        checksum = calculate_checksum_mod('test.txt', 7)
        result = verify_checksum('test.txt', bin(checksum)[2:].zfill(7), 'mod', 7, 'binary', False)
        print(result,checksum)
        self.assertEqual(result, True)

    def test_verify_checksum_mod_scaled(self):
        # Test with a small text file
        checksum = calculate_checksum_mod_scaled('test.txt', 7)
        result = verify_checksum('test.txt', bin(checksum)[2:].zfill(7), 'mod_scaled', 7, 'binary', False)
        print(bin(checksum)[2:],checksum, result)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
