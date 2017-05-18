# audio_tools.py  written by Duncan Murray 19/8/2014
# sources:
# https://mutagen.readthedocs.org/en/latest/api/id3.html#mutagen.mp3.MPEGInfo
# https://bitbucket.org/lazka/mutagen/issue/162/python3-no-tags-visible-in-mp3-file
#   (above shows bug in python 3 - suggests
#    https://pypi.python.org/pypi/mutagenx
# https://musicbrainz.org/doc/MusicBrainz_Picard/Tags/Mapping
# 

try:
    import mutagenx
    import mutagenx.id3
except ImportError:
    print("Error: cant import mutagen")
    
def TEST():
    """ local test to demo usage - see unittests for full functionality """
    
    print("Local test of audio_tools.py")
    fname = r"E:\backup\music\Music\_Rock\Angels\Red Back Fever\07 Red Back Fever.mp3"
    #res = get_audio_metadata(fname)
    #print(res)

    res = get_audio_metadata(fname)
    print(res)
    #{'album': ['Red Back Fever'], 'title': ['Red Back Fever'], 'artist': ['Angels']}    

    
    

def get_audio_metadata(fname):
    """ collects basic MP3 metadata
    Works, once you use mutagenx (buried deep in issues page)
    ['Angels']
    ['Red Back Fever']
    ['Red Back Fever']
    {'album': ['Red Back Fever'], 'title': ['Red Back Fever'], 'artist': ['Angels']}    
    """
    from mutagenx.easyid3 import EasyID3
    audio = EasyID3(fname)
    audio_dict = {}
    
    try:
        artist = audio["artist"]
    except KeyError:
        artist = ''
        
    try:    
        title = audio["title"]
    except KeyError:
        print("Cant get title")
        
    try:
        album = audio["album"]
    except KeyError:
        album = ''
        
    
    audio_dict['album'] = album
    audio_dict['title'] = title
    audio_dict['artist'] = artist
    
    return audio_dict
        
def get_audio_metadata_old(fname):
    """ retrieve the metadata from an MP3 file """
    audio_dict = {}
    print("IDv2 tag info for %s:" % fname)
    try:
        audio = mutagenx.id3.ID3(fname, translate=False)
    except StandardError as err:
        print("ERROR = " + str(err))
    #else:
        #print(audio.pprint().encode("utf-8", "replace"))
        #for frame in audio.values():
        #    print(repr(frame))
    
    try:
        audio_dict["title"] = audio["title"]
    except KeyError:
        print("No title")
        
    try:
        audio_dict["artist"] = audio["artist"] # tags['TPE1'] 
    except KeyError:
        print("No artist")
        
    try:
        audio_dict["album"] = audio["album"]
    except KeyError:
        print("No album")
        
    try:
        audio_dict["length"] = audio["length"]
    except KeyError:
        print("No length")
        
    #pprint.pprint(audio.tags)
        
    return audio_dict


    
        
if __name__ == '__main__':    
    TEST()  