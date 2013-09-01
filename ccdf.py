import datetime


Mandatory = 100
RequiredConditional = 200
IfAvailable = 300

FIELD_NO = 0
FIELD_NAME = 1
FIELD_TYPE = 2
FIELD_LENGTH = 3
FIELD_OPTIONS = 4

OTHER_ID = (
	('STAFF', 'Staff ID'),
	('STUD', 'Student ID'),
	('SERV', 'Service ID'),
	('NHIS', 'National Health Insurance ID'),
)

MARITAL_STATUS = (
	('S', 'Single'),
	('W', 'Widowed'),
	('D', 'Divorced'),
	('M', 'Married'),
	('P', 'Separated'),
)

PROOF_OF_ADDRESS = (
	('WAT', 'Water Bill'),
	('ELE', 'Electricity Bill'),
)

OWNER_OR_TENANT = (
	('O', 'Owner'),
	('T', 'Tenant'),
	('F', 'Family Owned'),
)


EMPLOYEMENT_TYPE = (
	('101', 'Salaried Individual'),
	('102', 'Unemployed'),
	('103', 'Student'),
	('104', 'Self Employed'),
	('105', 'Home Maker'),
	('106', 'Pensioner'),
)


CREDIT_FACILITY_TYPE = (
	('101', 'Agriculture Facility'),
	('102', 'Auto Loan'),
	('103', 'Bank Guarantee'),
	('104', 'Bills Discounted'),
	('106', 'Credit Card'),
	('107', 'Education Loan'),
	('108', 'Hire Purchase'),
	('109', 'Housing Loan'),
	('110', 'Leasing'),
	('111', 'Letter of Credit'),
	('112', 'Loan against Bank Deposit'),
	('113', 'Loan against Employee Provident Fund'),
	('114', 'Loan against Life Insurance'),
	('115', 'Loan against Salary/Payroll Loan'),
	('116', 'Loan against Shares and Securities'),
	('117', 'Loan to Professional'),
	('118', 'Mortgage'),
	('119', 'Non-secured Loans'),
	('120', 'Other Secured Loans'),
	('121', 'Overdraft'),
	('122', 'Personal Loan'),
	('123', 'Pledge Loan'),
	('124', 'Property Loan'),
	('125', 'Government Loans'),
	('126', 'Term Loans'),
	('127', 'Travel Finance'),
	('128', 'Student Loan'),
	('129', 'Others'),
)

REPAYMENT_FREQUENCY = (
	('10', 'Weekly'),
	('11', 'Bi Monthly'),
	('12', 'Monthly'),
	('13', 'Quarterly'),
	('14', 'Tri Annually'),
	('15', 'Semi Annually'),
	('16', 'Annual'),
	('17', 'Variable'),
	('18', 'Bullet (One payment)'),
	('19', 'Demand (Revolving)'),
	('20', 'Unspecified'),
	('21', 'Balloon (especially on interest-only mortgages)'),
)

ASSET_CLASSIFICATION = (
	('A', '1 - 30 days'),
	('B', '31 - 90 days'),
	('C', '91 - 180 days'),
	('D', '181 - 360 days'),
	('E', 'Over 360 days'),
)

CREDIT_FACILITY_STATUS = (
	('A', 'Open/Active'),
	('C', 'Closed'),
	('D', 'Disputed'),
	('E', 'Terms Extended'),
	('L', 'Handed Over/Legal'),
	('N', 'Loan against Policy'),
	('P', 'Paid Up'),
	('T', 'Early Settlement'),
	('G', 'Charge-off'),
	('Z', 'Deceased'),
	('R', 'Restructured/Rescheduled'),
	('B', 'Approved, but not disbursed'),
	('W', 'Written Off'),
)


WRITE_OFF_REASON = (
	('A', 'Part Settlement'),
	('B', 'Death'),
	('C', 'Unable to locate'),
	('D', 'Government Concession'),
	('E', 'Bankruptcy'),
	('F', 'Other'),
)

CLOSURE_REASON = (
	('A', 'By Credit Grantor without prejudice to the Subject'),
	('B', 'Balance Transfer'),
	('C', 'Death'),
	('D', 'End of Credit Facility Tenure'),
	('E', 'Merger of Credit Facility'),
	('F', 'Early Settlement by Subject'),
	('G', 'By Court Order'),
	('H', 'Lost Cards/Compromised Cards'),
	('J', 'Bankruptcy'),
	('K', 'Restructured/Rescheduled'),
) 

PURPOSE_OF_FACILITY = (
	('A', 'Crisis Loan'),
	('B', 'Home Loans'),
	('S', 'Study Loan'),
	('C', 'Other Asset acquisition financing'),
	('D', 'Project Finance'),
	('E', 'Capital finance'),
	('F', 'Equipment and Machinery Finance'),
	('G', 'Working capital finance'),
	('H', 'Subscription finance'),
	('P', 'Personal finance'),
	('J', 'Finance for Trading in securities'),
	('K', 'Consolidation Loan'),
	('L', 'Other'),
)


SPECIAL_COMMENDS_CODE = (
	('101', 'Paid by Co maker'),
	('102', 'Loan assumed by another party'),
	('103', 'Account closed at credit grantor\'s request'),
	('104', 'Accounts transferred to another lender'),
	('105', 'Adjustment pending'),
	('106', 'Paying under a partial payment agreement'),
	('107', 'Purchased by another lender'),
	('108', 'Payroll deduction'),
	('109', 'Credit Line suspended'),
	('110', 'Account closed due to refinance'),
	('111', 'Account closed due to Transfer'),
	('112', 'Account paid in full for less than the full balance'),
	('113', 'First payment never received'),
	('114', 'Account paid from collateral'),
	('115', 'Principal deferred/Interest payment only'),
)

SECURITY_TYPE = (
	('A', 'Land'),
	('B', 'Shares'),
	('C', 'Government Bonds/Securities'),
	('D', 'Building'),
	('D', 'Building'),
	('E', 'Cash/ Fixed Deposit'),
	('F', 'Bank Guarantee'),
	('G', 'Salary Assignment'),
	('H', 'Terminal Benefits Assignment'),
	('J', 'Bullions'),
	('K', 'General Plant & Machinery'),
	('L', 'Vehicles'),
	('M', 'Corporate Guarantee'),
	('N', 'Individual Guarantee'),
	('P', 'Government Guarantee'),
	('Q', 'Others'),
)


PAYMENT_HISTORY_PROFILE = (
	('0', '1 to 30 days (Current Account)'),
	('1', '31 to 60 days past due'),
	('2', '61 to 90 days past due'),
	('3', '91 to 120 days past due'),
	('4', '121 to 180 days past due'),
	('5', '180+ days past due'),
)

CORRECTION_INDICATOR = (
	('0', 'Normal Monthly Submission'),
	('1', 'Correction Update/Replacement Update'),
	('2', 'Delete Record'),
)

GENDER = (
	('M', 'Male'),
	('F', 'Female'),
)

JOINT_OR_SOLE_ACCOUNT = (
	('J', 'Joint'),
	('S', 'Sole'),
)

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
	return '%s-%s-%s-%s-%s-%s.csv' % (srn, date(period), date(created), version, file_id, submission_no)

def text(value):
	if value is None:
		return ''
	return '%s' % value


def date(value):
	"""
	Date fields should contain dates only and should be in YYYYMMDD format where 
	YYYY is the usual Gregorian calendar, 
	MM is the month of the year between 01 (January) and 12 (December), and 
	DD is the day of the month between 01 and 31. 
	
	Leading "0"'s are always used to pad single digit days and months 
	e.g. 1st June 2008 should be denoted as 20080601.
	"""
	if value is None:
		return ''
	return value.strftime('%Y%m%d')

def number(value):
	"""Numeric fields should contain whole numbers only 
	(without separators and without decimals i.e. all 
	decimals to be rounded to the nearest whole number).
	"""
	if value is None:
		return ''
	return int(round(value))

def get_value(values, key):
	return values[FIELD_INDEX[key]]

FIELDS = (
	(1, 'Data', text, 1, Mandatory),
	(2, 'CorrectionIndicator', text, 1, Mandatory),
	(3, 'FacilityAccNum', text, 25, Mandatory),
	(4, 'CustomerID', text, 25, Mandatory),
	(5, 'BranchCode', text, 15, IfAvailable),
	(6, 'NatIDNum', text, 20, RequiredConditional),
	(7, 'VotersIDNum', text, 20, RequiredConditional),
	(8, 'DriverLicNum', text, 20, RequiredConditional),
	(9, 'PassportNum', text, 20, RequiredConditional),
	(10, 'SSNum', text, 20, IfAvailable),
	(11, 'EzwichNum', text, 20, IfAvailable),
	(12, 'OtherID', text, 5, IfAvailable),
	(13, 'OtherIDNum', text, 20, RequiredConditional),
	(14, 'TINum', text, 20, IfAvailable),
	(15, 'Gender', text, 1, Mandatory),
	(16, 'MaritalStatus', text, 1, Mandatory),
	(17, 'Nationality', text, 3, Mandatory),
	(18, 'DOB', date, 8, Mandatory),
	(19, 'Title', text, 10, IfAvailable),
	(20, 'Surname', text, 60, Mandatory),
	(21, 'FirstName', text, 60, Mandatory),
	(22, 'MiddleNames', text, 60, IfAvailable),
	(23, 'PrevName', text, 60, IfAvailable),
	(24, 'Alias', text, 60, IfAvailable),
	(25, 'ProofOfAddType', text, 3, IfAvailable),
	(26, 'ProofOfAddNum', text, 15, RequiredConditional),
	(27, 'CurResAddr1', text, 100, Mandatory),
	(28, 'CurResAddr2', text, 50, IfAvailable),
	(29, 'CurResAddr3', text, 50, IfAvailable),
	(30, 'CurResAddr4', text, 50, IfAvailable),
	(31, 'CurResAddrPostalCode', text, 15, IfAvailable),
	(32, 'DateMovedCurrRes', date, 8, IfAvailable),
	(33, 'PrevResAddr1', text, 100, IfAvailable),
	(34, 'PrevResAddr2', text, 50, IfAvailable),
	(35, 'PrevResAddr3', text, 50, IfAvailable),
	(36, 'PrevResAddr4', text, 50, IfAvailable),
	(37, 'PrevResAddrPostalCode', text, 15, IfAvailable),
	(38, 'OwnerOrTenant', text, 1, Mandatory),
	(39, 'PostAddrLine1', text, 100, Mandatory),
	(40, 'PostAddrLine2', text, 50, IfAvailable),
	(41, 'PostAddrLine3', text, 50, IfAvailable),
	(42, 'PostAddrLine4', text, 50, IfAvailable),
	(43, 'PostalAddPostCode', text, 15, IfAvailable),
	(44, 'EmailAddress', text, 150, IfAvailable),
	(45, 'HomeTel', text, 30, IfAvailable),
	(46, 'MobileTel1', text, 30, Mandatory),
	(47, 'MobileTel2', text, 30, IfAvailable),
	(48, 'WorkTel', text, 30, IfAvailable),
	(49, 'NumOfDependants', number, 3, IfAvailable),
	(50, 'EmpType', text, 3, Mandatory),
	(51, 'EmpPayrollNum', text, 15, RequiredConditional),
	(52, 'Paypoint', text, 20, IfAvailable),
	(53, 'EmpName', text, 50, RequiredConditional),
	(54, 'EmpAddr1', text, 100, IfAvailable),
	(55, 'EmpAddr2', text, 50, IfAvailable),
	(56, 'EmpAddr3', text, 50, IfAvailable),
	(57, 'EmpAddr4', text, 50, IfAvailable),
	(58, 'EmpAddrPostalCode', text, 15, IfAvailable),
	(59, 'DateOfEmp', date, 8, IfAvailable),
	(60, 'Occupation', text, 50, Mandatory),
	(61, 'IncomeCurrency', text, 3, Mandatory),
	(62, 'Income', number, 15, Mandatory),
	(63, 'JointOrSoleAcc', text, 1, Mandatory),
	(64, 'NoParticipantsInAcc', number, 2, Mandatory),
	(65, 'OldCustomerID', text, 25, IfAvailable),
	(66, 'OldAccountNum', text, 25, IfAvailable),
	(67, 'OldSRN', text, 5, IfAvailable),
	(68, 'OldBranchCode', text, 15, IfAvailable),
	(69, 'CreditFacilityType', text, 3, Mandatory),
	(70, 'PurposeOfFacility', text, 3, Mandatory),
	(71, 'FacilityTerm', number, 3, Mandatory),
	(72, 'DefPaymentStartDate', date, 8, IfAvailable),
	(73, 'AmountCurrency', text, 3, Mandatory),
	(74, 'FacilityAmount', number, 15, Mandatory),
	(75, 'DisbursementDate', date, 8, Mandatory),
	(76, 'DisbursementAmt', number, 15, Mandatory),
	(77, 'MaturityDate', date, 8, Mandatory),
	(78, 'SchdInstalAmount', number, 15, RequiredConditional),
	(79, 'RepaymentFreq', text, 2, Mandatory),
	(80, 'LastPaymentAmount', number, 15, Mandatory),
	(81, 'LastPaymentDate', date, 8, RequiredConditional),
	(82, 'NextPaymentDate', date, 8, RequiredConditional),
	(83, 'CurBal', number, 15, Mandatory),
	(84, 'CurBalIndicator', text, 1, Mandatory),
	(85, 'AssetClassification', text, 1, IfAvailable),
	(86, 'AmountInArrears', number, 15, Mandatory),
	(87, 'ArrearsStartDate', date, 8, IfAvailable),
	(88, 'NDIA', number, 3, Mandatory),
	(89, 'PaymentHistoryProfile', text, 1, IfAvailable),
	(90, 'AmtOverdue1to30days', number, 15, IfAvailable),
	(91, 'AmtOverdue31to60days', number, 15, IfAvailable),
	(92, 'AmtOverdue11to90days', number, 15, IfAvailable),
	(93, 'AmtOverdue91to120days', number, 15, IfAvailable),
	(94, 'AmtOverdue121to150days', number, 15, IfAvailable),
	(95, 'AmtOverdue151to180days', number, 15, IfAvailable),
	(96, 'AmtOverdue181orMore', number, 15, IfAvailable),
	(97, 'LegalFlag', text, 3, IfAvailable),
	(98, 'FacilityStatusCode', text, 3, Mandatory),
	(99, 'FacilityStatusDate', date, 8, Mandatory),
	(100, 'ClosedDate', date, 8, RequiredConditional),
	(101, 'ClosureReason', text, 3, RequiredConditional),
	(102, 'WrittenOffAmt', number, 15, RequiredConditional),
	(103, 'ReasonForWrittenOff', text, 1, RequiredConditional),
	(104, 'DateRestructured', date, 8, RequiredConditional),
	(105, 'ReasonForRestructure', text, 1, RequiredConditional),
	(106, 'CreditCollateralInd', text, 3, Mandatory),
	(107, 'SecurityType', text, 3, RequiredConditional),
	(108, 'NatureOfCharge', text, 1, RequiredConditional),
	(109, 'SecurityValue', number, 15, RequiredConditional),
	(110, 'CollRegRefNum', text, 15, RequiredConditional),
	(111, 'SpecialCommentsCode', text, 3, IfAvailable),
	(112, 'NatureOfGuarantor', text, 3, Mandatory),
	(113, 'NameOfComGuarantor', text, 50, RequiredConditional),
	(114, 'BusRegOfGuarantor', text, 20, RequiredConditional),
	(115, 'G1Surname', text, 60, RequiredConditional),
	(116, 'G1FirstName', text, 60, RequiredConditional),
	(117, 'G1MiddleNames', text, 60, IfAvailable),
	(118, 'G1NatID', text, 20, RequiredConditional),
	(119, 'G1VotID', text, 20, RequiredConditional),
	(120, 'G1DrivLic', text, 20, RequiredConditional),
	(121, 'G1PassNum', text, 20, RequiredConditional),
	(122, 'G1SSN', text, 20, IfAvailable),
	(123, 'G1Gender', text, 1, RequiredConditional),
	(124, 'G1DOB', date, 8, RequiredConditional),
	(125, 'G1Add1', text, 100, IfAvailable),
	(126, 'G1Add2', text, 50, IfAvailable),
	(127, 'G1Add3', text, 50, IfAvailable),
	(128, 'G1HomeTel', text, 30, IfAvailable),
	(129, 'G1WorkTel', text, 30, IfAvailable),
	(130, 'G1Mobile', text, 30, IfAvailable),
	(131, 'G2Surname', text, 60, IfAvailable),
	(132, 'G2FirstName', text, 60, IfAvailable),
	(133, 'G2MiddleNames', text, 60, IfAvailable),
	(134, 'G2NatID', text, 20, RequiredConditional),
	(135, 'G2VotID', text, 20, RequiredConditional),
	(136, 'G2DrivLic', text, 20, RequiredConditional),
	(137, 'G2PassNum', text, 20, RequiredConditional),
	(138, 'G2SSN', text, 20, IfAvailable),
	(139, 'G2Gender', text, 1, RequiredConditional),
	(140, 'G2DOB', date, 8, RequiredConditional),
	(141, 'G2Add1', text, 100, IfAvailable),
	(142, 'G2Add2', text, 50, IfAvailable),
	(143, 'G2Add3', text, 50, IfAvailable),
	(144, 'G2HomeTel', text, 30, IfAvailable),
	(145, 'G2WorkTel', text, 30, IfAvailable),
	(146, 'G2Mobile', text, 30, IfAvailable),
	(147, 'G3Surname', text, 60, IfAvailable),
	(148, 'G3FirstName', text, 60, IfAvailable),
	(149, 'G3MiddleNames', text, 60, IfAvailable),
	(150, 'G3NatID', text, 20, RequiredConditional),
	(151, 'G3VotID', text, 20, RequiredConditional),
	(152, 'G3DrivLic', text, 20, RequiredConditional),
	(153, 'G3PassNum', text, 20, RequiredConditional),
	(154, 'G3SSN', text, 20, IfAvailable),
	(155, 'G3Gender', text, 1, RequiredConditional),
	(156, 'G3DOB', date, 8, RequiredConditional),
	(157, 'G3Add1', text, 100, IfAvailable),
	(158, 'G3Add2', text, 50, IfAvailable),
	(159, 'G3Add3', text, 50, IfAvailable),
	(160, 'G3HomeTel', text, 30, IfAvailable),
	(161, 'G3WorkTel', text, 30, IfAvailable),
	(162, 'G3Mobile', text, 30, IfAvailable),
	(163, 'G4Surname', text, 60, IfAvailable),
	(164, 'G4FirstName', text, 60, IfAvailable),
	(165, 'G4MiddleNames', text, 60, IfAvailable),
	(166, 'G4NatID', text, 20, RequiredConditional),
	(167, 'G4VotID', text, 20, RequiredConditional),
	(168, 'G4DrivLic', text, 20, RequiredConditional),
	(169, 'G4PassNum', text, 20, RequiredConditional),
	(170, 'G4SSN', text, 20, IfAvailable),
	(171, 'G4Gender', text, 1, RequiredConditional),
	(172, 'G4DOB', date, 8, RequiredConditional),
	(173, 'G4Add1', text, 100, IfAvailable),
	(174, 'G4Add2', text, 50, IfAvailable),
	(175, 'G4Add3', text, 50, IfAvailable),
	(176, 'G4HomeTel', text, 30, IfAvailable),
	(177, 'G4WorkTel', text, 30, IfAvailable),
	(178, 'G4Mobile', text, 30, IfAvailable),
)


headers = tuple([x[1] for x in FIELDS])

def row(data):
	values = [FIELDS[i][FIELD_TYPE](data.get(headers[i], None)) for i in range(len(headers))]
	values[0] = 'D'
	if values[1] is '':
		values[1] = '0'
	for i, value in enumerate(values):
		field = FIELDS[i]
		if field[FIELD_OPTIONS] is Mandatory and value is '':
			raise ValueError('Mandatory field cannot be blank for %d - %s' % (field[FIELD_NO], field[FIELD_NAME]))
	return '|'.join([str(x if x else '') for x in values])

def validate(row):
	values = row.split('|')
	for i, value in enumerate(values):
		pass