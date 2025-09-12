def solution(requestTimestamps, windowLength, maxInWindow): # windowLength # windowLength # requests = [ 1, 3, 4, 6 ] windowLength = 4 maxInWindow = 2 # [1,1,0,1,1,0,1] # currentReq = 0 # result = [] reqs = [0] * (requestTimestamps[len(requestTimestamps)-1]) print(reqs) for i in range(0,len(requestTimestamps)): index = requestTimestamps[i] - 1 print(f"{i} and {index}") reqs[index] = 1 print # 1,1,0,1,1,0,1 currentReq = 0 i, j = 0, 0 while((j - i) < windowLength): # there is a request at this place if reqs[j] == 1: currentReq += 1 if currentReq <= maxInWindow: result.append(True) else: result.append(False) print(j) j += 1 # 1,1,0,1,1,0,1, maxInWindow = 3, windowLength = 4 while j <= len(reqs): # 0,1,0,1,1,0,1 if reqs[i] == 1: currentReq -= 1 if reqs[j] == 1: currentReq += 1 print(currentReq) if currentReq <= maxInWindow: result.append(True) else: result.append(False) j += 1 i += 1 # return result
    result = []
    reqs = [0] * (requestTimestamps[-1])  # Initialize request array based on the last timestamp
    for timestamp in requestTimestamps:
        reqs[timestamp - 1] = 1  # Mark the request at the corresponding index

    currentReq = 0
    i, j = 0, 0

    while j < len(reqs) and (j - i) < windowLength:
        if reqs[j] == 1:
            currentReq += 1
            if currentReq <= maxInWindow:
                result.append(True)
            else:
                result.append(False)
        j += 1

    while j < len(reqs):
        if reqs[i] == 1:
            currentReq -= 1
        if reqs[j] == 1:
            currentReq += 1
            print(currentReq)
            if currentReq <= maxInWindow:
                result.append(True)
            else:
                result.append(False)
        
        j += 1
        i += 1

    return result


print(solution([1, 3, 4, 6], 4, 2))  # [True, True, False, True, True, False, True]