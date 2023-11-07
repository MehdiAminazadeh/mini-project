import cv2
import numpy as np

def gamma_function(image_given:str, alpha, beta, gamma, p1, p2, s1, s2):
    # Get the image dimensions
    image = cv2.imread(image_given)
    height, width, _ = image.shape
    
    # create an output image with the same dimensions and type as the input image
    output_image = np.zeros_like(image)
    
    for y in range(height):
        for x in range(width):
            r = image[y, x, 2]  # Assuming the red channel represents 'r' in the function
            
            if 0 <= r <= p1:
                S = alpha * r
            elif p1 <= r <= p2:
                S = beta * (r - p1) + s1
            else:
                S = gamma * (r - p2) + s2
            
            # Apply the value of S to all color channels (assuming RGB image)
            output_image[y, x] = [S, S, S]
    
    return cv2.imwrite("output.jpg", output_image)


# alpha: float = 1.0  
# beta: float = 2.0
# gamma: float = 2.0
# p1: int = 64
# p2: int = 128
# s1: int = 32
# s2: int = 192

# the following arguments can vary
# alpha, beta and gamma should be float
gamma_function("lena.jpg", alpha, beta, gamma, p1, p2, s1, s2)
