from os import listdir
from os.path import isfile, join

file_path = ".\\Pictures\\Pix\\" # Fixed path, original pix files
new_file_path = ".\\Pictures\\Pix_Rotated\\" # Fixed path, new rotated files

# List of pix files in original folder
onlyfiles = [f for f in listdir(file_path) if isfile(join(file_path, f))]

for file_name in onlyfiles:
    # open original pix file
    f = open(file_path + file_name, "r") # read only
    pix = f.read() # save as string
    f.close() # closes pix file

    # Since pix is a string, I have to identify where the logo beings
    logo = "logo=("
    x = pix.find(logo) # This is the position in the string of the logo( statement
    start_end = x + len(logo) # the start of the file ends with the (
    start = pix[0:start_end] # this is the entire start of the file. Won't change
    header_begin = start_end # the header starts where the start ends
    # Header is comprised of: 128 columns + 2x" + 1x, + 1xLF times 16 lines
    header_end = header_begin + (131*16) + 16
    header = pix[header_begin:header_end] # this is the header
    banner = pix[header_end:-2] # the banner begins where the header ends minus ) + LF

    # New pix for rotated oleds!!!!!!!
    new_pix = start + banner + ",\n" + header[:-2] + ")\n" # header is now footer!

    # Use newline="\n" to prevent "\n" to be changed to "\r\n", otherwise display won't load
    f_new = open(new_file_path + file_name, "w" , newline='\n') 
    f_new.write(new_pix)
    f_new.close()