import argparse

def create_parser()->tuple[str, str,int,int]:
    """
    Getting command line arguments
    :return:command line arguments
    """
    parser=argparse.ArgumentParser()
    parser.add_argument('imagedirectory', type=str)
    parser.add_argument('get_csv', type=str)
    parser.add_argument('max_width', type=int)
    parser.add_argument('max_height', type=int)
    args=parser.parse_args()
    return  args.imagedirectory, args.get_csv, args.max_width, args.max_height
