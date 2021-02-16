import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Do city-country input like 'Santiago, Chile' work?"""
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do city-country-population inputs work?"""
        city_country = get_city_country('santiago', 'chile', population=5000000)
        self.assertEqual(city_country, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()