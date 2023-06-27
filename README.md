# ant_customizer
Simple customizer for Netlab's Advanced Networking Tab options
- Developed with Python 3.11
- Uses template input file named 'advanced_networking_tab_template.txt'
  - The template file was provided by Instructor Bill Saichek to WASTC's Netlab Workshop participants in June 2023
  - Bill's original file has been slightly modified for use with this customizer
- Make sure the template input file and Python script file exist in the same folder!
- Outputs all Networking Tab option lines in the template file to a new file named 'advanced_networking_tab.txt'
- These file names are settable to whatever names you wish
- Edit any option line in the template file to make the option settable
  - Change ```<option>=<setting>``` to ```<option>/=<setting>  # <description>```
  - The ```# <description>``` comment is optional
- For instance, changing
```vswitch.0.ports=12``` to ```vswitch.0.ports=/12  # TOTAL number of NICs on all VMs, plus 1``` generates this description and prompt:
```
# TOTAL number of NICs on all VMs, plus 1
vswitch.0.ports=[12] ?
```
- Press the \<enter\> key to accept the option value in square brackets, or type a different value
