import os
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

def retrieve_filename(imagedirectory:str)->list:
    """
    collecting file names of downloaded images
    :param imagedirectory:the path to the downloaded images
    :return:list of file names
    """
    image_extensions=('.jpeg','.png','.jpg')
    image_filenames=[]
    for filename in os.listdir(imagedirectory):
        if filename.lower().endswith(image_extensions):
            image_filenames.append(filename)
    return image_filenames

def dataframe(imagedirectory:str, get_csv:str)->None:
    """
     Records the absolute and relative paths of downloaded images in the annotation file
    :param imagedirectory: the path to the downloaded images
    :param get_csv: annotation file in csv format
    :return: None
    """
    image_filenames = retrieve_filename(imagedirectory)
    image_data=[]

    for filename in image_filenames:
        absolute_path=os.path.abspath(os.path.join(imagedirectory,filename))
        relative_path=os.path.join(imagedirectory,filename)

        with Image.open(os.path.join(imagedirectory,filename)) as img:
            width,height=img.size
            area=width*height
            channels = len(img.getbands())

        image_data.append({
            'absolute_path':absolute_path,
            'relative_path': relative_path,
            'height':height,
            'width':width,
            'channels':channels,
            'area':area
        })
    df=pd.DataFrame(image_data)
    df.to_csv(get_csv,index=False)

def filter_images(df:pd.DataFrame,max_width:int,max_height:int)->pd.DataFrame:
    """
    the new DataFrame includes those photos
     whose sizes are smaller than the specified ones
    :param df: DataFrame with image annotation
    :param max_width: maximum width value
    :param max_height:maximum height value
    :return:DataFrame with image annotation with suitable sizes
    """
    return df[(df['width']<=max_width) & (df['height']<=max_height)]

def sort_area(df:pd.DataFrame)->pd.DataFrame:
    """
    sort by image area DataFrame
    :param df:DataFrame with image annotation
    :return:sorted by image area DataFrame with image annotation
    """
    df=df.sort_values(by='area')
    return df

def plot_histogram(df:pd.DataFrame)->None:
    """
    Creating a histogram of the distribution of image areas
    :param df: DataFrame
    """
    plt.hist(df['area'],bins=20,edgecolor='black')
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    plt.title('Histogram if Image Areas')
    plt.show()





