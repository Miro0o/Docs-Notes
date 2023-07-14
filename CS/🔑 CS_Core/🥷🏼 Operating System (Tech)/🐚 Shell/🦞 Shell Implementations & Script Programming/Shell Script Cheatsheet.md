# Shell Script Cheatsheet

[TOC]


## File & Text & Dir
### 👉 Replace whitespace with underscore in all filenames
**Replace whitespace from all filenames under current folder**
```bash
#!/bin/bash
ls | while read -r FILE; do
  mv -v "$FILE" `echo $FILE | tr ' ' '_'`
done
```

**Replace whitespace from all filenames under all sub-folders**
```bash
while IFS='' read -r -d '' fname ; do
   nname="${fname##*/}"
   mv -v -n "${fname}"  "${fname%/*}/${nname//[[:space:]]/_}"
done < <(find "$(pwd)"  -name "* *" -type f  -print0)
```

- `find "$(pwd)" -type f -print0` - Prints all the found file paths in current dir and subdirs. With the process substitution output of find command is sent to while loop where it reads variable fname.
- `nname="${fname##*/}"` - Extracts file name from path
- `"${fname%/*}"` - extracts the path
- `"${nname//[[:space:]]/"_"}"` - replaces spaces in the filename with `_`
- `"${fname%/*}/${nname//[[:space:]]/"_"}"` - path/new_filename


[How to replace whitespace with underscore in all filenames?]: https://superuser.com/questions/1323011/how-to-replace-whitespace-with-underscore-in-all-filenames


### 👉 Move a list of files(in a text file) to a directory?
You need to tell your loop to _read_ the file, otherwise it is just executing:
```bash
mv ~/Desktop/files.txt ~/newfolder
```

In addition, as nerdwaller said, you need separators. Try this:
```bash
while read file; do mv "$file" ~/newfolder; done < ~/Desktop/files.txt
```

If your paths or file names contain spaces or other strange characters, you may need to do this:
```bash
while IFS= read -r file; do mv "$file" ~/newfolder; done < ~/Desktop/files.txt
```

Notice the quotes `"` around the `$file` variable.


[Move a list of files(in a text file) to a directory?]: https://superuser.com/questions/538306/move-a-list-of-filesin-a-text-file-to-a-directory