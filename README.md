# directory_comparison_tool

DESCRIPTION
- This program is a simple tool that takes an input of the filepaths of two directories, recursively searches through them, and compares the files within to see if there are any differences between the files contained in each directory. It returns the files that are different between each directory and where those files are, or None if the directories contain the same files in the same places.

USAGE
- This program is run through the command line with the line "python directory_comparison_tool.py &lt;filepath 1&gt; &lt;filepath 2&gt;" but has a reminder of proper usage if this line is not input properly.
- The filepath portions are to be filled with the filepaths of the directories that the user would like to be compared.

PROGRAM STEPS
- Collect the information from the command line call
- Calls the directory_comparison() method with the information from the command line
  - ###EXPLAIN WHAT THIS METHOD DOES (OUTER METHOD THAT HANDLES COMPARISON)
- Calls the get_list_of_files() method for each directory
  - This method recursively searches through the directory using os.listdir(), populating a list of the files contained in that directory with their filepaths using os.path.join(), then returns the list of all the files within the directory
- Iterate through each of the returned lists, slicing off the filepath for each entry before the actual directory being compared
  - This ensures that the program is just comparing the contents of the directories in question, as including the extra filepath information would cause every file to be flagged as different as the directories could be in completely differnt places
- Compare the two lists by converting them to sets, then using the set.difference() method twice to create two sets of the different files
- Print the ###TO BE CONTINUED


This project is a simple tool that takes an input of two directories and compares the files within to see which directory contains different files and returns the different files (or None if the files are all contained in the other directory).
