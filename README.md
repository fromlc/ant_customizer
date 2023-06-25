# ant_customizer
Simple customizer for Netlab's Advanced Networking Tab options
- Developed with Python 3.11
- Make sure the template file exists in the current folder
- Uses template input file named 'advanced_networking_tab_template.txt'
  - The template file was provided by Instructor Bill Saichek to WASTC's Netlab Workshop participants in June 2023
  - Bill's original file has been slightly modified for use with this customizer
- Outputs to file 'advanced_networking_tab.txt'
- To make any option settable, change = to /= and append a description comment to the option line
   - For instance, change \<option\>=\<setting\> to \<option\>/=\<setting\>  # description
