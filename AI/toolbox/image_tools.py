# image_tools.py  written by Duncan Murray 1/7/2014


try:
    from PIL import Image
    print("PIL imported OK")
except ImportError:
    print("--------------------------------------------------------------------------")
    print("Error: Cant import PIL")
    print("you need to run 'easy_install pillow' for PIL functionality in 3.4")
    print("Also, you need to ensure Python 3.4 is used, e.g.")
    print("  >   C:\python34\python.exe image_tools.py")
    print("--------------------------------------------------------------------------\n")
    

def check_image_duplicates(file_list):
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
    #Return the Hamming distance between equal-length sequences
    # (http://en.wikipedia.org/wiki/Hamming_distance )
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))        
        
        
def get_img_hash(image, hash_size = 8):
    # Grayscale and shrink the image in one step.

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
    img = Image.open(fname)
    width, height = img.size
    pixels = list(img.getdata())
    for col in xrange(width):
        print (pixels[col:col+width])
        
        
  