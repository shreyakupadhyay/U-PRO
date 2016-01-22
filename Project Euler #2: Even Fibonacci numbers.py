# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case = input()
for i in range(0,test_case):
    val = input()
    val_first = 2
    val_second = 8
    val_third = 34
    count = 0
    while(val_first < val):
        if(val_first%2==0):
            count = count + val_first
        if(val_second%2==0 and val_second <= val):
            count = count + val_second
        if(val_third%2==0 and val_third <= val):
            count = count + val_third
        #print count, " sd"
        val_first = val_second + 4*val_third
        val_second = val_third + 4*val_first
        val_third =  val_first + 4*val_second 
        #print val_first,val_second,val_third
    print count
       
        
