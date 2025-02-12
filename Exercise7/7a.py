#!/usr/bin/env python3

import sys
import cv2
import numpy as np


def custom_erosion(img, kernel_size):
    """
    Morphological erosion in grayscale.
    For each pixel, we take the minimum value within the local neighborhood
    defined by kernel_size x kernel_size.
    """
    
    # Output image of the same size as the original (but will be modified later).
    out = img.copy()

    ## Establish dimensinos of image
    nrows=img.shape[0]
    ncols=img.shape[1]

    minrow=0
    maxrow=nrows
    mincol=0
    maxcol=ncols

    
    

    for row in range(0,nrows):
        ## Establish floors and ceilings so that pixels which do not exist are not called
        min_legal_boundary_row=max(row-kernel_size,minrow)
        max_legal_boundary_row=min(row+kernel_size,maxrow)

        
        for col in range(0,ncols):
            ## Establish floors and ceilings so that pixels which do not exist are not called
            min_legal_boundary_col=max(col-kernel_size,mincol)
            max_legal_boundary_col=min(col+kernel_size,maxcol)

                
            # print('ROW RANGE: '+str(min_legal_boundary_row)+', ',str(max_legal_boundary_row)+'COL RANGE: '+str(min_legal_boundary_col)+', ',str(max_legal_boundary_col))


    
            # Extract the region of interest from the image.
            # This region is kernel_size x kernel_size around (x, y).
            roi = img[min_legal_boundary_row : max_legal_boundary_row+1, min_legal_boundary_col:max_legal_boundary_col+1]
            # Erosion in grayscale: take the minimum value in the neighborhood.
            out[row, col] = np.min(roi)

    return out

def custom_dilation(img, kernel_size):
    """
    Morphological erosion in grayscale.
    For each pixel, we take the minimum value within the local neighborhood
    defined by kernel_size x kernel_size.
    """


    # Output image of the same size as the original (but will be modified later).
    out = img.copy()

    ## Establish dimensinos of image
    nrows=img.shape[0]
    ncols=img.shape[1]

    minrow=0
    maxrow=nrows
    mincol=0
    maxcol=ncols


    for row in range(0,nrows):
        ## Establish floors and ceilings so that pixels which do not exist are not called
        min_legal_boundary_row=max(row-kernel_size,minrow)
        max_legal_boundary_row=min(row+kernel_size,maxrow)

        
        for col in range(0,ncols):
            ## Establish floors and ceilings so that pixels which do not exist are not called
            min_legal_boundary_col=max(col-kernel_size,mincol)
            max_legal_boundary_col=min(col+kernel_size,maxcol)
            
            # print('ROW RANGE: '+str(min_legal_boundary_row)+', ',str(max_legal_boundary_row)+'COL RANGE: '+str(min_legal_boundary_col)+', ',str(max_legal_boundary_col))

    
            # Extract the region of interest from the image.
            # This region is kernel_size x kernel_size around (x, y).
            roi = img[min_legal_boundary_row : max_legal_boundary_row+1, min_legal_boundary_col:max_legal_boundary_col+1]
            # Erosion in grayscale: take the minimum value in the neighborhood.
            out[row, col] = np.max(roi)

    return out 


def ClosingOpeningAlternatedFilter(img,i):

   
    ## Apply the Dilation and then Erosion  (Closing)

    img_pt_2=custom_dilation(img,i)
    
    img_pt_3=custom_erosion(img_pt_2,i)

    ## Apply the Erosion and then Dilation (Opening)

    img_pt_4=custom_erosion(img_pt_3,i)
    
    img_pt_5=custom_dilation(img_pt_4,i)

    return img_pt_5

## Create a function that checks idempotence for ClosingOpening using i=1
def verifyClosingOpeningFilterIdempotence(image_path):
    
    ## Read image
    img=cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    ## Apply Opening Closing 1x
    img_1=ClosingOpeningAlternatedFilter(img,1)

    ## Apply Opening Closing 2x
    img_2=ClosingOpeningAlternatedFilter(ClosingOpeningAlternatedFilter(img,1),1)

    ## Apply Opening Closing 3x
    img_3=ClosingOpeningAlternatedFilter(ClosingOpeningAlternatedFilter(ClosingOpeningAlternatedFilter(img,1),1),1)


    ## Establish dimensinos of image
    nrows=img_1.shape[0]
    ncols=img_1.shape[1]

    ## Assume equality until proven otherwise
    are_equal=True
    for row in range(0,nrows):
        for col in range(0,ncols):
            cur_pixel_img_1=img_1[row,col]
            cur_pixel_img_2=img_2[row,col]
            cur_pixel_img_3=img_3[row,col]
            
            if (cur_pixel_img_1==cur_pixel_img_2==cur_pixel_img_3)!=True:
                are_equal=False
    return are_equal


## Test Case Number 1 - Size 1  
test1Exercise7a=verifyClosingOpeningFilterIdempotence('src/cam_74.pgm')

print(test1Exercise7a)

with open('output/test1Exercise7a.txt','w') as file:
    if test1Exercise7a==True:
        file.write('The image is the same with 1, 2 and 3 sequential ClosingOpening Filters applied, and the idempotence holds.')
    else:
        file.write('The image is not the same with 1, 2 and 3 sequential ClosingOpening Filters applied, the idempotence does not hold.')


