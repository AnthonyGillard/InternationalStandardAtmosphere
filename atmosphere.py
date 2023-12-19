from math import exp


def check_input_int_or_float(variable_name, variable):
    if type(variable) is not int and type(variable) is not float:
        raise TypeError(f'Expected {variable_name} to be int or float type instead {type(variable)}'
                        f' was provided')


def check_input_within_limits(variable_name, variable, lower_limit, upper_limit):
    if lower_limit <= variable <= upper_limit:
        return
    else:
        raise ValueError(f'{variable_name}, {variable}, outside defined limits of {lower_limit} to {upper_limit}')


class Atmosphere:
    _layer_start_altitudes = (0, 11000, 20000, 32000, 47000, 51000, 71000, 80000)
    _layer_start_temperature = (288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65, 196.65)
    _layer_start_pressure = (1.01325e5, 2.263204e4, 5.474879e3, 8.68016e2, 1.109058e02, 6.693853e1, 3.956392,
                             8.8627722e-1)
    _layer_temp_lapse_rate = (-6.5e-3, 0, 1.0e-3, 2.8e-3, 0, -2.8e-3, -2e-3)

    _earth_radius = 6378e3
    _g = 9.80665
    _R = 287.05287
    _sea_level_temperature = _layer_start_temperature[0]

    def __init__(self, sea_level_temperature=288.15):
        self.set_sea_level_temperature(sea_level_temperature)

    def set_sea_level_temperature(self, temperature_kelvin):
        """
        Set sea level temperature [K] for a non-standard day query.

        :param temperature_kelvin: Sea level temperature [k].
        """
        check_input_int_or_float('sea_level_temperature', temperature_kelvin)
        self._sea_level_temperature = temperature_kelvin

    def calculate_atmosphere(self, geometric_height):
        """
        Calculates atmospheric conditions at a given altitude [m].

        :param geometric_height: Altitude at which to query atmosphere.
        :return: Dictionary containing atmospheric conditions
        """
        check_input_int_or_float('geometric_height_meters', geometric_height)
        check_input_within_limits('geometric_height_meters', geometric_height,
                                  self._layer_start_altitudes[0], self._layer_start_altitudes[-1])

        atmosphere = dict()

        geopotential_height = self._convert_height_from_geometric_to_geopotential(geometric_height)
        layer_index = self._determine_atmospheric_layer(geopotential_height)
        temperature = self._calculate_temperature(geopotential_height, layer_index)

        atmosphere['pressure'] = self._calculate_pressure(temperature, geopotential_height, layer_index)
        atmosphere['temperature'] = self._adjust_temperature_to_account_for_non_standard_conditions(temperature)
        atmosphere['density'] = self._calculate_density_via_ideal_gas_eq(atmosphere['temperature'],
                                                                         atmosphere['pressure'])
        return atmosphere

    def _convert_height_from_geometric_to_geopotential(self, geometric_height_meters):
        return geometric_height_meters * (self._earth_radius / (self._earth_radius + geometric_height_meters))

    def _determine_atmospheric_layer(self, geopotential_height):
        for index, _ in enumerate(self._layer_start_altitudes):
            if self._layer_start_altitudes[index] <= geopotential_height < self._layer_start_altitudes[index+1]:
                return index

    def _calculate_temperature(self, geopotential_height, layer_index):
        return self._layer_start_temperature[layer_index] + self._layer_temp_lapse_rate[layer_index] * \
            (geopotential_height - self._layer_start_altitudes[layer_index])

    def _calculate_pressure(self, temperature, geopotential_height, layer_index):
        if self._layer_temp_lapse_rate[layer_index] == 0:
            return self._layer_start_pressure[layer_index] * \
                exp((-self._g * (geopotential_height - self._layer_start_altitudes[layer_index])) /
                    (self._R * self._layer_start_temperature[layer_index]))
        else:
            return self._layer_start_pressure[layer_index] * \
                ((temperature / self._layer_start_temperature[layer_index]) **
                 (-self._g / (self._R * self._layer_temp_lapse_rate[layer_index])))

    def _adjust_temperature_to_account_for_non_standard_conditions(self, atmospheric_temperature):
        atmospheric_temperature += (self._sea_level_temperature - self._layer_start_temperature[0])
        return atmospheric_temperature

    def _calculate_density_via_ideal_gas_eq(self, temperature, pressure):
        return pressure / (self._R * temperature)
