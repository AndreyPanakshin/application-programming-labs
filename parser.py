import argparse

def create_parser()->tuple[str, str]:
    """
    Getting command line arguments
    :return:command line arguments
    """
    parser=argparse.ArgumentParser()
    parser.add_argument('imgdir',type=str)
    parser.add_argument('savedir', type=str)
    args=parser.parse_args()
    return args.imgdir, args.savedir
