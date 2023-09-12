from formulas import metric
from formulas import imperial
from formulas import common

def calculate_table_for_o2_fraction_metric(o2_fraction):
    # Convert the fraction to percentage
    percent_o2 = int(o2_fraction * 100)

    # Initialize lists to hold data
    depths = [3] + [5] + list(range(6, 60, 3))  # Starting with 3 and 5, and multiples of 3
    eads = []
    po2s = []
    otu_mins = []

    # Calculate values for each depth
    for depth in depths:
        current_ead = round(metric.ead(o2_fraction, depth), 2)
        eads.append(current_ead)

        # Absolute pressure is depth/10 + 1 (10m of water column is roughly equivalent to 1 atm)
        current_po2 = round(common.po2(o2_fraction, depth / 10 + 1), 2)
        if current_po2 > 1.6:
            break
        po2s.append(current_po2)

        otu_mins.append(round(common.otu_min(current_po2), 2))

    # Adjust the depths list to match the length of the po2s list
    depths = depths[:len(po2s)]

    # Return the results as a dictionary
    return {
        'O2 Percentage': percent_o2,
        'Depth': depths,
        'EAD': eads,
        'PO2': po2s,
        'OTU/min': otu_mins
    }

def calculate_table_for_o2_fraction_imperial(o2_fraction):
    # Convert the fraction to percentage
    percent_o2 = int(o2_fraction * 100)

    # Initialize lists to hold data
    depths = [10] + [15] + list(range(20, 220, 10))  # Starting with 10 and 15, and multiples of 10
    eads = []
    po2s = []
    otu_mins = []

    # Calculate values for each depth
    for depth in depths:
        current_ead = round(imperial.ead(o2_fraction, depth), 2)
        eads.append(current_ead)

        # Absolute pressure is depth/33 + 1 (33 feet of water column is roughly equivalent to 1 atm)
        current_po2 = round(common.po2(o2_fraction, depth / 33 + 1), 2)
        if current_po2 > 1.6:
            break
        po2s.append(current_po2)

        otu_mins.append(round(common.otu_min(current_po2), 2))

    # Adjust the depths list to match the length of the po2s list
    depths = depths[:len(po2s)]

    # Return the results as a dictionary
    return {
        'O2 Percentage': percent_o2,
        'Depth': depths,
        'EAD': eads,
        'PO2': po2s,
        'OTU/min': otu_mins
    }
