## Exercise 2A

import cv2

# Define Function
def Exercise2A(image_path,value):
    ## ingest file given the path and ensure it is in grayscale mode
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    ## Make a copy of the given image to modify later
    new_img=img.copy()
    
    # Get Image dimensions
    nrows=img.shape[0]
    ncols=img.shape[1]

    ## Iterate through each row and column (each pixel)
    for row in range(0,nrows):
        for col in range(0,ncols):
            #Set a current value 
            cur_pixel=img[row,col]
            ## Change pixel if it exceeds the threshold value
            if cur_pixel>value:
                new_img[row,col]=value
    ## Return new image
    return new_img 


## Test Case Number 1 
test1Exercise2A=Exercise2A('src/cam_74.pgm',75)

## Save Image
cv2.imwrite("src/test1Exercise2A.pgm", test1Exercise2A);

## Test Case Number 2
test2Exercise2A=Exercise2A('src/cam_74.pgm',10)

## Save Image
cv2.imwrite("src/test2Exercise2A.pgm", test2Exercise2A);

## Test Case Number 3
test3Exercise2A=Exercise2A('src/cam_74.pgm',199)

## Save Image
cv2.imwrite("src/test3Exercise2A.pgm", test3Exercise2A);

