DISTRICTS = {

    "Bengaluru Urban": {
        "id": 1,
        "population": 12300000,
        "literacy": 89.0,
        "urban": 92,
        "latitude": 12.9716,
        "longitude": 77.5946,
        "crime_profile": {
            "Cyber Crime": 0.30,
            "Vehicle Theft": 0.22,
            "Fraud": 0.18,
            "Robbery": 0.10,
            "Murder": 0.05,
            "Drug Offence": 0.08,
            "Others": 0.07
        }
    },

    "Mysuru": {
        "id": 2,
        "population": 3200000,
        "literacy": 81,
        "urban": 64,
        "latitude": 12.2958,
        "longitude": 76.6394,
        "crime_profile": {
            "Burglary": 0.28,
            "Robbery": 0.20,
            "Vehicle Theft": 0.18,
            "Fraud": 0.12,
            "Murder": 0.07,
            "Others": 0.15
        }
    },

    "Dakshina Kannada": {
        "id": 3,
        "population": 2100000,
        "literacy": 89,
        "urban": 48,
        "latitude": 12.9141,
        "longitude": 74.8560,
        "crime_profile": {
            "Drug Offence": 0.26,
            "Smuggling": 0.18,
            "Cyber Crime": 0.12,
            "Fraud": 0.18,
            "Others": 0.26
        }
    }
}

CRIME_HEADS = {
    1: "Murder",
    2: "Attempt to Murder",
    3: "Robbery",
    4: "Burglary",
    5: "Vehicle Theft",
    6: "Cyber Crime",
    7: "Drug Offence",
    8: "Kidnapping",
    9: "Fraud",
    10: "Domestic Violence",
    11: "Assault",
    12: "Missing Person"
}

OFFICER_RANKS = [

    "Police Constable",
    "Head Constable",
    "Assistant Sub Inspector",
    "Sub Inspector",
    "Inspector",
    "Circle Inspector",
    "Deputy Superintendent",
    "Superintendent"

]

WEAPONS = [

    "Knife",
    "Pistol",
    "Iron Rod",
    "Crowbar",
    "Stick",
    "Hands",
    "Unknown"

]

VEHICLE_TYPES = [
    "Motorcycle",
    "Scooter",
    "Car",
    "SUV",
    "Auto Rickshaw",
    "Truck",
    "Bus",
    "Van"
]

VEHICLE_COLORS = [
    "White",
    "Black",
    "Silver",
    "Red",
    "Blue",
    "Grey",
    "Green",
    "Yellow"
]

VEHICLE_BRANDS = [
    "Maruti Suzuki",
    "Hyundai",
    "Tata",
    "Mahindra",
    "Honda",
    "Toyota",
    "Kia",
    "Royal Enfield",
    "Hero",
    "Bajaj",
    "TVS"
]

OCCUPATIONS = [
    "Student",
    "Engineer",
    "Doctor",
    "Teacher",
    "Business",
    "Farmer",
    "Driver",
    "Labourer",
    "Software Engineer",
    "Government Employee",
    "Private Employee",
    "Police",
    "Retired"
]

SEASONS = {

    "Summer": {

        "Vehicle Theft": 1.2,
        "Assault": 1.1

    },

    "Monsoon": {

        "Burglary": 1.3

    },

    "Festival": {

        "Fraud": 1.4,
        "Vehicle Theft": 1.6,
        "Robbery": 1.5

    },

    "Election": {

        "Assault": 1.5,
        "Murder": 1.2

    }
}

TIME_SLOTS = {

    "Morning": (6, 11),
    "Afternoon": (12, 17),
    "Evening": (18, 21),
    "Night": (22, 5)

}

AGE_GROUPS = {

    "Juvenile": (12,17),
    "Young Adult": (18,30),
    "Adult": (31,50),
    "Senior": (51,75)

}

POLICE_STATIONS = {
    "Bengaluru Urban": [
        {"name": "Whitefield Police Station", "type": "Urban"},
        {"name": "Indiranagar Police Station", "type": "Urban"},
        {"name": "HAL Police Station", "type": "Urban"},
        {"name": "Electronic City Police Station", "type": "Urban"},
        {"name": "Koramangala Police Station", "type": "Urban"},
        {"name": "Jayanagar Police Station", "type": "Urban"},
        {"name": "Banashankari Police Station", "type": "Urban"},
        {"name": "Malleswaram Police Station", "type": "Urban"},
        {"name": "Yelahanka Police Station", "type": "Urban"},
        {"name": "Hebbal Police Station", "type": "Urban"}
    ],

    "Mysuru": [
        {"name": "Lashkar Police Station", "type": "Urban"},
        {"name": "Nazarbad Police Station", "type": "Urban"},
        {"name": "Vijayanagar Police Station", "type": "Urban"},
        {"name": "Mysuru South Police Station", "type": "Urban"},
        {"name": "Mysuru East Police Station", "type": "Urban"}
    ],

    "Dakshina Kannada": [
        {"name": "Mangaluru North Police Station", "type": "Urban"},
        {"name": "Mangaluru South Police Station", "type": "Urban"},
        {"name": "Bantwal Police Station", "type": "Semi Urban"},
        {"name": "Moodbidri Police Station", "type": "Semi Urban"},
        {"name": "Surathkal Police Station", "type": "Urban"}
    ]
}

CRIME_SUBHEADS = {

    "Murder": [
        "Contract Killing",
        "Family Dispute",
        "Gang Rivalry",
        "Property Dispute"
    ],

    "Attempt to Murder": [
        "Knife Attack",
        "Firearm Attack",
        "Personal Rivalry"
    ],

    "Robbery": [
        "Bank Robbery",
        "Street Robbery",
        "House Robbery"
    ],

    "Burglary": [
        "House Break-in",
        "Shop Burglary",
        "Office Burglary"
    ],

    "Vehicle Theft": [
        "Motorcycle Theft",
        "Car Theft",
        "Truck Theft",
        "Auto Rickshaw Theft"
    ],

    "Cyber Crime": [
        "UPI Fraud",
        "Phishing",
        "Identity Theft",
        "Credit Card Fraud",
        "Social Media Scam"
    ],

    "Drug Offence": [
        "Drug Possession",
        "Drug Trafficking",
        "Drug Manufacturing"
    ],

    "Kidnapping": [
        "Child Kidnapping",
        "Ransom Kidnapping",
        "Human Trafficking"
    ],

    "Fraud": [
        "Insurance Fraud",
        "Loan Fraud",
        "Investment Scam"
    ],

    "Domestic Violence": [
        "Physical Abuse",
        "Mental Abuse",
        "Dowry Harassment"
    ],

    "Assault": [
        "Simple Assault",
        "Aggravated Assault",
        "Public Fight"
    ],

    "Missing Person": [
        "Child Missing",
        "Adult Missing",
        "Senior Citizen Missing"
    ]
}

DEPARTMENTS = [
    "Law & Order",
    "Crime",
    "Cyber Crime",
    "Traffic",
    "Administration",
    "Intelligence"
]

RELIGIONS = [
    "Hindu",
    "Muslim",
    "Christian",
    "Sikh",
    "Jain",
    "Buddhist"
]

MARITAL_STATUS = [
    "Single",
    "Married",
    "Divorced",
    "Widowed"
]

EDUCATION = [
    "Primary",
    "High School",
    "PUC",
    "Diploma",
    "Graduate",
    "Post Graduate"
]

CASE_STATUS = [
    "Under Investigation",
    "Charge Sheet Filed",
    "Pending Trial",
    "Closed"
]

MODUS_OPERANDI = [
    "Forced Entry",
    "Duplicate Key",
    "Social Engineering",
    "Fake Identity",
    "Online Scam",
    "ATM Skimming",
    "Vehicle Lock Break",
    "Knife Attack",
    "Firearm",
    "Poisoning",
    "Physical Assault"
]

CASE_PRIORITY = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

EVIDENCE_TYPES = [
    "Fingerprint",
    "DNA Sample",
    "Blood Sample",
    "Knife",
    "Firearm",
    "Mobile Phone",
    "Laptop",
    "Hard Disk",
    "CCTV Footage",
    "Vehicle",
    "Clothing",
    "Drug Sample",
    "Document",
    "SIM Card",
    "USB Drive"
]

EVIDENCE_STATUS = [
    "Collected",
    "Sent to FSL",
    "Verified",
    "Pending Analysis",
    "Rejected"
]

GANG_TYPES = [
    "Drug Syndicate",
    "Vehicle Theft Gang",
    "Cyber Crime Ring",
    "Human Trafficking",
    "Extortion Group",
    "Contract Killers",
    "Illegal Mining",
    "Financial Fraud Network"
]

ARREST_STATUS = [
    "Arrested",
    "Absconding",
    "Bail",
    "Unknown"
]

GANG_NAMES = [
    "Black Cobra",
    "Shadow Wolves",
    "Iron Tigers",
    "Silent Fox",
    "Night Hawks",
    "Red Scorpions",
    "Ghost Riders",
    "Golden Syndicate",
    "Dark Network",
    "Silver Kings"
]

COURTS = [
    "Bengaluru Sessions Court",
    "Mysuru District Court",
    "Mangaluru District Court",
    "Hubballi District Court",
    "Belagavi Sessions Court",
    "Kalaburagi District Court"
]