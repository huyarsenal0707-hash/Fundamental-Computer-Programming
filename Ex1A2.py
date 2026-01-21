def  check_zander_size():
    zander_length = float(input("Enter the length of the zander: "))
    
    
    if zander_length < 42:
        print("The zander is undersized and must be released back to the lake.")
        print(f'The fish is {42 - zander_length:.1f} cm below the size limit.')
    else:
        print("The zander meets the size requirement and can be kept.")
check_zander_size()
     
        
    
    