import pandas as pd
import numpy as np
import wfdb
from wfdb import processing

#computes average heart rate
def compute_heart_rate(record):
    qrs_locations = wfdb.processing.gqrs_detect(record.p_signal[:, 0], fs=record.fs)
    heart_rates = wfdb.processing.compute_hr(sig_len=record.sig_len, qrs_inds=qrs_locations, fs=record.fs)
    avg_heart_rate = 0
    no_of_relevant_heart_rates = 0

    for i in heart_rates:

        if not np.isnan(i):
            avg_heart_rate += i
            no_of_relevant_heart_rates += 1

    return avg_heart_rate / no_of_relevant_heart_rates


def retrieve_age(meta_data):
    age = meta_data['comments'][0].split(':')
    return age[1]


def retrieve_date(meta_data):
    date = meta_data['comments'][2].split(':')
    return date[1]


def retrieve_sex(meta_data):
    sex = meta_data['comments'][1].split(':')
    return sex[1]
