from Parser import create_parser
from Annotation import annotation
from Annotation import dataframe
from Annotation import add_image_dimensions
from Annotation import filter_images
from Annotation import sort_area
from Annotation import statistic
from Annotation import plot_histogram
import pandas as pd

def main():
    imageditectory, get_csv, max_width,max_height=create_parser()

    try:
        annotation(imageditectory, get_csv)
        df = pd.read_csv(get_csv)
        dataframe(get_csv)
        add_image_dimensions(df)
        print(f"dataframe\n{df}")
        statistic(df)
        print("----")
        df = filter_images(df, max_width, max_height)
        print(f"filter by size dataframe\n{df}")
        df = sort_area(df)
        print(f"sort by area dataframe:\n{df}")
        plot_histogram(df)
    except Exception as e:
        print(f"mistake:{e}")


if __name__=="__main__":
    main()
