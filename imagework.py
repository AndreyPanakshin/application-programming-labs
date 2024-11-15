import cv2
import matplotlib.pyplot as plt
import numpy as np

def get_img(imgdir:str)->np.ndarray:
    '''
    getting an image from the specified directory
    :param imgdir:image directory
    :return:an image in the form of a multidimensional array
    '''
    img=cv2.imread(imgdir)
    if img is None:
        raise ValueError
    return img

def size_img(img:np.ndarray)->tuple[int,int,int]:
    '''
    getting image parameters
    :param img:an image in the form of a multidimensional array
    :return:image dimensions in the form of a tuple
    '''
    height,width,channels=img.shape
    return height,width,channels

def plot_histogram(img:np.ndarray)->dict:
    """
    creating an image histogram
    :param img:an image in the form of a multidimensional array
    :return:A histogram dictionary for each color channel of the image.
    """
    histogram={}
    try:
        color=('b','g','r')
        for i,col in enumerate(color):
            hist=cv2.calcHist([img],[i],None,[256],[0,256])
            histogram[col]=hist.flatten()
    except Exception as e:
        raise RuntimeError(f'mistake:{e}')
    return histogram

def display_histogram(histogram:dict)->None:
    """
    display image histogram
    :param histogram: A histogram dictionary for each color channel of the image.
    """
    try:
        plt.figure()
        for col in histogram.keys():
            plt.plot(histogram[col], color=col)
        plt.xlim([0, 256])
        plt.title("image histogram")
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Number of pixels')
        plt.show()
    except Exception as e:
        raise RuntimeError(f'mistake:{e}')

def invert_colors(img:np.ndarray)->np.ndarray:
    '''
    creating an image with color inversion
    :param img:an image in the form of a multidimensional array
    :return:image with color inversion in the form of a multidimensional array
    '''
    return cv2.bitwise_not(img)

def save_image(savedir:str,img:np.ndarray)->None:
    '''
    saving the modified image
    :param savedir:
    :param img:an image in the form of a multidimensional array
    '''
    try:

        cv2.imwrite(savedir,img)

    except Exception:
        raise IOError(f'the image has not been uploaded in {savedir}')

def display_images(original_image:np.ndarray,inverted_image:np.ndarray)->None:
    '''
    output of the original and modified images
    :param original_image:original image
    :param inverted_image:modified image
    '''

    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.imshow(cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB))
    plt.title('Original image')
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(cv2.cvtColor(inverted_image,cv2.COLOR_BGR2RGB))
    plt.title('Inverted image')
    plt.axis('off')

    plt.show()

