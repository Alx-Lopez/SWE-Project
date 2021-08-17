# Dynamic Imports #

## Requirements ##
You need to two imports for this method to work:
`import os`
`import sys`

## The Solution ##
```python
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(currentdir)
sys.path.append((rootdir + "/NameOfProject"))
from <subfolderInProject> import <whateverFileYouNeed>
```

## Explanation of Components ##
So you need `import os` for getting the paths of things.
`os.path.realpath(__file__)` gives you the path to the current file you're in
`os.path.dirname()` gives the directory name of whatever is inside. since we have the previous line (the path to our file) inside, it gives us the directory that the file is in, or the **current directory**.  Essentially, calling this is like doing `cd ..` in linux, and takes you up one directory in the path.

In our solution specifically, you should note that you must append the name of the project folder to the root directory as `from common-services-be import ...` does not like the dashes in the directory name and will cause an error.