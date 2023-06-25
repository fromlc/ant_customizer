# ant_customizer
Simple customizer for Netlab's Advanced Networking Tab options
- Developed with Python 3.11
- Uses template input file named 'advanced_networking_tab_template.txt'
  - The template file was provided by Instructor Bill Saichek to WASTC's Netlab Workshop participants in June 2023
  - Bill's original file has been slightly modified for use with this customizer
- Make sure the template input file and Python script exist in the same folder!
- Outputs all Networking Tab options in template file to new file named 'advanced_networking_tab.txt'
- File names are settable to whatever names you wish
- To make any option settable, change = to /= and (optionally) append a description comment to the option line
- For instance, change ```<option>=<setting>``` to ```<option>/=<setting>  # <description>```
- This generates the following description and prompt lines:
```
# <description>
<option>=[<setting>] ?
```
- Press the \<enter\> key to accept the option value in square brackets, or type a different value
