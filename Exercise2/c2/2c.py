## Exercise 2C

import cv2

## Use method of either 'inf' or 'sup' in argument
def Exercise2C(image1_path,image2_path,method):
    ## Read image file paths
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    
    ## Set a copy of the first image for output later
    new_img=img1
    
    ## Check n_pixels
    if img1.size!=img2.size:
        raise ValueError("Images Sizes are not Equal")
    
    ## Continue with code if image sizes are equal
    else:
        ## Set dimensions of images
        nrows=img1.shape[0]
        ncols=img1.shape[1]
        
        ## Iterate through each row and column (each pixel)
        for row in range(0,nrows):
            for col in range(0,ncols):
                ## Set a value for the current pixel of each image
                cur_pixel_img1=img1[row,col]
                cur_pixel_img2=img2[row,col]
                ## Use the Min of the two pixels if Inf
                if method=='inf':
                    new_img[row,col]=min(cur_pixel_img1,cur_pixel_img2)
                
                ## Use the max of the two pixels if sup
                elif method=='sup':
                    new_img[row,col]=max(cur_pixel_img1,cur_pixel_img2)
    
    return new_img



## Test on  Image 1 and Image 2 (Inf)
test1Exercise2C=Exercise2C('src/'+'image1.pgm','src/'+'image2.pgm',method='inf')

cv2.imwrite("output/inf.pgm", test1Exercise2C);



## Test on  Image 1 and Image 2 (Sup)
test2Exercise2C=Exercise2C('src/'+'image1.pgm','src/'+'image2.pgm',method='sup')

cv2.imwrite("output/sup.pgm", test2Exercise2C);
