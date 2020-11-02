"""
Read and return a dictionary with the Twitter keys.

"""

file = '/Users/liviaclarete/coding/apis_keys/twitter_keys.txt'

    
def return_twitter_keys(file, advtools=True):
    """
    Return dictionary of twitter keys
    Input:
        file: path of the keys
        advtools: if True, returns the categorie's names 
            for the twitter keys asks for
    Output:
        dictionary of twitter keys
    """
    # open the key file
    with open(file, 'r') as f:
        keys = f.readlines()
        f.close()
    
    # transforming the list into a dictionary
    d = {}
    for s in keys:
        l = s.replace('\n', '').split(',')
        idx=0
        d[l[idx]] = l[idx+1]
        idx += 1
        
    
    if advtools==True:
        new_keys = ['app_key', 'app_secret', 'oauth_token', 'oauth_token_secret']
        for new, old in zip(new_keys, list(d.keys())):
            d[new] = d.pop(old)
        return d

    else:
        return d