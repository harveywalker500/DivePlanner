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
    return volume / (1 - reserve)


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
