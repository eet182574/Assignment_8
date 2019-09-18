# PS1.py: Program to handle bit message stream.
# Author: Parveen Bajaj
# This Program takes in a msg in binary format from user and find its parity and Modify  
# the message as per assginment instructions.
import sys

if __name__ == "__main__":
    
  
    # Check for arguments
    if len(sys.argv) != 2:
        print "Arguments Mismatch"
        print "Run <exec> <binary string>"
        exit()
    
    msg= sys.argv[1]

    length = len(msg)
    
    # find parity of message
    parity = 0
    temp = 0
    for i in range(length):
        if msg[i] == '1':
            temp += 1         
    
    # Check for even parity and if even bits, set parity bit to 1
    
    if temp % 2 == 0:
        parity = 1
        
    parity_msg = msg + str(parity)
    
    print "Parity Bit Data:", parity_msg
    
    # Modify parity_msg to  make it frame of Data layer
          
    parity_msg = parity_msg.replace('010','0100')
        
    final_msg = parity_msg + '0101'
    
    print "Transmitting data:",final_msg
