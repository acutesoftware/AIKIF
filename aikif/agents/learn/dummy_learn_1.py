# dummy_learn_1.py     # written by Duncan Murray 7/1/2015


    
def main(arg1=55, arg2='test', arg3=None):
    """
    This is a sample program to show how a learning agent can
    be logged using AIKIF. 
    The idea is that this main function is your algorithm, which
    will run until it finds a successful result. The result is 
    returned and the time taken is logged.
    
    There can optionally be have additional functions 
    to call to allow for easy logging access
    """
    print(('Starting dummy AI algorithm with :', arg1, arg2, arg3))
    
    if arg3 is None:
        arg3=[5,6,7,5,4,]
    result = arg1 + arg3[0] * 7566.545  # dummy result
    
    print(('Done - returning ', result))
    return result


def API_option_1_get_best_result():
    """
    example API call that you would implement in your AI algorithm
    that returns the best result so far. This will be useful for 
    running multiple simulations with a range of parameters and 
    tracking the result by time (so to halt progress when diminishing
    returns occur, eg when it gets within 99.9% there is often little
    point in continuing for another 2 days
    """
    return 6.00006  # example
   
if __name__ == '__main__':   
    main()
    