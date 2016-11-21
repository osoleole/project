import os

def remove_new_str(in_filename, out_filename):
    '''Removes all \n from in_filename and writes back to
    out_filename'''
    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            for line in in_file:
                out_file.write(line.replace('\n',' '))

if __name__ == "__main__":
    remove_new_str('in_test.txt', 'out_test.txt')

