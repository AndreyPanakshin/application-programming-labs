import argparse

def create_parser()->tuple[str, str, str, int]:
    """
    Getting command line arguments
    :return:command line arguments
    """
    parser=argparse.ArgumentParser()
    parser.add_argument('keyw',type=str)
    parser.add_argument('imagedirectory', type=str)
    parser.add_argument('get_csv', type=str)
    parser.add_argument('quantity', type=int)
    args=parser.parse_args()
    return args.keyw, args.imagedirectory, args.get_csv,args.quantity
