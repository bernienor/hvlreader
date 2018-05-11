# Unittest module for hvlfilereader

import unittest
import hvlfilereader as hvlfr
import numpy as np

'''>>> dir(self.fr1)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'__weakref__', 'data', 'header', 'identifyfile', 'instrumenttype',
'model', 'samplerate']
'''


class tektronixfrTestCase(unittest.TestCase):
    """Tests for `hvlfilereader.py`."""
    def setUp(self):
        self.fr1 = hvlfr.tektronixfr(
                   'testfiles/tektronix_DPO2012B/T0001CH1.CSV')
        pass

    def tearDown(self):
        pass

    def test_tekfr_T0001CH1(self):
        self.assertIsInstance(self.fr1.data, np.ndarray)
        self.assertIsInstance(self.fr1.header, list)
        self.assertIsInstance(self.fr1.instrumenttype, str)
        self.assertIsInstance(self.fr1.model, str)
        self.assertIsInstance(self.fr1.samplerate, float)

        self.assertEqual(self.fr1.data.size, 18747)
        self.assertEqual(self.fr1.data.shape, (6249, 3))
        self.assertEqual(self.fr1.instrumenttype, 'Tektronix oscilioscope')
        self.assertEqual(self.fr1.model, 'DPO2012B')
        # You have to compute the delta to secure the resolution
        self.assertAlmostEqual(self.fr1.samplerate, 1.6e-07,
                               delta=(self.fr1.samplerate/1.0e7))


if __name__ == '__main__':
    unittest.main()
