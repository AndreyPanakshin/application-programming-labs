import os
import pandas as pd
import matplotlib.pyplot as plt
import csv
import cv2

def retrieve_filename(imagedirectory: str) -> list:
    """Collecting file names of downloaded images.
    :param imagedirectory: directory of images
    :return: list with image filenames
    """
    image_extensions = ('.jpeg', '.png', '.jpg')
    image_filenames = []
    for filename in os.listdir(imagedirectory):
        if filename.lower().endswith(image_extensions):
            image_filenames.append(filename)
    return image_filenames

def annotation(imagedirectory: str, get_csv: str) -> None:
    """Records the absolute and relative paths of downloaded images in the annotation file.
    :param imagedirectory: directory of images
    :param get_csv:path to file csv
    """
    image_filenames = retrieve_filename(imagedirectory)
    with open(get_csv, mode='w', newline='', encoding='utf-8') as file_csv:
        fieldnames = ['absolute_path', 'relative_path']
        writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
        writer.writeheader()
        for filename in image_filenames:
            absolute_path = os.path.abspath(os.path.join(imagedirectory, filename))
            relative_path = os.path.join(imagedirectory, filename)
            writer.writerow({'absolute_path': absolute_path, 'relative_path': relative_path})

def dataframe(get_csv: str) -> None:
    """Load data from csv file into DataFrame.
    :param get_csv
    csv: path to file csv
    """
    if not os.path.exists(get_csv):
        raise FileNotFoundError(f"Annotation file not found: {get_csv}")
    df = pd.read_csv(get_csv)
    df.columns = ['absolute_path', 'relative_path']
    return df

def add_image_dimensions(df: pd.DataFrame) -> None:
    """Add columns for height, width, depth, and area.
    :param df:data frame
    """
    heights, widths, depths, areas = [], [], [], []
    for rel_path in df["relative_path"]:
        if not os.path.exists(rel_path):
            raise FileNotFoundError(f"Image file not found: {rel_path}")
        image = cv2.imread(rel_path)
        if image is None:
            raise ValueError(f"Could not open image: {rel_path}")
        height, width, depth = image.shape
        area = height * width
        heights.append(height)
        widths.append(width)
        depths.append(depth)
        areas.append(area)

    df["Height"] = heights
    df["Width"] = widths
    df["Depth"] = depths
    df["Area"] = areas

def filter_images(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """Return DataFrame with images smaller than specified sizes.
    :param df: data frame
    :param max_width:max width
    :param max_height:max height
    :return:filter data frame
    """
    return df[(df['Width'] <= max_width) & (df['Height'] <= max_height)]

def sort_area(df: pd.DataFrame) -> pd.DataFrame:
    """Sort DataFrame by image area.
    :param df:data frame
    :return:sort data frame
    """
    df = df.sort_values(by='Area')
    return df

def statistic(df: pd.DataFrame) -> None:
    """
    Создание статистики
    :param df: DataFrame to statistic
    :return: Statistical information of columns: height, width, depth
    """
    stats = df[['Height', 'Width', 'Depth']].describe()
    print (stats)

def plot_histogram(df: pd.DataFrame) -> None:
    """Create a histogram of the distribution of image areas.
    :param:data frame
    """
    plt.hist(df['Area'], bins=20, edgecolor='black')  # Используем 'Area' с большой буквы
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    plt.title('Histogram of Image Areas')
    plt.show()
