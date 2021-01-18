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
    (0, 'risk_forms'),
    (1, 'med_forms'),
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