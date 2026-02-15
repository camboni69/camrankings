# NCAA Division I Conference Mappings
# Format: "School Name": "Conference"

# HOW TO ADD SCHOOLS:
# If you see schools in the "Other" category that should be in a conference:
# 1. Find the school name in your TFRRS data (check the exact spelling)
# 2. Add a line like: "School Name": "Conference",
# 3. Re-run: python3 daily_update.py
# 4. Upload the new sample_data.js to GitHub
#
# IMPORTANT: School names must match EXACTLY how they appear in TFRRS

CONFERENCE_MAP = {
    # SEC
    "Alabama": "SEC",
    "Arkansas": "SEC",
    "Auburn": "SEC",
    "Florida": "SEC",
    "Georgia": "SEC",
    "Kentucky": "SEC",
    "LSU": "SEC",
    "Mississippi": "SEC",
    "Ole Miss": "SEC",
    "Miss State": "SEC",
    "Missouri": "SEC",
    "South Carolina": "SEC",
    "Tennessee": "SEC",
    "Texas A&M": "SEC",
    "Vanderbilt": "SEC",
    "Texas": "SEC",
    "Oklahoma": "SEC",
    
    # Big Ten
    "Illinois": "Big Ten",
    "Indiana": "Big Ten",
    "Iowa": "Big Ten",
    "Maryland": "Big Ten",
    "Michigan": "Big Ten",
    "Michigan State": "Big Ten",
    "Minnesota": "Big Ten",
    "Nebraska": "Big Ten",
    "Northwestern": "Big Ten",
    "Ohio State": "Big Ten",
    "Penn State": "Big Ten",
    "Purdue": "Big Ten",
    "Rutgers": "Big Ten",
    "Wisconsin": "Big Ten",
    "UCLA": "Big Ten",
    "USC": "Big Ten",
    "Oregon": "Big Ten",
    "Washington": "Big Ten",
    
    # Big 12
    "Baylor": "Big 12",
    "BYU": "Big 12",
    "Cincinnati": "Big 12",
    "Colorado": "Big 12",
    "Houston": "Big 12",
    "Iowa State": "Big 12",
    "Kansas": "Big 12",
    "Kansas State": "Big 12",
    "Oklahoma State": "Big 12",
    "TCU": "Big 12",
    "Texas Tech": "Big 12",
    "UCF": "Big 12",
    "Utah": "Big 12",
    "West Virginia": "Big 12",
    "Arizona": "Big 12",
    "Arizona State": "Big 12",
    
    # ACC
    "Boston College": "ACC",
    "Clemson": "ACC",
    "Duke": "ACC",
    "Florida State": "ACC",
    "Georgia Tech": "ACC",
    "Louisville": "ACC",
    "Miami (Fla.)": "ACC",
    "North Carolina": "ACC",
    "NC State": "ACC",
    "Notre Dame": "ACC",
    "Pittsburgh": "ACC",
    "Syracuse": "ACC",
    "Virginia": "ACC",
    "Virginia Tech": "ACC",
    "Wake Forest": "ACC",
    "California": "ACC",
    "Stanford": "ACC",
    "SMU": "ACC",
    
    # Pac-12 (remaining schools)
    "Washington State": "Pac-12",
    "Oregon State": "Pac-12",
    
    # Mountain West
    "Air Force": "Mountain West",
    "Boise State": "Mountain West",
    "Colorado State": "Mountain West",
    "Fresno State": "Mountain West",
    "Hawaii": "Mountain West",
    "Nevada": "Mountain West",
    "New Mexico": "Mountain West",
    "San Diego State": "Mountain West",
    "San Jose State": "Mountain West",
    "UNLV": "Mountain West",
    "Utah State": "Mountain West",
    "Wyoming": "Mountain West",
    
    # American Athletic
    "Charlotte": "American",
    "East Carolina": "American",
    "FAU": "American",
    "Memphis": "American",
    "Navy": "American",
    "North Texas": "American",
    "Rice": "American",
    "South Florida": "American",
    "Temple": "American",
    "Tulane": "American",
    "Tulsa": "American",
    "UAB": "American",
    "UTSA": "American",
    
    # Conference USA
    "FIU": "C-USA",
    "Jacksonville State": "C-USA",
    "Liberty": "C-USA",
    "Louisiana Tech": "C-USA",
    "Middle Tennessee": "C-USA",
    "New Mexico State": "C-USA",
    "Sam Houston": "C-USA",
    "UTEP": "C-USA",
    "Western Kentucky": "C-USA",
    
    # Sun Belt
    "App State": "Sun Belt",
    "Arkansas State": "Sun Belt",
    "Coastal Carolina": "Sun Belt",
    "Georgia Southern": "Sun Belt",
    "Georgia State": "Sun Belt",
    "James Madison": "Sun Belt",
    "Louisiana": "Sun Belt",
    "Marshall": "Sun Belt",
    "Old Dominion": "Sun Belt",
    "South Alabama": "Sun Belt",
    "Southern Miss": "Sun Belt",
    "Texas State": "Sun Belt",
    "Troy": "Sun Belt",
    "ULM": "Sun Belt",
    
    # MAC
    "Akron": "MAC",
    "Ball State": "MAC",
    "Bowling Green": "MAC",
    "Buffalo": "MAC",
    "Central Michigan": "MAC",
    "Eastern Michigan": "MAC",
    "Kent State": "MAC",
    "Miami (Ohio)": "MAC",
    "Northern Illinois": "MAC",
    "Ohio": "MAC",
    "Toledo": "MAC",
    "Western Michigan": "MAC",
    
    # Ivy League
    "Brown": "Ivy League",
    "Columbia": "Ivy League",
    "Cornell": "Ivy League",
    "Dartmouth": "Ivy League",
    "Harvard": "Ivy League",
    "Penn": "Ivy League",
    "Princeton": "Ivy League",
    "Yale": "Ivy League",
    
    # Big East
    "Butler": "Big East",
    "Creighton": "Big East",
    "DePaul": "Big East",
    "Georgetown": "Big East",
    "Marquette": "Big East",
    "Providence": "Big East",
    "Seton Hall": "Big East",
    "St. John's": "Big East",
    "Villanova": "Big East",
    "Xavier": "Big East",
    
    # Big Sky
    "Eastern Washington": "Big Sky",
    "Idaho": "Big Sky",
    "Idaho State": "Big Sky",
    "Montana": "Big Sky",
    "Montana State": "Big Sky",
    "Northern Arizona": "Big Sky",
    "Northern Colorado": "Big Sky",
    "Portland State": "Big Sky",
    "Sacramento State": "Big Sky",
    "Weber State": "Big Sky",
    
    # Big West
    "Cal Poly": "Big West",
    "CS Bakersfield": "Big West",
    "CS Fullerton": "Big West",
    "CS Northridge": "Big West",
    "Long Beach State": "Big West",
    "UC Davis": "Big West",
    "UC Irvine": "Big West",
    "UC Riverside": "Big West",
    "UC San Diego": "Big West",
    "UC Santa Barbara": "Big West",
    
    # Atlantic 10
    "Davidson": "Atlantic 10",
    "Dayton": "Atlantic 10",
    "Duquesne": "Atlantic 10",
    "Fordham": "Atlantic 10",
    "George Mason": "Atlantic 10",
    "George Washington": "Atlantic 10",
    "La Salle": "Atlantic 10",
    "Loyola Chicago": "Atlantic 10",
    "Massachusetts": "Atlantic 10",
    "Rhode Island": "Atlantic 10",
    "Richmond": "Atlantic 10",
    "Saint Joseph's": "Atlantic 10",
    "Saint Louis": "Atlantic 10",
    "St. Bonaventure": "Atlantic 10",
    "VCU": "Atlantic 10",
    
    # WCC
    "Gonzaga": "WCC",
    "Loyola Marymount": "WCC",
    "Pacific": "WCC",
    "Pepperdine": "WCC",
    "Portland": "WCC",
    "Saint Mary's": "WCC",
    "San Diego": "WCC",
    "San Francisco": "WCC",
    "Santa Clara": "WCC",
    
    # Colonial
    "Campbell": "Colonial",
    "Charleston": "Colonial",
    "Delaware": "Colonial",
    "Drexel": "Colonial",
    "Elon": "Colonial",
    "Hampton": "Colonial",
    "Hofstra": "Colonial",
    "Monmouth": "Colonial",
    "Northeastern": "Colonial",
    "Stony Brook": "Colonial",
    "Towson": "Colonial",
    "UNC Wilmington": "Colonial",
    "William & Mary": "Colonial",
    
    # Independents & Other
    "Army": "Independent",
    "UConn": "Independent",
}

def get_conference(school_name):
    """
    Get conference for a school, handling variations in naming.
    Returns "Other" if school not found.
    """
    # Direct lookup
    if school_name in CONFERENCE_MAP:
        return CONFERENCE_MAP[school_name]
    
    # Try some common variations
    variations = [
        school_name.replace("State", "St."),
        school_name.replace("St.", "State"),
        school_name.replace("University", "").strip(),
        school_name.replace("(Fla.)", "Florida"),
    ]
    
    for variant in variations:
        if variant in CONFERENCE_MAP:
            return CONFERENCE_MAP[variant]
    
    # Default to "Other" for unrecognized schools
    return "Other"
