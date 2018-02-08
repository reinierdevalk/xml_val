# `xmval`

## What is xmval?

`xmval` is a Python script for batch validating XML files that is executed from the command line. It is written for Mac OS X and makes use of [`xmllint`](http://xmlsoft.org/xmllint.html). The script must be stored in the _~/bin_ directory. For this script to run, Python (preferably v3.5 or higher) must be installed on your computer. To check which version of Python you have installed, open the terminal and enter the following command: 
 
    $ python -V

If this returns an error, you must first install Python in order to be able to proceed.


## How to use xmval

`xmval` takes one mandatory (M) argument and two optional (O) arguments:
* `<schema_path>.xsd` (M) - the path to the XML schema to validate against
* `<folder_path>` (O) -	the path to the folder containing the XML files to validate. NB: if this folder contains subfolders, any XML files in them will be validated as well.	
* `<subfolder>` (O):	a subfolder constraint: only subpaths of `<folder_path>` containing this subfolder are checked.

The three arguments must be given in this order, and none of them may be omitted. Optional arguments that do not apply must be represented by an empty string ('').

Both `<schema_path>.xsd` and `<folder_path>` must be full paths--although the tilde (`~`) may be used to represent your home directory. `<subfolder>` must be the name of a single folder.

Once these paths and the subfolder are known, there are two ways to validate XML files.  

**1. Validation from inside the folder where the XML files are stored.** This is done by first changing directory into `<folder_path>`, and then invoking the script:

    $ cd <folder_path>
    $ xmval.py <schema-path> '' ''

or, if the subfolder constraint is used:
    
    $ cd <folder_path>
    $ xmval.py <schema-path> '' <subfolder> 
    
Note that in both cases, the first optional parameter need not be supplied.

**2. Validation from anywhere on your computer.** In this case, no directory change needs to be specified (this is handled internally), but `<folder_path>` must be explicitly supplied as a parameter:

    $ xmval.py <schema-path> <folder_name> ''
    
or, if the subfolder constraint is used:

    $ xmval.py <schema-path> <folder_name> <subfolder>

## Output

The validator output is stored as a text file in `<folder_path>`. It contains, in addition to path, folder, and file information, for each XML file a statement whether or not that file is valid.
