import csv
import os

def annotation(imagedirectory:str, get_csv:str)->None:
    """
     Records the absolute and relative paths of downloaded images in the annotation file
    :param imagedirectory: the path to the downloaded images
    :param get_csv: annotation file in csv format
    :return: None
    """
    image_filenames = retrieve_filename(imagedirectory)
    with open(get_csv, mode='w', newline='', encoding='utf-8') as file_csv:
        fieldnames= ['absolute_path', 'relative_path']
        writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
        writer.writeheader()

        for filename in image_filenames:
            absolute_path = os.path.abspath(filename)
            relative_path = os.path.relpath(filename, start=imagedirectory)
            writer.writerow({'absolute_path': absolute_path, 'relative_path': relative_path})

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