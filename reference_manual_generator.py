import colorpair_generator as color
from cable_colors import get_colorpair_names

def create_reference_manual():
    reference_manual = []
    pair_number_start_index = 1
    pair_number_end_index = len(color.MAJOR_COLORS) * len(color.MINOR_COLORS) + 1
    for pair_number in range(pair_number_start_index, pair_number_end_index):
        major_color, minor_color = color.get_color_from_pairnumber(pair_number)
        formatted_colorpair = get_colorpair_names(major_color, minor_color)
        reference_manual.append("{:<15} {:<10} ".format(pair_number, formatted_colorpair))
    return reference_manual


def print_reference_manual(reference_manual):
    print("{:<15} {:<15}".format('Pair Number', 'Major Minor ColorPairs'))
    for manual_entries in reference_manual:
        print(manual_entries)
