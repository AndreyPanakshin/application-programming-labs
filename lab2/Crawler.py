import os

from icrawler.builtin import GoogleImageCrawler

def download_images(keyw: str, imagedirectory: str, quantity: int)->None:
    """
    Searches for images by the entered words in Google Image Crawler and uploads them to the directory, which is cleared when the program is started again
    :param keyw: image search word
    :param imagedirectory:the path to the downloaded images
    :param quantity:number of images to download
    :return:
    """
    if not os.path.isdir(imagedirectory):
        os.mkdir(imagedirectory)
    for filename in os.listdir(imagedirectory):
        os.remove(os.path.join(imagedirectory,filename))

    google_crawler = GoogleImageCrawler(downloader_threads=4, storage={'root_dir': imagedirectory})
    google_crawler.crawl(keyword=keyw, max_num=quantity)
