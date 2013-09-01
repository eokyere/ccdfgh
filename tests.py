import unittest
import datetime
import ccdf

class TestCCDF(unittest.TestCase):
	def test_date(self):
		self.assertEqual('20080601', ccdf.date(datetime.date(2008, 6, 1)))
		self.assertEqual('20120205', ccdf.date(datetime.date(2012, 2, 5)))

	def test_file_name(self):
		self.assertEqual('10118-20120130-20120205-1.1-CONC-12.csv',
						 ccdf.filename(srn='10118', period=datetime.date(2012, 1, 30),
						 	           created=datetime.date(2012, 2, 5), version=1.1,
						 	           submission_no=12))

if __name__ == "__main__":
    unittest.main()