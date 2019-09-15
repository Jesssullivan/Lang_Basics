Collecting snippets-



# PPTX_2_PDF:
bulk convert PowerPoint PPTX to PDF 

**Install LibreOffice tools for CLI**
https://www.libreoffice.org/get-help/install-howto/

**Make the shell script:**
```
nano PPTX2PDF.sh
```
```
#!/bin/bash

# contents of PPTX2PDF.sh:

for f in *.pptx;
do
        echo "Converting $f file to PDF..."
        /Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf:writer_pdf_Export "$f"
done
```

**permissions:**
```
chmod u+x PPTX2PDF.sh
```

**run somewhere...**
```
./PPTX2PDF.sh
```

*For those unfamilar with terminal but need to make some PDFs:*
use ```cd``` and ```cd - ``` to navigate to and from directories ("Change Directory", folders in your computer).  For example:
if the PowerPoints are in a folder "PPTX" in my Documents folder, I would get there in terminal with ```cd Documents/PPTX```.
To see what is in the directory, use the command ```ls```.   Then, run the new command```./PPTX2PDF.sh``` to convert the files to PDF.   (This is assuming the LibreOffice tools are in the default macos location)
