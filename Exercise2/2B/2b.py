## Exercise 2B

import cv2

def Exercise2B(image1_path,image2_path,output_file_name):
    
    ## Ingest Images from file paths
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    

    ## Check n_pixels
    if img1.size!=img2.size:
        ## In case the images are not of equal file size, write automatically 0
        with open('output/'+output_file_name,'w') as file:
            file.write('0')
            file.close()
    ## If pixel arguments are equal, continue with code
    else:
        ## Assume the images are the same at first until proven otherwise
        are_equal=True

        ## Set dimensions
        nrows=img1.shape[0]
        ncols=img1.shape[1]
        
        ## Iterate through each row and column (each pixel)
        for row in range(0,nrows):
            for col in range(0,ncols):
                ## Set a value for the current pixel of each image
                cur_pixel_img1=img1[row,col]
                cur_pixel_img2=img2[row,col]
                ## Check for equality, and set to false if values are not equal
                if cur_pixel_img1!=cur_pixel_img2:
                    are_equal=False
        ## Finally, write to file the outcome
        with open('output/'+output_file_name,'w') as file:
            file.write(str(int(are_equal)))
            file.close()



## Test on the same Image
test1Exercise2B=Exercise2B('src/cam_74.pgm','src/cam_74.pgm','exercise_02b_output_01.txt')

## Test on Different Images
test1Exercise2B=Exercise2B('src/cam_74_threshold100.pgm','src/cam_74.pgm','exercise_02b_output_02.txt')


