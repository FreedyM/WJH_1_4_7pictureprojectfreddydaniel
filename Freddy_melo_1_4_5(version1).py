import PIL
import os.path  
import PIL.ImageDraw            
    
def logoPlacement(original_image, logo_size, logo, st):
    """places logo on top of image in left corner of an image

    0<logo-size<1, this code uses 4 arguements, rt checking
    if it should change the logos value or not. Plus image files.
    """ 
    width, height = original_image.size
    position = int(logo_size * min(width, height))
    
    rlogo = logo.resize((position, position)) 
    
    result = original_image.copy()
    result.paste(rlogo, (0,0), rlogo)
    return result

