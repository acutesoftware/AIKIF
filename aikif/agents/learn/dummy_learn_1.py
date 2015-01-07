# dummy_learn_1.py     # written by Duncan Murray 7/1/2015


    
def main(arg1=55, arg2='test', arg3=[5,6,7,5,4,]):
    """
    This is a sample program to show how a learning agent can
    be logged using AIKIF. 
    The idea is that this main function is your algorithm, and 
    you there are several functions you can add to allow for easy
    logging access
    """
    print('Starting dummy AI algorithm with :', arg1, arg2, arg3)
    
    
    result = arg1 + arg3[0] * 7566.545  # dummy result
    
    print('Done - returning ', result)
    return result
    
   
if __name__ == '__main__':   
    main()
    