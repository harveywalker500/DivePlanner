def ead(o2, depth):
    """Equivalent air depth.
    :param o2: Fraction of oxygen.
    :param depth: Depth.
    :return: Equivalent air depth in metres."""
    return ((1 - o2) * (depth + 10) / .79) - 10


def max_depth_bottom(o2):
    """Maximum depth for bottom gas.
    :param o2: Fraction of oxygen.
    :return: Maximum depth for bottom gas in metres."""
    return (14 / o2) - 10


def max_depth_deco(o2):
    """Maximum depth for decompression gas.
    :param o2: Fraction of oxygen.
    :return: Maximum depth for decompression gas in metres."""
    return (16 / o2) - 10


def sac_rate(bar, cylinder, depth, time):
    """Surface air consumption rate.
    :param bar: Bar.
    :param cylinder: Cylinder.
    :param depth: Depth.
    :param time: Time.
    :return: Surface air consumption rate in L/Min."""
    return (bar * cylinder) / ((depth + 10) / 10) / time


def gas_requirement_estimate(time, sac, depth):
    """Gas requirement estimate.
    :param time: Time.
    :param sac: Surface air consumption rate.
    :param depth: Depth.
    :return: Gas requirement estimate in L."""
    return (time * sac) * ((depth + 10) / 10)


def actual_gas_supply(volume, bar):
    """Actual gas supply.
    :param volume: Volume of gas.
    :param bar: Bar.
    :return: Actual gas supply in L."""
    return volume * bar


def ascent_time(bottom, stop, rate):
    """Ascent time.
    :param bottom: Bottom depth.
    :param stop: Stop depth.
    :param rate: Rate of ascent.
    :return: Ascent time."""
    return (bottom - stop) / rate


def turn_pressure(start, bottom, cylinder):
    """Turn pressure.
    :param start: Starting pressure.
    :param bottom: Bottom depth.
    :param cylinder: Cylinder.
    :return: Turn pressure in bar."""
    return start - (bottom / cylinder)
