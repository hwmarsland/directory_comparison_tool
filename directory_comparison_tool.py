import sys
import os

def directory_comparison(dir1, dir2):
    list1 = get_list_of_files(dir1)
    list2 = get_list_of_files(dir2)

    for i in range(len(list1)):
        list1[i] = str(list1[i])[len(str(dir1)):]
    for i in range(len(list2)):
        list2[i] = str(list2[i])[len(str(dir2)):]

    diff1 = set(list1).difference(set(list2))
    if str(diff1) == 'set()':
        diff1 = 'None'

    diff2 = set(list2).difference(set(list1))
    if str(diff2) == 'set()':
        diff2 = 'None'

    print('Files that exist in folder 1 that don\'t exist in folder 2: ' + str(diff1))
    print('Files that exist in folder 2 that don\'t exist in folder 1: ' + str(diff2))
    print('If both are "None" then the folders contain the same files.')
    


def get_list_of_files(dir_name):
    list_of_file = os.listdir(dir_name)
    all_files = list()

    for i in list_of_file:
        full_path = os.path.join(dir_name, i)
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)
    
    return all_files


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('\nUsage: python directory_comparison_tool.py <filepath 1> <filepath 2>')
        print('Example Filepath: \'C:/Users/username/Desktop/folder_in_desktop\'\n')
    
    else:
        directory_comparison(sys.argv[1], sys.argv[2])