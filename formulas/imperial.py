def ead(o2, depth):
    """Equivalent air depth.
    :param o2: Fraction of oxygen.
    :param depth: Depth.
    :return: Equivalent air depth in feet."""
    return ((1 - o2) * (depth + 33) / .79) - 33


def max_depth_bottom(o2):
    """Maximum depth for bottom gas.
    :param o2: Fraction of oxygen.
    :return: Maximum depth for bottom gas in feet."""
    return (46.2 / o2) - 33


def max_depth_deco(o2):
    """Maximum depth for decompression gas.
    :param o2: Fraction of oxygen.
    :return: Maximum depth for decompression gas in feet."""
    return (52.8 / o2) - 33


def sac_rate(psi, w_pressure, cylinder, depth, time):
    """Surface air consumption rate.
    :param psi: PSI.
    :param w_pressure: Working pressure.
    :param cylinder: Cylinder.
    :param depth: Depth.
    :param time: Time.
    :return: Surface air consumption rate in Cu Ft/Min."""
    return ((psi / w_pressure) * cylinder) / ((depth + 33) / 33) / time


def gas_requirement_estimate(time, sac, depth):
    """Gas requirement estimate.
    :param time: Time.
    :param sac: Surface air consumption rate.
    :param depth: Depth.
    :return: Gas requirement estimate in Cu Ft."""
    return (time * sac) * ((depth + 33) / 33)


def actual_gas_supply(volume, psi, w_pressure):
    """Actual gas supply.
    :param volume: Volume of gas.
    :param psi: PSI.
    :param w_pressure: Working pressure.
    :return: Actual gas supply in Cu Ft."""
    return psi / w_pressure * volume


def turn_pressure(start, bottom, cylinder):
    """Turn pressure.
    :param start: Starting pressure.
    :param bottom: Bottom pressure.
    :param cylinder: Cylinder.
    :return: Turn pressure in psi."""
    return start - (bottom / cylinder)
