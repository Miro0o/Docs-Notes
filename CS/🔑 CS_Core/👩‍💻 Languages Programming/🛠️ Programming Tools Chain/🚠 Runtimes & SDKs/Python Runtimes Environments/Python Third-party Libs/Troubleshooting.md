# Troubleshooting

[TOC]



## 👉 PIL.UnidentifiedImageError: cannot identify image file
#PIL 


**\#1 Image format unsupported**
skip.. (see ref)

---
**\#2 Target file unavailable**
This could be the file path error, or the file itself is not available. 

> **💡 In my case** I was running into this problem on Respray Pi. Turns out I was using two process to access the same file concurrently but Respray PI doesn't seem to support this. 😒 It means when i access it from one process the other process still holds it (with lock) and the lock is mutual exclusive, hence i cannot access it until the holder release the lock. 



[PIL.UnidentifiedImageError: cannot identify image file | Stackoverflow]: https://stackoverflow.com/questions/60168905/pil-unidentifiedimageerror-cannot-identify-image-file

[UnidentifiedImageError: cannot identify image file | Stackoverflow]: https://stackoverflow.com/questions/63754311/unidentifiedimageerror-cannot-identify-image-file

[UnidentifiedImageError: cannot identify image file `PNG` #5631 | Github]: https://github.com/python-pillow/Pillow/issues/5631

[UnidentifiedImageError when I try to train my model #4678 | Github]: https://github.com/python-pillow/Pillow/issues/4678

[Image.open() cannot identify image file - Python? | Stackoverflow]: https://stackoverflow.com/questions/19230991/image-open-cannot-identify-image-file-python



## 👉 UnicodeDecodeError: 'utf8' codec can't decode byte 0xa5 in position 0: invalid start byte
#utf8

The error is because there is some non-ascii character in the dictionary and it can't be encoded/decoded. One simple way to avoid this error is to encode such strings with `encode()`function as follows (if `a` is the string with non-ascii character):
```python
a.encode('utf-8').strip()
```
---

I switched this simply by defining a different codec package in the `read_csv()` command:
`encoding = 'unicode_escape'`

Eg:
```python
import pandas as pd
data = pd.read_csv(filename, encoding= 'unicode_escape')
```


[UnicodeDecodeError: 'utf8' codec can't decode byte 0xa5 in position 0: invalid start byte]: https://stackoverflow.com/questions/22216076/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-s
