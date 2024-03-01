import geocoder as geo
bing_api_key = "xUBhOh74QkgPNlf6lC97~bvDde5sihSdE87MsCCDcjQ~AlwsrntknIdP0Z_oHgN_oSqy0GiJvz1QlahyjVDjWdlG0zFudMXMPcSpWm5LOJ0O"

"""
This helper function creates the vectorized query input using user values from frontend.py.
@param skill_level: An integer between 0 and 100 that represents the user's experience level
@param location_filter: 0 if the location param is a City and 1 if the location param is a State
@param location: A City or State name depending on the location_filter parameter
@param month: A integer from 1 to 12 corresponding to a month in the year
@return: A list of values in the following order: Difficulty Rating, Latitude, Longitude, followed by 12 month indicators. 
         Returns -1 if the location param is invalid.
"""
def build_query_vector(skill_level, location, month):
    # Skill level needs to be converted to an integer between -100 and 100
    vector = list()
    vector.append(int(-100 + 2*skill_level))

    # Location needs to be converted from city/state name to lat/long
    g = geo.bing(location, key=bing_api_key)
    result = g.json
    if result is None:
        return -1
    vector.append(result['lat'] * 8 - 200)
    vector.append(result['lng'] * 7.273 + 909.125)

    # Month needs to be expanded into 12 indicators
    for i in range(1, 13):
        if (month == i):
            vector.append(1)
        else:
            vector.append(0)

    return vector
