import unittest
import datetime
import xlrd

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

	def get_valid_rows(self):
		wb = open_wb('data/valid-rows.xlsx')
		sheet = wb.sheet_by_name('Data')
		rows = [sheet.row_values(i)[1:] for i in range(sheet.nrows)] # cut off serial
		wb.unload_sheet('Data')
		wb.release_resources()
		
		# remove header
		header = rows[0]
		rows = rows[1:]

		# fix Excel data
		for values in rows:
			for i, val in enumerate(values):
				if type(val) in [float, int]:
					values[i] = str(int(val))
		
		return rows

	def test_valid_rows(self):
		rows = self.get_valid_rows()
		self.assertEqual(199, len(rows))

		# data = dict(FacilityAccNum='abc|123', CustomerID=1234)
		# row = ccdf.row(data)
		# values = row.split('|')

		for row in rows:
			ccdf.validate(row)


def open_wb(path, use_mmap=False):
    return xlrd.open_workbook(file_contents=content(path), 
                              use_mmap=use_mmap)

def content(path):
    f = open(path, 'r')
    content = f.read() 
    f.close()
    return content 

if __name__ == "__main__":
    unittest.main()