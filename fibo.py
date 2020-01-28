def fibo(target):    
    seq = [0,1]
    cnt = len(seq)
    while (seq[cnt-1] + seq[cnt-2] <= target): 
        seq.append(seq[cnt-1] + seq[cnt-2])   
        cnt += 1
    return(seq)