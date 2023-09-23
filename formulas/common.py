
import numpy as np

def po2(fo2, p):
    """Partial pressure of oxygen.
    :param fo2: Fraction of oxygen.
    :param p: Pressure.
    :return: Partial pressure of oxygen."""
    return fo2 * p


def fo2(po2, p):
    """Fraction of oxygen.
    :param po2: Partial pressure of oxygen.
    :param p: Pressure.
    :return: Fraction of oxygen."""
    return po2 / p


def p(fo2, po2):
    """Absolute pressure.
    :param fo2: Fraction of oxygen.
    :param po2: Partial pressure of oxygen.
    :return: Absolute pressure."""
    return po2 / fo2


def gas_reserve(volume, reserve):
    """Gas reserve.
    :param volume: Volume of gas.
    :param reserve: Gas reserve.
    :return: Gas reserve in L/Cu Ft."""
    return volume / (1 - (reserve / 100))


def ascent_depth(bottom, stop):
    """Ascent depth.
    :param bottom: Bottom depth.
    :param stop: Stop depth.
    :return: Ascent depth."""
    return ((bottom - stop) / 2) + stop


def ascent_time(bottom, stop, rate):
    """Ascent time.
    :param bottom: Bottom depth.
    :param stop: Stop depth.
    :param rate: Rate of ascent.
    :return: Ascent time."""
    return (bottom - stop) / rate


def otu_min(po2):
    """OTU per minute.
    :param po2: Partial pressure of oxygen.
    :return: OTU per minute."""
    if po2 <= 0.5:  # Avoiding mathematical issues if PO2 <= 0.5
        return 0
    return (0.5 / (po2 - 0.5)) ** (-5.0 / 6.0)


def total_otu(otu_min, time):
    """Total OTU.
    :param otu_min: OTU per minute.
    :param time: Time.
    :return: Total OTU."""
    return otu_min * time

def cns_min(po2):
    # Data from the NOAA max oxygen exposure table
    ppo2 = [0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65]
    minutes = [720, 570, 450, 360, 300, 240, 210, 195, 180, 165, 150, 135, 120, 83, 45, 7]

    if po2 <= 0.5:
        return 0.0

    interpolated_min = np.interp(po2, ppo2, minutes)

    return (1 / interpolated_min) * 100


def total_cns(cns_min, time):
    """Total CNS%.
    :param cns_min: CNS per minute.
    :param time: Time.
    :return: Total CNS%."""
    return cns_min * time
