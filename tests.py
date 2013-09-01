import unittest
import datetime
import ccdf

class TestCCDF(unittest.TestCase):
	def test_date(self):
		self.assertEqual('20080601', ccdf.date(datetime.date(2008, 6, 1)))
		self.assertEqual('20120205', ccdf.date(datetime.date(2012, 2, 5)))

	def test_number(self):
		self.assertEqual(1, ccdf.number(1.1))
		self.assertEqual(2, ccdf.number(1.5))

	def test_file_name(self):
		self.assertEqual('10118-20120130-20120205-1.1-CONC-12.csv',
						 ccdf.filename(srn='10118', period=datetime.date(2012, 1, 30),
						 	           created=datetime.date(2012, 2, 5), version=1.1,
						 	           submission_no=12))

	def test_invalid_row(self):
		try:
			row = ccdf.row({})
			raise Exception('ValueError should be raised')
		except ValueError, msg:
			pass

	def test_valid_row(self):
		data = dict(FacilityAccNum='abc|123', CustomerID=1234)
		row = ccdf.row(data)
		values = row.split('|')

		self.assertEqual(178, len(values))
		
		self.assertEqual('D', ccdf.get_value(values, 'Data'))


		xs = (
			('CorrectionIndicator', ccdf.CORRECTION_INDICATOR),
			('OtherID', ccdf.OTHER_ID),
			('OwnerOrTenant', ccdf.OWNER_OR_TENANT),
			('EmpType', ccdf.EMPLOYMENT_TYPE),
			('JointOrSoleAcc', ccdf.JOINT_OR_SOLE_ACCOUNT),
		)

		for key, choices in xs:  
			self.assertIn(ccdf.get_value(values, key), choices)

if __name__ == "__main__":
    unittest.main()