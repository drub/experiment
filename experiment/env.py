#!/Users/thedrub/anaconda3/bin/python

# ----------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------
import sys
import os


def Get_Input_Files(fname):

    #print(os.environ) #deubg
    print(fname)

    if fname in os.environ:
        # The ENV variable exists. Return the file list.
        print("Found: " + fname) #deubg
        print("Contents: " + os.environ[fname]) #deubg
        return os.environ[fname]
    else:
        print("Error: ")
        exit()

# Main
#file_list = Get_Input_Files("PATH")
file_list = Get_Input_Files("GETHRSPATH")

print(file_list)
#print("File list: " + file_list)

exit()

