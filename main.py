import GetColor_PairNumber
import GetPair_fromNumber


def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'




if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
