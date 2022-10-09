import unittest

from quickcontact.utils.qr import generate_qr
from quickcontact.utils.vcf import generate_vcf


class TestGeneration(unittest.TestCase):
    """Test: Generate VCF"""

    def test_vcf(self):
        data = {"first_name": "Tester", "last_name": "One", "cell": "XXXXXXXXXX"}
        vcf = generate_vcf(data)
        self.assertIsInstance(vcf, str)

    def test_qr(self):
        data = {"first_name": "Tester", "last_name": "One", "cell": "XXXXXXXXXX"}
        qr = generate_qr(generate_vcf(data))
        self.assertIsInstance(qr, bytes)
