BS_MONTHS = [
    (1, "वैशाख"),
    (2, "जेष्ठ"),
    (3, "असार"),
    (4, "श्रावण"),
    (5, "भदौ"),
    (6, "आश्विन"),
    (7, "कार्तिक"),
    (8, "मंसिर"),
    (9, "पौष"),
    (10, "माघ"),
    (11, "फाल्गुण"),
    (12, "चैत्र"),
]

DEVANAGARI_DIGITS = (
    "०",
    "१",
    "२",
    "३",
    "४",
    "५",
    "६",
    "७",
    "८",
    "९"
)

STATES = [
    ('draft', 'Draft'),
    ('submitted', 'Submitted'),
]

STATUS = [
    ('started', 'STARTED'),
    ('incomplete', 'INCOMPLETE'),
    ('submitted', 'SUBMITTED'),
    ('completed', 'COMPLETED'),
]

CH_STATE = [
    (0, 'fund_receipt_expense'),
    (1, 'risk_allowance'),
    (2, 'medical_expense'),
    (3, 'medical_receipt'),
    (4, 'medical_use'),
    (5, 'med_purchase_desc'),
    (6, 'pcr_test_compliance_detail'),
    (7, 'pcr_lab_detail'),
    (8, 'rdt_test_detail'),
    (9, 'pcr_kit_usage'),
    (10, 'covid_hos_mainpower'),
    (11, 'cov_hos_equipment'),
    (12, 'covid_hospital_detail'),
    (13, 'quarantine_management_detail'),
    (14, 'isolation_management_detail'),
    (15, 'quarantine_contruction_expenditure'),
    (16, 'isolation_construction_expenditure'),
    (17, 'cov_hos_management_checklist'),
]

PROVINCE_STATE = [
    (0, 'epidemic_outbreak_prep'),
    (1, 'fund_receipt_expense'),
    (2, 'risk_allowance'),
    (3, 'medical_expense'),
    (4, 'medical_receipt'),
    (5, 'medical_use'),
    (6, 'med_purchase_desc'),
    (7, 'pcr_test_compliance_detail'),
    (8, 'pcr_lab_detail'),
    (9, 'rdt_test_detail'),
    (10, 'pcr_kit_usage'),
    (11, 'covid_hos_mainpower'),
    (12, 'cov_hos_equipment'),
    (13, 'covid_hospital_detail'),
    (14, 'quarantine_management_detail'),
    (15, 'isolation_management_detail'),
    (16, 'quarantine_contruction_expenditure'),
    (17, 'isolation_construction_expenditure'),
    (18, 'district_covid_management'),
]

INTERNAL_AFFAIRS_STATE = [
    (0, 'epidemic_outbreak_prep'),
    (1, 'fund_receipt_expense'),
    (2, 'risk_allowance'),
    (3, 'action_plan_implementation'),
]

def num_to_devanagari(num):
    """
    Utility function to convert an integer number to Devanagari
    """
    dev_num = ''
    if type(num) != int:
        return -1

    for digit in str(num):
        dev_num += DEVANAGARI_DIGITS[int(digit)]

    return dev_num
