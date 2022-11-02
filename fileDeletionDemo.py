import os
import shutil

path = 'test.txt'
folder_path = 'test_folder'
stuffed_folder = 'stuffed_folder'

try:
    os.remove(path)
    #os.remove(folder_path) this won't remove dir's
    os.rmdir(folder_path) #to remove directories you have to use this one
    #os.rmdir(stuffed_folder) this won't remove directories  with things in them. For that you need to import shutil
    shutil.rmtree(stuffed_folder) #This will delete a directory and all files within. !!USE WITH CAUTION!!

except FileNotFoundError as e:
    print('{} was not found'.format(path))
    print(e)

except PermissionError as e:
    print('You do not have permission to remove {}'.format(folder_path))
    print(e)

except OSError as e:
    print(e)

else:
    print('{},{}, and {} were deleted successfully'.format(path, folder_path, stuffed_folder))
