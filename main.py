from Crawler import download_images
from Parser import create_parser
from Annotation import dataframe
from Annotation import filter_images
from Annotation import sort_area
from Annotation import plot_histogram
import pandas as pd

def main():
    keyw, imageditectory, get_csv, quantity=create_parser()

    try:
        download_images(keyw,imageditectory,quantity)
        df = pd.read_csv(get_csv)
        dataframe(imageditectory,get_csv)
        print(f"dataframe\n{df}")
        max_width = 1000
        max_height = 1000
        df = filter_images(df, max_width, max_height)
        print(f"filter by size dataframe\n{df}")
        df = sort_area(df)
        print(f"sort by area dataframe:\n{df}")
        plot_histogram(df)

    except Exception as e:
        print(f"mistake:{e}")


if __name__=="__main__":
    main()


