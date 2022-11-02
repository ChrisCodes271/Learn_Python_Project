#copyfile() = copies content of a file
#copy() = copyfile() + permission mode + destination can be directory
#copy2() = copy() + copies metadata (files creation and modification time)

import shutil

shutil.copyfile('test.txt','copy.txt') #two arguments. src,destination. Since src file is within program you don't need to qualify path.