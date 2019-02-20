def learnOLERegression(X,y):
    # Inputs:                                                         
    # X = N x d 
    # y = N x 1                                                               
    # Output: 
    # w = d x 1 

    # IMPLEMENT THIS METHOD - REMOVE THE NEXT LINE
    
    
    N = X.shape[0]
    d = X.shape[1]
    w = np.zeros((d,1))
    ymean = 0
    xmean = np.zeros((d,1))
    
    for i in range(N):
#         add all the y's
        ymean += y[i]
        for j in range(d):
#             add all the x's in each column
            xmean[j] += X[i][j]
#     average the y's
    ymean = ymean / N
#     average each column of x's
    for i in range(d):
        xmean[i] = xmean[i] / N
        
    num = 0
    den = 1
    for i in range(d):
        for j in range(N):
#             sum of (x-xmean)*(y-ymean)
            num += (X[j][i] - xmean[i]) * (y[j] - ymean[0])
#             sum of (x-xmean)^2
            den += (X[j][i] - xmean[i]) * (X[j][i] - xmean[i])
            
#         weights? for each row (d x 1 matrix)
        w[i] = num / den
        
#     print(w)
    
    
    return w