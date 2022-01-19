import colorpair_generator as color
from reference_manual_generator import create_reference_manual


def test_given_pairnumber_yeild_expected_colorpair(pair_number,
                                                   expected_major_color, expected_minor_color):
    major_color, minor_color = color.get_color_from_pairnumber(pair_number)
    assert (major_color == expected_major_color)
    assert (minor_color == expected_minor_color)


def test_given_colorpair_yeild_expected_pairnumber(major_color, minor_color, expected_pair_number):
    pair_number = color.get_pairnumber_from_color(major_color, minor_color)
    assert (pair_number == expected_pair_number)


def test_create_reference_manual_length(expected_entries_number):
    reference_manual = create_reference_manual()
    assert (len(reference_manual) == expected_entries_number)


def execute_unittests():
    test_given_pairnumber_yeild_expected_colorpair(4, 'White', 'Brown')
    test_given_pairnumber_yeild_expected_colorpair(5, 'White', 'Slate')
    test_given_colorpair_yeild_expected_pairnumber('Black', 'Orange', 12)
    test_given_colorpair_yeild_expected_pairnumber('Violet', 'Slate', 25)
    test_given_colorpair_yeild_expected_pairnumber('Red', 'Orange', 7)
    test_create_reference_manual_length(25)
