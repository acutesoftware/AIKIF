# image_tools.py  written by Duncan Murray 1/7/2014

import sys
import os

try:
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
    from PIL import ImageFilter
    from PIL.ExifTags import TAGS, GPSTAGS
    from PIL import ImageStat
    from PIL import ImageOps
    
    print("PIL imported OK")
except ImportError:
    print("--------------------------------------------------------------------------")
    print("Error: Cant import PIL")
    print("you need to run 'easy_install pillow' for PIL functionality in 3.4")
    print("Also, you need to ensure Python 3.4 is used, e.g.")
    print("  >   C:\python34\python.exe image_tools.py")
    print("--------------------------------------------------------------------------\n")
    
def TEST():
    """ local test to demo usage - see unittests for full functionality """
    print("Local test of image_tools.py")
    print_all_metadata('..\\..\\doc\\web-if-progs-v01.jpg')
    
    # save CSV file of metadata
    with open('..\\..\\tests\\test_results\\image_metadata.csv', 'w') as f:
        f.write(List2String(metadata_header(), ", ") + '\n')
        f.write(get_metadata_as_csv('..\\..\\doc\\web-if-progs-v01.jpg') + '\n')
        f.write(get_metadata_as_csv('..\\..\\doc\\AIKIF-Overview.jpg') + '\n')
        f.write(get_metadata_as_csv('..\\..\\doc\\AIKIF-data-structure.jpg') + '\n')
        f.write(get_metadata_as_csv('..\\..\\doc\\AIKIF-learning.jpg') + '\n')
        f.write(get_metadata_as_csv('..\\..\\doc\\AIKIF-ProcessFlow.jpg') + '\n')



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
        #print("IN GET_LAT_LONG - GPSInfo = ", gps_info)
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
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
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

    
def print_exif_data(img):   
    """ NOTE - the img is ALREADY opened by calling function """
    try:
        exif_data = {
            TAGS[k]: v
            for k, v in img._getexif().items()
            if k in TAGS
        }
        
        for k,v in exif_data.items():
            if k:
                if type(v) is str:
                    #if  v[1:] != 'b':
                    print (k , " : ", v)
                elif type(v) is int:    
                    print (k , " : ", v)
                elif type(v) is tuple:    
                    print (k , " : ", v)
                else:
                    #pass
                    #print("NON STRING? = ", k, " : ", type(v))
                    if k == "GPSInfo":
                        pass
                        #print(v) - this is now done by get_exif_data
        #print("exif_data       :", exif_data)
    except:
        print ("Error - ", sys.exc_info()[0])

        
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
    max_dim = max(img.size)
    print("Width      :", width)
    print("Height     :", height)
    print("Format     :", img.format)
    print("palette    :", img.palette )
     
    print_stats(img)
    print_exif_data(img)
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
	for k, v in d: # .iteritems():
		res = res + k + ',' + str(v) + ','
	return res

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False    

def get_metadata_as_csv(fname):
    """ Gets all metadata and puts into CSV format """
    q = chr(34)
    d = ","
    res = q + fname + q + d
    res = res + q + os.path.basename(fname) + q + d
    res = res + q + os.path.dirname(fname) + q + d
    res = res + q + str(os.path.getsize(fname)) + q + d
    try:
        img = Image.open(fname)
        # get the image's width and height in pixels
        width, height = img.size
        res = res + q + str(width) + q + d
        res = res + q + str(height) + q + d
        res = res + q + str(img.format) + q + d
        res = res + q + str(img.palette) + q + d
        stat = ImageStat.Stat(img)
         
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
    except:
        pass
    return res
        
        
def auto_contrast(img, opFile):
    """ run the autocontrast PIL function to a new opFile """
    imgOp = ImageOps.autocontrast(img)
    imgOp.save(opFile)
    
    
def add_text_to_image(fname, txt, opFilename):
    """ convert an image by adding text """
    ft = ImageFont.load("T://user//dev//src//python//_AS_LIB//timR24.pil")
    wh = ft.getsize(txt)
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
    """ TODO - not implemented """
    storage = cv.CreateMemStorage()
    haar=cv.LoadHaarClassifierCascade('haarcascade_frontalface_default.xml')
    detected = cv.HaarDetectObjects(fname, haar, storage, 1.2, 2,cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected:
        for face in detected:
            print (face)
    
def check_image_duplicates(file_list):
    """ Checking Images for duplicates (despite resizing, colours, etc) """
    master_hash = ''
    ham_dist = 0
    
    print("Checking Images for duplicates (despite resizing, colours, etc) " )
    for ndx, fname in enumerate(test_files):
        hash = get_img_hash(Image.open(fname))
        if ndx == 0:  # this is the test MASTER image
            master_hash = hash
        else:
            # compare hamming distance against image 1  
            #print("hash=" + hash + "  MASTER_HASH=" + master_hash)
            ham_dist = hamming_distance(hash, master_hash)
        print(hash + " <- " + fname + " ,  hamming dist to img1 = " + str(ham_dist))

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
    """ read an image from file """
    return Image.open(fname)
    
def dump_img(fname):
    """ output the image """
    img = Image.open(fname)
    width, height = img.size
    pixels = list(img.getdata())
    for col in xrange(width):
        print (pixels[col:col+width])
        
        
if __name__ == '__main__':    
    TEST()  