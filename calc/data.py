data = {}
back = 0

applied = [105, 202, 402, 404, 501, 505]
core = [201, 204, 301, 302, 303, 304, 401, 403, 405, 502, 503, 504]
humanities = [101,102,103,104, 203, 205, 305]

credit_4 = [101, 102, 103, 104, 105,201, 202, 203, 204, 205,301, 302, 303, 304, 305,401, 402, 403, 404, 405,501, 502, 503, 504, 505,601, 602, 603, 604, 605,701, 702, 703, 704, 705, 801, 802, 803, 806]
credit_3 = [106, 309, 709]
credit_2 = [107, 108, 109, 206, 207, 208, 209, 306, 307, 308, 406, 407, 408, 409, 410, 506, 507, 508, 606, 607, 608, 610, 706, 707, 708, 804]
credit_1 = [310, 411, 412, 509, 609, 710, 807]
credit_8 = [805]

subject = {
	'101': 'Humanities',
	'102': 'Mathematics I',
	'103': 'Physics I',
	'104': 'Chemistry',
	'105': 'Manufacturing Processes',
	'106': 'Engineering Drawing',
	'107': 'Physics I Lab',
	'108': 'Chemitsry Lab',
	'109': 'Workshop I',
	'201': 'Principles of Electrical Engineering',
	'202': 'Applied Mechanics',
	'203': 'Mathematics II',
	'204': 'Introduction to Programming',
	'205': 'Physics of Materials',
	'206': 'Principles of Electrical Engineering Lab',
	'207': 'Applied Mechnics Lab',
	'208': 'Introduction to Programming Lab',
	'209': 'Physics of Materials Lab',
	'301': 'Electronics I',
	'302': 'Circuit and Systems',
	'303': 'Power Apparatus',
	'304': 'Electrical Measurements',
	'305': 'Mathematics III',
	'306': 'Electronics I Lab',
	'307': 'Power Apparatus Lab',
	'308': 'Electrical Measurement Lab',
	'309': 'Machine Drawing',
	'310': 'Programming I',
	'401': 'Electronics II',
	'402': 'Fluid Mechanics and Thermodynamics',
	'403': 'Electronic Instrumentation and Measurements',
	'404': 'Computer Graphics',
	'405': 'Transducers and Components',
	'406': 'Electronics II Lab',
	'407': 'Computer Graphics Lab',
	'408': 'Instrumentation Lab',
	'409': 'Electrical Workshop and Electrical Drawing Lab',
	'410': 'Practical Training',
	'411': 'Report Writing',
	'412': 'Programming II',
	'501': 'Analog and Digital Communication',
	'502': 'Industrial and Analytical Instruments',
	'503': 'Digital Integrated Circuits I',
	'504': 'Linear Integrated Circuits',
	'505': 'Industrial Organisation and Managerial Economics',
	'506': 'Analog and Digital Communication Lab',
	'507': 'Digital Integrated Circuits I Lab',
	'508': 'Linear Integrated Circuits Lab',
	'509': 'Programming III Lab',
	'601': 'Microprocessors',
	'602': 'Computer Aided Design',
	'603': 'Industrial Electronics',
	'604': 'Control Systems I',
	'605': 'Telemetry and Data Transmission',
	'606': 'Microprocessor Lab',
	'607': 'Computer Aided Design Lab',
	'608': 'Control Systems I Lab',
	'609': 'Programming IV Lab',
	'610': 'Practical Training',
	'701': 'Control Sytems II',
	'702': 'Digital Integrated Circuits II',
	'703': 'Process Control',
	'704': 'Elective I',
	'705': 'Elective II',
	'706': 'Control Systems Lab',
	'707': 'Digital Integrated Circuits II Lab',
	'708': 'Instrumentation Lab',
	'709': 'Practical Training',
	'710': 'Programming V',
	'801': 'Consumer Electronics',
	'802': 'Elective III',
	'803': 'Elective IV',
	'804': 'Elective III & IV Lab',
	'805': 'Major Project',
	'806': 'Practical Training',
	'807': 'Seminar Reports',
}
