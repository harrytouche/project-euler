"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""



n_ways = 1 # pre-fill £2

for h in range(3):
    
    for f in range(5):
        
        for t in range(11):
            
            for te in range(21):
                
                for fi in range(41):
                    
                    for tw in range(101):
                        
                        o = 200 - (100*h + 50*f + 20*t + 10*te + 5*fi + 2*tw)
                        
                        if o >=0:
                            
                            #print("found!")
                            #print(h, f, t, te, fi, tw, o)
                            #input("Press enter to continue...")
                            n_ways += 1
                            
                        else:
                            break
                            
            
                            
                            