#feature engineering - wavelet transformation 

import numpy as np
import pywt #py wavelet transform image
import cv2

#input image and do wavelet transformation on top of it -> return new image of wavelet transform
#differentiates eyes from nose and forehead -> almost looks like a black white image -> easy for computer to detect facial features


#signal processing, fourier transform, rep image as a frequency
#image can be a signal -> presented in spacial (x,y) domain or frequency domain
#fourier transform -> take complex signal and return basic signals that make that complex signal (think noise cancellation)

def w2d(img, mode='haar', level=1):
    imArray = img
    #datatype conversion, convert to grayscale
    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
    #convert to float
    imArray = np.float32(imArray)
    imArray /= 255

    #compute coefficients
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #process coefficients 
    coeffs_H=list(coeffs)
    coeffs_H[0] *= 0

    #reconstruction
    imArray_H = pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)

    
    return imArray_H