import sys
sys.path.append("./")

import numpy as np

from .calibrate_sensors import Calibration

def baseline_sensor_data(values):
    return values - np.nanmedian(values)

# -------------------------------- Corrections ------------------------------- #

def calibrate_sensors_data(sensors_data, sensors, calibration_data=None,
                                weight_percent=False, mouse_weight=None):
    """
        Calibrates the sensors to convert voltages to grams

        :param sensors_data: dictionary with voltages at each frame for each channel
        :param sensors: list of strings with the name of allowed sensors
        :param calibration_data: data from csv file with calibration data
        :param weight_percent: if true the weights are expressed in percentage of the mouse weight
        :param mouse_weight: float, weight of the mouse whose data are being processed
    """

    calibration = Calibration(calibration_data=calibration_data)
    calibrated =  {ch:calibration.correct_raw(volts, ch) 
                                for ch, volts in sensors_data.items() if ch in sensors}

    if weight_percent:
        calibrated = {ch:(values/mouse_weight)*100 for ch, values in calibrated.items()}
    
    return calibrated

def correct_paw_used(sensors_data, paw_used):
    if 'l' in paw_used.lower():
        return {
            'fr': sensors_data['fl'],
            'fl': sensors_data['fr'],
            'hr': sensors_data['hl'],
            'hl': sensors_data['hr']
        }
    return sensors_data


# ------------------------------- Computations ------------------------------- #
def compute_center_of_gravity(sensors_data):
    y = (sensors_data["fr"]+sensors_data["fl"]) - \
            (sensors_data["hr"]+sensors_data["hl"])
    x = (sensors_data["fr"]+sensors_data["hr"]) - \
            (sensors_data["fl"]+sensors_data["hl"])

    centered_x, centered_y = x-x[0], y-y[0]
    return np.vstack([x,y]).T, np.vstack([centered_x,centered_y]).T

