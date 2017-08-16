import unittest
import subprocess
import glob


class testEndToEnd(unittest.TestCase):

    # Unit test for validating test outputs from install to test script
    def test_endtoend(self):
        generatedFaFiles = []

        # Fetch the generated fa files and verify that they match reference files
        for filename in glob.glob("../test_output/*.fa"):
            if filename.__contains__("msa") or filename.__contains__("refseq"):
                generatedFaFiles.append(open(filename, 'r'))

        referenceFaFiles = [open("test_constants/rpoB_0_msa_0.fa", 'r'),
                            open("test_constants/rpoB_0_refseq_msa_1.fa", 'r')]

        # compare the two FA files with reference
        if(len(generatedFaFiles) > 0):
            for i in range(0,2):
                print 'Comparing reference file: ' + referenceFaFiles[i].name
                tempStringReference = ''
                tempStringGenerated = ''
                for line in referenceFaFiles[i]:
                    tempStringReference = tempStringReference.rstrip('\r\n') + line
                for line in generatedFaFiles[i]:
                    tempStringGenerated = tempStringGenerated.rstrip('\r\n') + line
                self.assertEqual(tempStringReference, tempStringGenerated)
        else:
            print("Please run test_metannotate.sh and verify that it works before running nosetests.")


if __name__ == '__main__':
    unittest.main()
