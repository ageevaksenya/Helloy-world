for i in range (210235, 210301):
        x=0
        v=i/2
        if round(v,0) == int(v):
	    v+=1
	else:
	    continue
        for n in range (2, round(v)+1):
            if i//n == 0:
                x+=1
            else:
                continue
            if x == 2:
                print(i)
            else:
                break
        
