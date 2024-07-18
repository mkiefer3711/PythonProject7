import sys
# This was the highest limit I could set for it to not error out, meaning the highest limit for my computer
sys.setrecursionlimit(2130)
count = 0
# Function that calculates the Ackerman Function
def ack(x,y,z):
    # Adds the count variable to the function to keep a counter
    global count
    count = count + 1
    # If statements for the Ackerman Function
    if x == 0:
        return y + z
    elif x == 1 and z == 0:
        return y * z
    elif x == 2 and z == 0:
        return y ** z
    elif x > 2 and z == 0:
        return y
    elif x > 0 and z > 0:
        return  ack(x-1, y, ack(x,y,z-1))
# Function that contains exception handling, prints and formats each answer
def callAck(x,y,z):
    # Try that calls ack function and will print the result
    try:
        global count
        count = 0
        print(f"ack({x:<2},{y:<2},{z:<2}):", end=" ")
        test = ack(x,y,z)
        print(f"{test:<18}", end=" ")
        print(f"count: {str(count):<12}" )
    # Except that will print the stack overflow error if recursion limit is too high    
    except Exception as e:
        stackerr ="Stack overflow"
        print(f"{stackerr:<18}", end=" ")
        print(f"count: {str(count):<12}" )
# Main function where the program starts
def main():
    # Calls the callAck function to calculate and print each value
    print("Value of the Ackerman Function\n\n")
    callAck(0,5,3)
    callAck(0,11,33)
    callAck(1,5,3)
    callAck(1,11,33)
    callAck(2,5,3)
    callAck(2,9,5)
    callAck(3,2,2)
    callAck(3,2,3)
    callAck(3,3,1)
    callAck(3,3,2)
    callAck(4,2,1)
    callAck(5,1,2)
    callAck(5,2,1)
    callAck(6,1,99)
    print("\n\nDone!")
# Calls the main function
main()