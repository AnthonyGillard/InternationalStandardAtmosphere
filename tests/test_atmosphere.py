import unittest
from atmosphere import Atmosphere


class TestAtmosphere(unittest.TestCase):

    @staticmethod
    def create_atmosphere():
        return Atmosphere(288.15)

    def test_calculate_atmosphere_returns_expected_temp_at_0km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(0)

        self.assertAlmostEqual(288.15, conditions['temperature'])

    def test_calculate_atmosphere_returns_expected_pressure_at_0km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(0)

        self.assertAlmostEqual(1.01325e5, conditions['pressure'])

    def test_calculate_atmosphere_returns_expected_density_at_0km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(0)

        self.assertAlmostEqual(1.225, conditions['density'])

    def test_calculate_atmosphere_returns_expected_temp_at_5km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(5e3)

        self.assertAlmostEqual(255.67545824847247, conditions['temperature'])

    def test_calculate_atmosphere_returns_expected_pressure_at_5km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(5e3)

        self.assertAlmostEqual(54048.16782705765, conditions['pressure'])

    def test_calculate_atmosphere_returns_expected_density_at_5km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(5e3)

        self.assertAlmostEqual(0.7364275717, conditions['density'])

    def test_calculate_atmosphere_returns_expected_temp_at_15km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(15e3)

        self.assertAlmostEqual(216.65, conditions['temperature'])

    def test_calculate_atmosphere_returns_expected_pressure_at_15km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(15e3)

        self.assertAlmostEqual(12111.583535103531, conditions['pressure'])

    def test_calculate_atmosphere_returns_expected_density_at_15km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(15e3)

        self.assertAlmostEqual(0.19475128960438784, conditions['density'])

    def test_calculate_atmosphere_returns_expected_temp_at_25km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(25e3)

        self.assertAlmostEqual(221.55238950491957, conditions['temperature'])

    def test_calculate_atmosphere_returns_expected_pressure_at_25km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(25e3)

        self.assertAlmostEqual(2549.089455130193, conditions['pressure'])

    def test_calculate_atmosphere_returns_expected_density_at_25km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(25e3)

        self.assertAlmostEqual(0.040081756438850216, conditions['density'])

    def test_calculate_atmosphere_returns_expected_temp_at_40km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(40e3)

        self.assertAlmostEqual(250.3519632284201, conditions['temperature'])

    def test_calculate_atmosphere_returns_expected_pressure_at_40km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(40e3)

        self.assertAlmostEqual(287.1104191361581, conditions['pressure'])

    def test_calculate_atmosphere_returns_expected_density_at_40km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(40e3)

        self.assertAlmostEqual(0.003995177308809338, conditions['density'])

    def test_calculate_atmosphere_returns_expected_temp_at_50km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(50e3)

        self.assertAlmostEqual(270.65, conditions['temperature'])

    def test_calculate_atmosphere_returns_expected_pressure_at_50km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(50e3)

        self.assertAlmostEqual(79.76573128665314, conditions['pressure'])

    def test_calculate_atmosphere_returns_expected_density_at_50km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(50e3)

        self.assertAlmostEqual(0.0010267067714370681, conditions['density'])

    def test_calculate_atmosphere_returns_expected_temp_at_60km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(60e3)

        self.assertAlmostEqual(247.01570363466914, conditions['temperature'])

    def test_calculate_atmosphere_returns_expected_pressure_at_60km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(60e3)

        self.assertAlmostEqual(21.952917541867947, conditions['pressure'])

    def test_calculate_atmosphere_returns_expected_density_at_60km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(60e3)

        self.assertAlmostEqual(0.00030960344824027507, conditions['density'])

    def test_calculate_atmosphere_returns_expected_temp_at_75km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(75e3)

        self.assertAlmostEqual(208.39337517433754, conditions['temperature'])

    def test_calculate_atmosphere_returns_expected_pressure_at_75km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(75e3)

        self.assertAlmostEqual(2.38699851722098, conditions['pressure'])

    def test_calculate_atmosphere_returns_expected_density_at_75km(self):
        atmosphere = self.create_atmosphere()

        conditions = atmosphere.calculate_atmosphere(75e3)

        self.assertAlmostEqual(3.990307341708261e-05, conditions['density'])

    def test_calculate_atmosphere_raises_exception_when_queried_above_80km(self):
        atmosphere = self.create_atmosphere()

        with self.assertRaises(ValueError) as exception_context:
            conditions = atmosphere.calculate_atmosphere(100e3)
        self.assertEqual('geometric_height_meters, 100000.0, outside defined limits of 0 to 80000',
                         str(exception_context.exception))

    def test_calculate_atmosphere_raises_exception_when_queried_below_0km(self):
        atmosphere = self.create_atmosphere()

        with self.assertRaises(ValueError) as exception_context:
            conditions = atmosphere.calculate_atmosphere(-100e3)
        self.assertEqual('geometric_height_meters, -100000.0, outside defined limits of 0 to 80000',
                         str(exception_context.exception))

    def test_calculate_atmosphere_correctly_adds_non_standard_day_temperature(self):
        atmosphere = self.create_atmosphere()
        atmosphere.set_sea_level_temperature(300)

        conditions = atmosphere.calculate_atmosphere(0)

        self.assertAlmostEqual(300, conditions['temperature'])

    def test_calculate_atmosphere_does_not_modify_pressure_with_non_standard_day_temperature(self):
        atmosphere = self.create_atmosphere()
        atmosphere.set_sea_level_temperature(300)

        conditions = atmosphere.calculate_atmosphere(0)

        self.assertAlmostEqual(101325, conditions['pressure'])

    def test_calculate_atmosphere_correctly_modifies_density_with_non_standard_day_temperature(self):
        atmosphere = self.create_atmosphere()
        atmosphere.set_sea_level_temperature(300)

        conditions = atmosphere.calculate_atmosphere(0)

        self.assertAlmostEqual(1.1766125174083786, conditions['density'])

