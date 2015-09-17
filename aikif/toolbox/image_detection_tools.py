#!/usr/bin/python3
# coding: utf-8
# image_detection_tools.py  written by Duncan Murray 17/9/2015

import os

try:
    #    from PIL import Image as ImagePIL
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
    from PIL import ImageFilter
    from PIL.ExifTags import TAGS, GPSTAGS
    from PIL import ImageStat
    from PIL import ImageOps

except ImportError:
    print("--------------------------------------------------------------------------")
    print("Error: Cant import PIL")
    print("you need to run 'easy_install pillow' for PIL functionality in 3.4")
    print("--------------------------------------------------------------------------\n")
    
"""

SCIPY examples with PIL
https://scipy-lectures.github.io/advanced/image_processing/

http://docs.scipy.org/doc/scipy/reference/tutorial/ndimage.html

http://docs.scipy.org/doc/scipy/reference/ndimage.html

http://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.measurements.find_objects.html



TODO
=====
Attempt to use a path finding / line trace method to detect objects 
drawn on a map rather than traditional pattern match against existing
set of training images.

Reason is, that it would be easier to define map objects mathematically
and it should be similar to the path finding routine that follows the 
roads

"""

def TEST(fname):
    """
    Test function to step through all functions in
    order to try and identify all features on a map
    This test function should be placed in a main 
    section later
    """
    #fname = os.path.join(os.getcwd(), '..','..',  # os.path.join(os.path.getcwd(), '
    m = MapObject(fname, os.path.join(os.getcwd(), 'img_prog_results'))
    m.add_layer(ImagePathFollow('border'))
    m.add_layer(ImagePathFollow('river'))
    m.add_layer(ImagePathFollow('road'))
    
    m.add_layer(ImageArea('sea', col='Blue', density='light'))
    m.add_layer(ImageArea('desert', col='Yellow', density='med'))
    m.add_layer(ImageArea('forest', col='Drak Green', density='light'))
    m.add_layer(ImageArea('fields', col='Green', density='light'))
    
    m.add_layer(ImageObject('mountains'))
    m.add_layer(ImageObject('trees'))
    m.add_layer(ImageObject('towns'))
            
    
    
##############################################
# Main Functions to call from external apps  #   
##############################################

def get_roads(fname):
    """
    takes a filename and returns a vector map
    (or possibly an image layer) of roads on 
    the map
    """
    return []


##############################################
# Utility functions                          #   
##############################################

def img_to_array(fname):
    """
    takes a JPG file name and loads into an array
    """
    img = Image.open(fname)
    return img


##############################################
# Classes used for managing image detection  #   
##############################################
    
class MapObject(object):
    """
    base class used to hold objects detected on a map.
    Takes a filename which it loads into the first layer
    of an array.
    Additional layers are added mapped to same [x,y] 
    points for each additional feature extraction done.
    """
    def __init__(self, fname='', op_folder=''):
        self.arr = []
        self.arr.append(img_to_array(fname))
        
    def add_layer(self, layer):
        """
        creates a new layer in the self.arr and sets
        to zeros,ready for next image processing task
        """
        self.arr.append(layer)
        
  
class ImagePathFollow(object):
    """
    class to handle the long lines line
    drawn on the map - eg borders, rivers, roads, 
    """
    def __init__(self, nme):
        #super(ImagePathFollow, self).__init__(fname, op_folder)
        self.nme = nme
        self.arr = []
    
  
class ImageObject(object):
    """
    class to handle the list of small objects that are
    drawn on the map - eg mountains, trees, towns
    """
    def __init__(self, nme):
        #super(ImagePathFollow, self).__init__(fname, op_folder)
        self.nme = nme
        self.arr = []
    
class ImageArea(object):
    """
    class to handle the list of AREAS on the map.
    These are the regions for sea, land, forest, 
    desert and are mainly based on colours or 
    styles.
    
    mountains, trees
    """
    def __init__(self, nme, col, density):
        #super(ImagePathFollow, self).__init__(fname, op_folder)
        self.nme = nme
        self.arr = []
        self.col = col
        self.density = density
    
#TEST('')        