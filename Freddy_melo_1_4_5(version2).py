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

def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, andlogo
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list


def logo_all_images(directory=None,size=0.5, st = False):
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    new_directory = os.path.join(directory, 'logo')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass #if directory already exists, continue on
    
    #load up all images in list
    image_list, file_list = get_images(directory)
    logo = PIL.Image.open('/Users/229017/Desktop/SourPodsCandy.png') 
   
     # Go through the images and save modified versions 
    for n in range(len(image_list)):
        print n
        filename, filetype = file_list[n].split('.')
        
        new_image = image_list[n]
        new_image = logoPlacement(image_list[n], size, logo, st)

        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        
    