"""
Module containing the test cases for the frontend modules.

Contains the test cases for
- frontend.py - create_display and UI
- frontendutil.py - build_query_vector
"""

import unittest

import pandas as pd
from streamlit.testing.v1 import AppTest

# pylint: disable=import-error
from frontendutil import build_query_vector


class TestFrontEnd(unittest.TestCase):
    """
    Class to contain the test cases for the frontendutil module
    """

    def test_frontend_smoke(self):
        """
        Smoke test to see if the frontend app
        can be run without failing.
        """

        AppTest.from_file("frontend.py").run()

    def test_frontend_smoke_with_query(self):
        """
        Smoke test to see if the frontend app
        can perform a search without failing.
        """

        at = AppTest.from_file("frontend.py").run()
        at.text_input[0].set_value("Seattle").run()
        at.date_input[0].set_value(pd.to_datetime("2023-04-04")).run()
        at.button[0].click().run()

    def test_frontend_valid_query_1(self):
        """
        Test if the front end app can make a search
        with a user inputted city name.
        """

        at = AppTest.from_file("frontend.py").run()
        at.text_input[0].set_value("Seattle").run()
        at.date_input[0].set_value(pd.to_datetime("2023-04-04")).run()
        at.button[0].click().run()

        self.assertEqual(at.table[0].value.loc[0]["Resort Name"], "Crystal Mountain-WA-")
        self.assertEqual(at.table[0].value.loc[1]["Resort Name"], "The Summit at Snoqualmie")

    def test_frontend_valid_query_2(self):
        """
        Test if the front end app can make a search
        with a user inputted state name.
        """

        at = AppTest.from_file("frontend.py").run()
        at.text_input[0].set_value("Utah").run()
        at.date_input[0].set_value(pd.to_datetime("2023-04-04")).run()
        at.button[0].click().run()

        self.assertEqual(at.table[0].value.loc[0]["Resort Name"], "Alta")
        self.assertEqual(at.table[0].value.loc[1]["Resort Name"], "Solitude")

    def test_frontend_valid_query_one_result(self):
        """
        Test if the front end app can make a search
        with a user inputted city name when the result
        is only a single resort.
        """

        at = AppTest.from_file("frontend.py").run()
        at.text_input[0].set_value("Seattle").run()
        at.date_input[0].set_value(pd.to_datetime("2023-04-04")).run()
        at.slider[0].set_value(35)
        at.button[0].click().run()

        self.assertEqual(at.table[0].value.loc[0]["Resort Name"], "Summit Ski Area at Mt. Hood")
        self.assertEqual(at.table[0].value.loc[0]["Relative Price"], "Relative Price Unavailable")

    def test_frontend_valid_query_no_results(self):
        """
        Test if the front end app can make a search
        with a user inputted city name when the result
        contains no resorts.
        """

        at = AppTest.from_file("frontend.py").run()
        at.text_input[0].set_value("Seattle").run()
        at.date_input[0].set_value(pd.to_datetime("2023-04-04")).run()
        at.slider[0].set_value(10)
        at.button[0].click().run()

        self.assertEqual(at.error[0].value, "No results found")

    def test_frontend_bad_query_invalid_location(self):
        """
        Test if the front end app displays an error message
        when the user inputs an invalid location.
        """

        at = AppTest.from_file("frontend.py").run()
        at.text_input[0].set_value("asdfghjkl").run()
        at.date_input[0].set_value(pd.to_datetime("2023-04-04")).run()
        at.slider[0].set_value(100)
        at.button[0].click().run()

        self.assertEqual(at.error[0].value, "Invalid Location")

    def test_build_query_vector_smoke(self):
        """
        Smoke test to see if the build_query_vector
        function can be called successfully.
        """

        skill_level = 50
        location = "Seattle"
        month = 3
        build_query_vector(skill_level, location, month)

    def test_build_query_vector_city_name(self):
        """
        Test for the user providing a city name.
        """

        skill_level = 50
        location = "Seattle"
        month = 3
        result = build_query_vector(skill_level, location, month)

        self.assertEqual(result[0], 0)
        self.assertEqual(round(result[1], 3), 180.826)
        self.assertEqual(round(result[2], 3), 19.417)

        for i in range(1, 13):
            if i == month:
                self.assertEqual(result[2 + i], 1)
            else:
                self.assertEqual(result[2 + i], 0)

    def test_build_query_vector_state_name(self):
        """
        Test for the user providing a state name.
        """

        skill_level = 35
        location = "Utah"
        month = 5
        result = build_query_vector(skill_level, location, month)

        self.assertEqual(result[0], -30)
        self.assertEqual(round(result[1], 3), 114.590)
        self.assertEqual(round(result[2], 3), 96.889)

        for i in range(1, 13):
            if i == month:
                self.assertEqual(result[2 + i], 1)
            else:
                self.assertEqual(result[2 + i], 0)

    def test_build_query_vector_invalid_name(self):
        """
        Test for the user providing an invalid name.
        """

        skill_level = 50
        location = "asdfghjkl"
        month = 3
        result = build_query_vector(skill_level, location, month)

        self.assertEqual(result, -1)
