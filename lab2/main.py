from Crawler import download_images
from IteratorImage import Iterator
from Parser import create_parser
from Annotation import annotation

def main():
    keyw, imageditectory, get_csv, quantity=create_parser()

    try:
        download_images(keyw,imageditectory,quantity)
        annotation(imageditectory,get_csv)
        iterator=Iterator(get_csv)
        for vyvod in iterator:
            print(vyvod)
    except Exception as e:
        print(f"mistake:{e}")


if __name__=="__main__":
    main()


