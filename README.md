# Directory Comparison Tool

DESCRIPTION
- This program is a simple tool that takes an input of the filepaths of two directories, recursively searches through them, and compares the files within to see if there are any differences between the files contained in each directory. It returns the files that are different between each directory and where those files are, or None if the directories contain the same files in the same places.
- NOTE: This program only checks the names of the files, not their actual contents to determine if the directories contain the same files.

USAGE
- This program is run through the command line with the line "python directory_comparison_tool.py &lt;filepath 1&gt; &lt;filepath 2&gt;" but has a reminder of proper usage if this line is not input properly.
- The filepath portions are to be filled with the full filepaths of the directories that the user would like to be compared.

PROGRAM STEPS
- Collect the information from the command line call
- Calls the directory_comparison() method with the information from the command line
  - This method is an outer method that handles the comparison of the lists returned by the inner method's traversal of the directories
- Calls the get_list_of_files() method for each directory
  - This method recursively searches through the directory using os.listdir(), populating a list of the files contained in that directory with their filepaths using os.path.join(), then returns the list of all the files within the directory
- Iterate through each of the returned lists, slicing off the filepath for each entry before the actual directory being compared
  - This ensures that the program is just comparing the contents of the directories in question, as including the extra filepath information would cause every file to be flagged as different (the directories could be in completely different places)
- Compare the two lists by converting them to sets, then using the set.difference() method twice to create two sets of the different files
- Print the lists of files that exist in one directory and not the other for both directories
  - Also print the tip that if both lists display "None", the directories contain the same files.
