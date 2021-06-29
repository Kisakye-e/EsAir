from datetime import datetime, timedelta
import pandas as pd
import requests
import urllib3
from dataclasses import dataclass
from config import configuration
import numpy as np

from exceedances.exceedance import get_WHO_exceedances

# disable tls/ssl warnings
urllib3.disable_warnings()


@dataclass
class Exceedances:
    standard: str
    pollutant: str
    n_values: int
    day: datetime
    values: np.ndarray
    first_value: np.dtype(int)
    last_value:  np.dtype(int)


class CalculateExceedances:

    def __init__(self, tenant, standard, day):
        self.tenant = tenant
        self.WHO_LIMIT = {"pm2_5": 25, "pm10": 50, "no2": 40}
        self.PM_25_AQI_LIMIT = {
            'Good': [0, 12],
            'Moderate': [12, 35.4],
            'UHFSG': [35.4, 55.4],
            'Unhealthy': [55.4, 150.4],
            'VeryUnhealthy': [150.4, 250.4],
            'Hazardous': [250.4, 500.4],
            'All': [0, 2000],
        }
        self.PM_10_AQI_LIMIT = {
            'Good': [0, 54],
            'Moderate': [54, 154],
            'UHFSG': [154, 254],
            'Unhealthy': [254, 354],
            'VeryUnhealthy': [354, 424],
            'Hazardous': [424, 604],
            'All': [0, 2000],
        }
        self.NO2_AQI_LIMIT = {
            'Good': [0, 53],
            'Moderate': [53, 100],
            'UHFSG': [100, 360],
            'Unhealthy': [360, 649],
            'VeryUnhealthy': [649, 1249],
            'Hazardous': [1249, 2049],
            'All': [0, 2049],
        }

    def calculate_exceedance():
        get_measurements()
        aqi = get_AQ1()
        who = get_WHO()

        return {
            site_id: "",
            time: "",
            who: {
                pm2_5: "",
                pm10: "",
                no2: ""
            },
            aqi: {
                pm2_5: "",
                pm10: "",
                no2: ""
            },
        }

    def save_exceedance():
        exceedance_document = {
            day: "",
            exceedances: [
                {
                    site_id: "",
                    time: "",
                    who: {
                        pm2_5: "",
                        pm10: "",
                        no2: ""
                    },
                    aqi: {
                        pm2_5: "",
                        pm10: "",
                        no2: ""
                    },
                }
            ]
        }

    def get_AQ1():
        get_measuremnts()

    def get_WHO():
        pass

    def get_measurements():
        pass
