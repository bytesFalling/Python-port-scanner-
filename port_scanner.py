#importing all required libraries 
import socket

def main():
        #Output message 
        print ( "bytesFalling present\n" )
        print ( "Python port scanner\n" )

        #calling function
        portScan()


def portScan():
        #Colling user input 
        user_input    = input("Enter a remote host to scan: ")
        ip_addr  = socket.gethostbyname(user_input)

        #Using for loop to scan for ports
        for port in range(1,1000):
                #Creating socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                port_results = sock.connect_ex((ip_addr, port))
                 #validating and printing the results.
        if port_results == 0:
                print ("Open: ".format(port_results))

        else:
                print ( "All Ports are close")

        
        #closing socket     
        sock.close()

#calling main function
main()
