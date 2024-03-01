"""
This module contains helper code for the streamlit front end application.

Usage: build_query_vector(50, "Seattle", 10)
"""

import geocoder as geo
BING_API_KEY = """xUBhOh74QkgPNlf6lC97~bvDde5sihSdE87MsCCDc
    jQ~AlwsrntknIdP0Z_oHgN_oSqy0GiJvz1QlahyjVDjWdlG0zFudMXMPcSpWm5LOJ0O"""

def build_query_vector(skill_level, location, month):
    """
    This helper function creates the vectorized query input using user values from frontend.py.

    parameters:
        skill_level: An integer between 0 and 100 that represents the user's experience level
        location_filter: 0 if the location param is a City and 1 if the location param is a State
        location: A City or State name depending on the location_filter parameter
        month: A integer from 1 to 12 corresponding to a month in the year

    returns: A list of values in the following order: Difficulty Rating, scaled latitude, 
             scaled longitude, followed by 12 month indicators. Returns -1 if the location 
             param is invalid.
    """
    # Skill level needs to be converted to an integer between -100 and 100
    vector = []
    vector.append(int(-100 + 2*skill_level))

    # Location needs to be converted from city/state name to lat/long
    g = geo.bing(location, key=BING_API_KEY)
    result = g.json
    if result is None:
        return -1
    vector.append(result['lat'] * 8 - 200)
    vector.append(result['lng'] * 7.273 + 909.125)

    # Month needs to be expanded into 12 indicators
    for i in range(1, 13):
        if month == i:
            vector.append(1)
        else:
            vector.append(0)

    return vector
