def ternarySearch (a , k ):
    n = len ( a )
    if ( n == 0):
        return False
    if ( n <= 2):
        for i in range (0 , n ):
            if ( a [ i ] == k ):
                return True
        return False
    t1 = n /3
    t2 = 2* n /3
    if ( a [0] >= k and k < a [ t1 ]):
        print a[0:t1], k
        return ternarySearch ( a [0: t1 ] , k )
    elif ( a [ t1 ] <= k and k < a [ t2 ]):
        print a[t1:t2], k
        return ternarySearch ( a [ t1 : t2 ] , k )
    elif ( a [ t2 ] <= k and k <= a [n -1]):
        print a[t2:n], k
        return ternarySearch ( a [ t2 : n ] , k )
    else :
        return False

print ternarySearch( [1,3,5,10,12,15,32,91,125,132], 18)
