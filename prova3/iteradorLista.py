def fromTail( lista ):   

    iter = lista.tail        

    while iter.before is not None:        
        
        print(iter.value)

        iter = iter.before

    print(iter.value)

    return iter