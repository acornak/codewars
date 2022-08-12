"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries
the "instructions" for the development and functioning of living organisms.
If you want to know more: http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
Your function receives one side of the DNA (string), you need to
return the other complementary side. DNA strand is never empty or there is no DNA at all.
More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
Example: (input --> output)
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""
import unittest


def dna_strand(dna: str) -> str:
    """
    Returns complementary DNA sequence, replaces A with T, and C with G and vice versa
    """
    character_map: dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return dna.translate(str.maketrans(character_map))


class ComplementaryDNATestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        dna = "AAAA"
        res = dna_strand(dna)
        self.assertEqual(res, "TTTT")

        # test argument mutation
        self.assertEqual(dna, "AAAA")

    def test_2(self):
        """
        Test 2
        """
        dna = "ATTGC"
        res = dna_strand(dna)
        self.assertEqual(res, "TAACG")

        # test argument mutation
        self.assertEqual(dna, "ATTGC")

    def test_3(self):
        """
        Test 3
        """
        dna = "GTAT"
        res = dna_strand(dna)
        self.assertEqual(res, "CATA")

        # test argument mutation
        self.assertEqual(dna, "GTAT")


if __name__ == "__main__":
    unittest.main()
