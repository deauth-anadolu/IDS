import numpy as np
from scipy.optimize import root



class GeoLocater:
    xs = [10, 100, 300]
    ys = [10, 200, 300]
    

    def calculate_geo_location(self, rs: list):
        location = self.__trilateration(GeoLocater.xs, GeoLocater.ys, rs)
        return location

    def calculate_distances(self, dbms):
        rs = []
        for dbm in dbms:
            r = GeoLocater.__calculate_distance_by_dbm(int(dbm))
            rs.append(r)
        return rs

    @classmethod
    def __calculate_distance_by_dbm(cls, rssi: int, n=2, A=-30):
        """
        Calculate the distance from the RSSI value using the path-loss model.

        Parameters:
        rssi (dbm) (int): The received signal strength indicator (RSSI) in dBm.

        Returns:
        float: The estimated distance in meters.

        This function uses the following formula to convert RSSI to distance:
        d = 10^((A - RSSI) / (10 * n))
        where:
        - d is the distance in meters.
        - A is the RSSI value at a reference distance (typically 1 meter).
        - n is the path-loss exponent, which varies depending on the environment.
        """
        return 10 ** ((A - rssi) / (10 * n))
    
    @classmethod
    def set_antennas_pos(cls, xs, ys):
        cls.xs = xs
        cls.ys = ys

    @classmethod
    def __trilateration(cls, xs, ys, rs):
        return cls.__solve_equations(xs, ys, rs)
    
    @classmethod
    def __solve_equations(cls, xs, ys, rs):
        initial_guess = (0, 0)
        solution = root(cls.__equations, initial_guess, args=(xs, ys, rs), method='lm')
        return solution.x


    @classmethod
    def __equations(cls, vars, xs, ys, rs):
        x, y = vars
        eqs = np.empty(len(xs))  # Create empty NumPy array with space for 3 elements
        for i in range(3):
            eq = (x - xs[i])**2 + (y - ys[i])**2 - rs[i]**2
            eqs[i] = eq  # Assign each equation value to the corresponding index in the array
        return eqs


