import datetime

def filename(srn, period, created=None, 
			 submission_no=1, file_id='CONC', version=1.1):
	"""File must always conform to the following file naming convention and 
	have a unique file name:

	SRN-Reporting Date-Date file was Created-Version No-File Identifier-Submission 
	Sequence Number

	1. SRN - Supplier Reference Number of reporting institution as assigned
	   by the Bank of Ghana.
	2. Reporting Date - The Date (Period) as of which the data refers to. 
	   Must be an 'as at' valid calendar date and in YYYYMMDD format.
	3. Date file was Created - Must contain the date when the file was 
	   created/extracted/generated from the Data Provider's system. 
	   Must be valid calendar date and in YYYYMMDD format.
	4. Version Number - Version number of the reporting template. (1.1 for this template)
	5. File Identifier - CONC, for Consumer Credit data file.
	6. Submission Sequence Number - To identify each submission in case of 
	   multiple submissions of the same format within a reporting period. 
	   Indicate 1, 2, 3... for first, second and third... submissions respectively
	
	Example: 10118-20120130-20120205-1.1-CONC-12.csv will be a valid filename 
	for an institution with SRN 10118 submitting a Consumer Credit data for the 
	month of January 2012. The file was created with version 1.1 on the 5th of February, 
	2012 and this is the 12th submission within the reporting period.
	"""

	if created is None:
		created = datetime.date.today()

	assert type(created) is datetime.date
	assert type(period) is datetime.date

	return '%s-%s-%s-%s-%s-%s.csv' % (srn, date(period), date(created), version, file_id, submission_no)

def date(dt):
	return dt.strftime('%Y%m%d')