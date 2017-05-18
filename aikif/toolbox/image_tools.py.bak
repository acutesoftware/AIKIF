#!/usr/bin/python3
# coding: utf-8
# image_tools.py  written by Duncan Murray 1/7/2014

import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import ImageStat
from PIL import ImageOps
try:
    from PIL import ImageGrab
except Exception as ex:
    print('cant load ImageGrab (running on Linux)' + str(ex))

def screenshot(fname):
    """
    takes a screenshot of the users desktop (Currently Win only)
    """
    try:
        im = ImageGrab.grab()
        im.save(fname)
    except Exception as ex:
        print('image_tools.screenshot:cant create screenshot ' + str(ex))
    
def get_exif_data(image):
    """
    Returns a dictionary from the exif data of 
    an PIL Image item. Also converts the GPS Tags
    """
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
 
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
 
    return exif_data
 
def _get_if_exist(data, key):
    if key in data:
        return data[key]
        
    return None
    
def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates 
    stored in the EXIF to degress in float format
    """
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)
 
    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)
 
    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)
 
    return d + (m / 60.0) + (s / 3600.0)
 
def get_lat_lon(exif_data):
    """
    Returns the latitude and longitude, if available, from the 
    provided exif_data (obtained through get_exif_data above)
    """
    lat = None
    lon = None
 
    if "GPSInfo" in exif_data:      
        gps_info = exif_data["GPSInfo"]
        print("IN GET_LAT_LONG - GPSInfo = ", gps_info)
        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')
 
        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":                     
                lat = 0 - lat
 
            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon
 
    return lat, lon
 
def resize(fname, basewidth, opFilename):
    """ resize an image to basewidth """
    if basewidth == 0:
        basewidth = 300
    img = Image.open(fname)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(opFilename)
    #print("Resizing ", fname, " to ", basewidth, " pixels wide to file " , opFilename)
 
def print_stats(img):
    """ prints stats, remember that img should already have been loaded """
    stat = ImageStat.Stat(img)
    print("extrema    : ", stat.extrema)
    print("count      : ", stat.count)
    print("sum        : ", stat.sum)
    print("sum2       : ", stat.sum2)
    print("mean       : ", stat.mean)
    print("median     : ", stat.median)
    print("rms        : ", stat.rms)
    print("var        : ", stat.var)
    print("stddev     : ", stat.stddev)

    
#def print_exif_data(img):   
#    """ NOTE - the img is ALREADY opened by calling function """
#    try:
#        exif_data = {
#            TAGS[k]: v
#            for k, v in img._getexif().items()
#            if k in TAGS
#        }
#        for k,v in exif_data.items():
#            if k:
#                if type(v) is str:
#                    #if  v[1:] != 'b':
#                    print (k , " : ", v)
#                elif type(v) is int:    
#                    print (k , " : ", v)
#                elif type(v) is tuple:    
#                    print (k , " : ", v)
#                else:
#                    if k == "GPSInfo":
#                        pass
#    except Exception:
#        print ("Error - ", sys.exc_info()[0])

        
def print_all_metadata(fname):
    """ high level that prints all as long list """
    print("Filename   :", fname )
    print("Basename   :", os.path.basename(fname))
    print("Path       :", os.path.dirname(fname))
    print("Size       :", os.path.getsize(fname))
    img = Image.open(fname)
    # get the image's width and height in pixels
    width, height = img.size
    # get the largest dimension
    #max_dim = max(img.size)
    print("Width      :", width)
    print("Height     :", height)
    print("Format     :", img.format)
    print("palette    :", img.palette )
     
    print_stats(img)
    #print_exif_data(img)
    exif_data = get_exif_data(img)
    (lat, lon) = get_lat_lon(exif_data)
    print("GPS Lat    :", lat )
    print("GPS Long   :", lon )

def metadata_header():
    hdr = [
        'Filename',
        'Basename',
        'Path',
        'Size',
        'Width',
        'Height',
        'Format',
        'palette',
        'count',
        'sum',
        'sum2',
        'mean',
        'median',
        'rms',
        'var',
        'stddev',
        'GPS_Lat',
        'GPS_Long'
        ]  
    return hdr

def get_metadata_as_dict(fname):
    """ Gets all metadata and puts into dictionary """
    imgdict = {}
    try:
        imgdict['filename'] = fname
        imgdict['size'] = str(os.path.getsize(fname)) 
        imgdict['basename'] = os.path.basename(fname)
        imgdict['path'] = os.path.dirname(fname)
        img = Image.open(fname)
        # get the image's width and height in pixels
        width, height = img.size
        imgdict['width'] = str(width)
        imgdict['height'] = str(height)
        imgdict['format'] = str(img.format) 
        imgdict['palette'] = str(img.palette)
        stat = ImageStat.Stat(img)
         
        #res = res + q + str(stat.extrema) + q + d
        imgdict['count'] =  List2String(stat.count, ",")
        imgdict['sum'] =  List2String(stat.sum, ",")
        imgdict['sum2'] =  List2String(stat.sum2, ",")
        imgdict['mean'] =  List2String(stat.mean, ",") 
        imgdict['median'] =  List2String(stat.median, ",") 
        imgdict['rms'] =  List2String(stat.rms, ",") 
        imgdict['var'] =  List2String(stat.var, ",")
        imgdict['stddev'] =  List2String(stat.stddev, ",") 

        exif_data = get_exif_data(img)
        print('exif_data = ', exif_data)
        (lat, lon) = get_lat_lon(exif_data)
        print('(lat, lon)', (lat, lon))
        imgdict['lat'] =  str(lat)
        imgdict['lon'] =  str(lon)
    except Exception as ex:
        print('problem reading image file metadata in ', fname, str(ex))
        imgdict['lat'] =  'ERROR'
        imgdict['lon'] =  'ERROR'
    return imgdict
        
def get_metadata_as_csv(fname):
    """ Gets all metadata and puts into CSV format """
    q = chr(34)
    d = ","
    res = q + fname + q + d
    res = res + q + os.path.basename(fname) + q + d
    res = res + q + os.path.dirname(fname) + q + d
    try:
        res = res + q + str(os.path.getsize(fname)) + q + d
        img = Image.open(fname)
        # get the image's width and height in pixels
        width, height = img.size
        res = res + q + str(width) + q + d
        res = res + q + str(height) + q + d
        res = res + q + str(img.format) + q + d
        res = res + q + str(img.palette) + q + d
        stat = ImageStat.Stat(img)
        #print(fname, width, height) 
        #res = res + q + str(stat.extrema) + q + d
        res = res + q + List2String(stat.count, ",") + q + d
        res = res + q + List2String(stat.sum, ",") + q + d
        res = res + q + List2String(stat.sum2, ",") + q + d
        res = res + q + List2String(stat.mean, ",") + q + d
        res = res + q + List2String(stat.median, ",") + q + d
        res = res + q + List2String(stat.rms, ",") + q + d
        res = res + q + List2String(stat.var, ",") + q + d
        res = res + q + List2String(stat.stddev, ",") + q + d

        exif_data = get_exif_data(img)
        (lat, lon) = get_lat_lon(exif_data)
        res = res + q + str(lat) + q + d
        res = res + q + str(lon) + q + d
    except Exception as ex:
        print('problem reading image file metadata in ', fname, str(ex))
    return res
        
    
    
def List2String(l, delim):
    res = ""
    for v in l:
        if is_number(v):
            res = res + str(v) + delim
        else:
            res = res + v + delim
    return res

def Dict2String(d):
    res = ","
    for k, v in d.items(): # .iteritems():
        res = res + k + ',' + str(v) + ','
    return res

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False    

        
#def auto_contrast(img, opFile):
#    """ run the autocontrast PIL function to a new opFile """
#    imgOp = ImageOps.autocontrast(img)
#    imgOp.save(opFile)
    
    
def add_text_to_image(fname, txt, opFilename):
    """ convert an image by adding text """
    ft = ImageFont.load("T://user//dev//src//python//_AS_LIB//timR24.pil")
    #wh = ft.getsize(txt)
    print("Adding text ", txt, " to ", fname, " pixels wide to file " , opFilename)
    im = Image.open(fname)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), txt, fill=(0, 0, 0), font=ft)
    del draw  
    im.save(opFilename)
    
def add_crosshair_to_image(fname, opFilename):
    """ convert an image by adding a cross hair """
    im = Image.open(fname)
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=(255, 255, 255))
    draw.line((0, im.size[1], im.size[0], 0), fill=(255, 255, 255))
    del draw  
    im.save(opFilename)

def filter_contour(imageFile, opFile):
    """ convert an image by applying a contour """
    im = Image.open(imageFile)
    im1 = im.filter(ImageFilter.CONTOUR)
    im1.save(opFile)

def detect_face(fname, opFile):
    """ 
    TODO - not implemented 
    storage = cv.CreateMemStorage()
    haar=cv.LoadHaarClassifierCascade('haarcascade_frontalface_default.xml')
    detected = cv.HaarDetectObjects(fname, haar, storage, 1.2, 2,cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected:
        for face in detected:
            print (face, 'saving to ', opFile)
    """
    print("detect_face NOT IMPLEMENTED: ", fname, opFile)
    
    
def check_image_duplicates(file_list):
    """ Checking Images for duplicates (despite resizing, colours, etc) """
    master_hash = ''
    ham_dist = 0
    results = []
    print("Checking Images for duplicates (despite resizing, colours, etc) " )
    for ndx, fname in enumerate(file_list):
        #img = Image.open(fname)
        img = load_image(fname)
        hsh = get_img_hash(img)
        if ndx == 0:  # this is the test MASTER image
            master_hash = hsh
        else:
            # compare hamming distance against image 1  
            #print("hash=" + hash + "  MASTER_HASH=" + master_hash)
            ham_dist = hamming_distance(hsh, master_hash)
        #print(hsh + " <- " + fname + " ,  hamming dist to img1 = " + str(ham_dist))
        #results.append(hsh + " <- " + fname + " ,  hamming dist to img1 = " + str(ham_dist))
        results.append({'hsh':hsh, 'fname':fname, 'dist_to_img1':str(ham_dist)})
    return results

def hamming_distance(s1, s2):
    """ 
    Return the Hamming distance between equal-length sequences
    (http://en.wikipedia.org/wiki/Hamming_distance )
    """
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))        
        
        
def get_img_hash(image, hash_size = 8):
    """ Grayscale and shrink the image in one step """

    image = image.resize((hash_size + 1, hash_size), Image.ANTIALIAS, )

    pixels = list(image.getdata())
    #print('get_img_hash: pixels=', pixels)

    # Compare adjacent pixels.
    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)

    # Convert the binary array to a hexadecimal string.
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2**(index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)

def load_image(fname):
    """ read an image from file - PIL doesnt close nicely """
    with open(fname, "rb") as f:
        i = Image.open(fname)
        #i.load()
        return i
    
def dump_img(fname):
    """ output the image as text """
    img = Image.open(fname)
    width, _ = img.size
    txt = ''
    pixels = list(img.getdata())
    for col in range(width):
        txt += str(pixels[col:col+width])
    return txt    
