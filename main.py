from parser import create_parser

from imagework import get_img
from imagework import size_img
from imagework import plot_histogram
from imagework import display_histogram
from imagework import invert_colors
from imagework import save_image
from imagework import display_images

def main():
    imgdir,savedir= create_parser()

    try:
        img=get_img(imgdir)
        print(f"size of image: {size_img(img)}")
        histogram=plot_histogram(img)
        display_histogram(histogram)
        inverted_image=invert_colors(img)
        save_image(savedir,inverted_image)
        display_images(img,inverted_image)

    except Exception as e:
        print(f'mistake:{e}')

if __name__ == "__main__":
    main()
