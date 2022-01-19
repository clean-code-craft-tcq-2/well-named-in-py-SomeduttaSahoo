from color_coder_test import execute_unittests
from reference_manual_generator import print_reference_manual, create_reference_manual

if __name__ == '__main__':
    execute_unittests()
    print("\n Reference Manual for Telecomm Insulation Wire color codes \n", )
    reference_manual = create_reference_manual()
    print_reference_manual(reference_manual)
    print('Done :)')
