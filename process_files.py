import os

def replace_string_in_filename(file_extension, old_string, new_string):
    for f in os.listdir('.'):
        if f.endswith(file_extension):
            new_filename = f.replace(old_string, new_string)
            os.rename(f, new_filename)


def append_string_to_filename(ext, new_string):
    for f in os.listdir('.'):
        if f.endswith(ext):
            new_name = f[:-4]
            os.rename(f, new_name + new_string)

def main():
    replace_string_in_filename('.csv', 'output', '_test_data_')

if __name__ == '__main__':
    main()
