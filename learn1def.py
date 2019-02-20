def learnOLERegression(X,y):
    # Inputs:                                                         
    # X = N x d 242 X 64
    # y = N x 1 242 X 1                                                              
    # Output: 
    # w = d x 1 
    
    #calc mean
    mX = np.mean(X)
    mY = np.mean(y)

    # calc terms for beta and alpha
    wX = (X - mX) * (y - mY)
    sX = (X - mX)**2
    
    # calc beta and alpha
    b = np.sum(wX) / np.sum(sX)
    a = mY - (b * mX)
    
    est = a + b * X

    # IMPLEMENT THIS METHOD - REMOVE THE NEXT LINE
    w = np.zeros((X.shape[0],1))
    return est
