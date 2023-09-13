# FAQ

[TOC]



## 👉 Difference between API and ABI
#API #ABI

My understanding: (?🤷‍♀️)
The concepts of API/ABI is dynamic and relative. When referring to API, it means the interface the system as a whole provided to the outside; while for ABI, it means the interfaces provided among system's components for intra-communicating purposes.

---

**API: Application Program Interface**
This is the set of public types/variables/functions that you expose from your application/library.

In C/C++ this is what you expose in the header files that you ship with the application.


**ABI: Application Binary Interface**
This is how the compiler builds an application.  
It defines things (but is not limited to):
- How parameters are passed to functions (registers/stack).
- Who cleans parameters from the stack (caller/callee).
- Where the return value is placed for return.
- How exceptions propagate.

[👍 Difference between API and ABI | Stackoverflow]: https://stackoverflow.com/a/3784697/16542494

---

**Linux shared library minimal runnable API vs ABI example**

This answer has been extracted from my other answer: [What is an application binary interface (ABI)?](https://stackoverflow.com/questions/2171177/what-is-an-application-binary-interface-abi/54967743#54967743) but I felt that it directly answers this one as well, and that the questions are not duplicates.

In the context of shared libraries, the most important implication of "having a stable ABI" is that you don't need to recompile your programs after the library changes.

As we will see in the example below, it is possible to modify the ABI, breaking programs, even though the API is unchanged.

main.c
```c
#include <assert.h>
#include <stdlib.h>

#include "mylib.h"

int main(void) {
    mylib_mystruct *myobject = mylib_init(1);
    assert(myobject->old_field == 1);
    free(myobject);
    return EXIT_SUCCESS;
}
```

mylib.c
```c
#include <stdlib.h>

#include "mylib.h"

mylib_mystruct* mylib_init(int old_field) {
    mylib_mystruct *myobject;
    myobject = malloc(sizeof(mylib_mystruct));
    myobject->old_field = old_field;
    return myobject;
}
```

mylib.h
```c
#ifndef MYLIB_H
#define MYLIB_H

typedef struct {
    int old_field;
} mylib_mystruct;

mylib_mystruct* mylib_init(int old_field);

#endif
```

Compiles and runs fine with:
```c
cc='gcc -pedantic-errors -std=c89 -Wall -Wextra'
$cc -fPIC -c -o mylib.o mylib.c
$cc -L . -shared -o libmylib.so mylib.o
$cc -L . -o main.out main.c -lmylib
LD_LIBRARY_PATH=. ./main.out
```

Now, suppose that for v2 of the library, we want to add a new field to `mylib_mystruct` called `new_field`.

If we added the field before `old_field` as in:
```c
typedef struct {
    int new_field;
    int old_field;
} mylib_mystruct;
```

and rebuilt the library but not `main.out`, then the assert fails!

This is because the line:
``` c
myobject->old_field == 1
```

had generated assembly that is trying to access the very first `int` of the struct, which is now `new_field` instead of the expected `old_field`.

Therefore this change broke the ABI.

If, however, we add `new_field` after `old_field`:
``` c
typedef struct {
    int old_field;
    int new_field;
} mylib_mystruct;
```

then the old generated assembly still accesses the first `int` of the struct, and the program still works, because we kept the ABI stable.

Here is a [fully automated version of this example on GitHub](https://github.com/cirosantilli/cpp-cheat/tree/449024d6bedc8ff1d9d5a832efaf8f0851fb260c/shared_library/abi).

Another way to keep this ABI stable would have been to treat `mylib_mystruct` as an [opaque struct](https://en.wikipedia.org/wiki/Opaque_pointer), and only access its fields through method helpers. This makes it easier to keep the ABI stable, but would incur a performance overhead as we'd do more function calls.

**API vs ABI**
In the previous example, it is interesting to note that adding the `new_field` before `old_field`, only broke the ABI, but not the API.

What this means, is that if we had recompiled our `main.c` program against the library, it would have worked regardless.

We would also have broken the API however if we had changed for example the function signature:
```c
mylib_mystruct* mylib_init(int old_field, int new_field);
```

since in that case, `main.c` would stop compiling altogether.

**Semantic API vs Programming API**
We can also classify API changes in a third type: semantic changes.

The semantic API, is usually a natural language description of what the API is supposed to do, usually included in the API documentation.

It is therefore possible to break the semantic API without breaking the program build itself.

For example, if we had modified
```c
myobject->old_field = old_field;
```

to:
```c
myobject->old_field = old_field + 1;
```

then this would have broken neither programming API, nor ABI, but `main.c` the semantic API would break.

There are two ways to programmatically check the contract API:
- test a bunch of corner cases. Easy to do, but you might always miss one.
- [formal verification](https://en.wikipedia.org/wiki/Formal_verification). Harder to do, but produces mathematical proof of correctness, essentially unifying documentation and tests into a "human" / machine verifiable manner! As long as there isn't a bug in your formal description of course ;-)

Tested in Ubuntu 18.10, GCC 8.2.0.


[👍 Difference between API and ABI | Stackoverflow]: https://stackoverflow.com/a/54970475/16542494

