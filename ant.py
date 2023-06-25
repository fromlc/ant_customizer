#-----------------------------------------------------------------------
# ant.py
#
# Customizer for Netlab's Advanced Networking Tab options
# Author: L. Carver
# 
# - Developed with Python 3.11
# - Make sure the template file exists in the current folder
# - Uses template file name 'advanced_networking_tab_template.txt'
# - Outputs to file 'advanced_networking_tab.txt'
#-----------------------------------------------------------------------
import os

filename_in = "advanced_networking_tab_template.txt"
filename_out = "advanced_networking_tab.txt"

print("\nOutput will be written to file '" + filename_out + "'")
print("Reading options template file '" + filename_in + "'...")

# check for input template file in current folder
if not os.path.isfile(filename_in):
    print("\nMake sure the options template file '" + filename_in + "' exists in this folder, then try again.")
    quit()

f_in = open(filename_in)
f_out = open(filename_out, "w")

print("\nAt each prompt, enter setting to use OR")
print("press <enter> to accept the default setting shown\n")

for x in f_in:
    # display comment lines and write to output file
    if x[0] == "#":
        print(x)
        f_out.write(x)
        continue

    # check for settable option in this format: option=/setting
    setting_pos = x.find("=/")

    if setting_pos > 0:
        # check for option description comment on same line 
        description_pos = x.find("#")
        if description_pos > 0:
            input_str = x[:description_pos]
            print(x[description_pos:-1] + ":")
        else:
            input_str = x

        # option name
        option = input_str[:setting_pos + 1].strip()

        # prompt for setting to use
        use_setting = input(option + "[" + input_str[setting_pos + 2:-1].strip() + "] ? ")

        # use default if no setting value entered
        if len(use_setting) == 0:
            use_setting = input_str[setting_pos + 2:-1].strip()

        # display option and setting and write to output file
        print(option + use_setting + "\n")
        f_out.write(option + use_setting + "\n")

# not a settable option, just write line to output file
else:
    f_out.write(x)

f_in.close()
f_out.close()

# display output file for testing
#f = open(filename_out)
#print(f.read())
#f.close()
