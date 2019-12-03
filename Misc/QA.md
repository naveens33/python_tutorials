# Interview Questions
1. What is os module?
    * It is a miscellaneous operating system interfaces module
    * Provides a portable way of using operating system dependent functionality

2. Some common function in os module
    * **Manipulating directories:**
        * chdir()
        * getcwd()
        * listdir()
        * mkdir()
        * makedirs()
        * rmdir()
        * removedirs()
    * **Removing a file:**
        * remove()
        * Renaming files/directories:
        * rename()
    * **Using more than one process:**
        * system()
        * popen()
        * close()
        * walk()
    * **User id and process id:**
        * getgid(), os.getuid(), os.getpid()
    * **More about directories and files:**
        * error
        * stat()
    * **Cross-plateform os attributes:**
        * name
    * **Accessing environment variables:**
        * environ

3. How to get the value of environment variables
    * using os.environ.get('TEMP')function

4. Difference between os.makedirs() and os.mkdir()
    * makedirs() creates all the intermediate directories if they don’t exist already
    * mkdir() can create a single sub-directory and it will throw an exception if intermediate directories that don’t exist are specified.
    * Note: removedirs() and rmdir() also works the same way i.e. os.rmdir() will not remove the intermediate directory where as os.removedirs() will remove the intermediate directories