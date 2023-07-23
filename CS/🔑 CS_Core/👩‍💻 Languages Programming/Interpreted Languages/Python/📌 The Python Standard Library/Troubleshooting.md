# Troubleshooting

[TOC]



## 👉 AttributeError: 'NoneType' object has no attribute 'text'
#python #xml 

ERROR:
```csharp
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-70-77e5e1b79ccc> in <module>()
     11 
     12 for child in root.iter('Materia'):
---> 13     if not child.find('EmentaMateria').text is None:
     14             ementa = child.find('EmentaMateria').text
     15 

AttributeError: 'NoneType' object has no attribute 'text'
```

---
Instead of checking if `child.find('EmentaMateria').text` is not `None`, you should make sure that `child.find('EmentaMateria')` is not `None` first.

Also, you should store the returning value of `child.find('EmentaMateria')` to avoid calling it twice.

Lastly, you should assign `ementa` a default value if `child.find('EmentaMateria')` is `None`; otherwise your `print` function below will be referencing an un-initialized variable.

Change:
```vhdl
if child.find('EmentaMateria').text is not None:
    ementa = child.find('EmentaMateria').text
```

to:
```python
node = child.find('EmentaMateria')
if node is not None:
    ementa = node.text
else:
    ementa = None
```

Alternatively, you can use the built-in function `getattr` to do the same without a temporary variable:
```python
ementa = getattr(child.find('EmentaMateria'), 'text', None)
```

[(Python) AttributeError: 'NoneType' object has no attribute 'text']: https://stackoverflow.com/questions/51664292/python-attributeerror-nonetype-object-has-no-attribute-text

