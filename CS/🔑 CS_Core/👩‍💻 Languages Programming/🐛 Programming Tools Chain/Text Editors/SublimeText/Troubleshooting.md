# Troubleshooting

[TOC]



## 👉 操作系统中的Python vs Sublime Text 2内嵌的[Python](https://sublime-text.readthedocs.io/en/latest/basic_concepts.html#python-vs-sublime-text-2python "Permalink to this headline")
在 **Windows** 以及 **Linux** 平台，Sublime Text的Python解释器是完全与系统的Python解释器分离的。
而在 **OS X** 平台上，Sublime Text使用的则是系统的Python解释器。这就导致对系统Python解释器版本所做的修改，可能会对Sublime Text造成影响。比如使用MacPorts提供的解释器替换系统默认的解释器，就可能造成一些问题。
这个内嵌的解释器只是为了与插件API作交互，并不应该用来进行通用Python应用的开发。



## 👉 [White line appears when in full-screen](https://gitlab.com/gnachman/iterm2/-/issues/9199)
Please try this build:
https://iterm2.com/adhocbuilds/iTerm2-3_4_20201227_121705-adhoc.zip

Turn on **Prefs > Advanced > Work around Big Sur bug where a white line flashes at the top of the screen in full screen mode** and then restart the app.



## 👉 Remap hotkey on `Neovintinge`
>  [How do I remap escape when in Sublime Text vintage mode?](https://stackoverflow.com/questions/9620812/how-do-i-remap-escape-when-in-sublime-text-vintage-mode) 

1. For [Vintageous](https://github.com/guillermooo/Vintageous) plugin, use [the following key binding](https://github.com/guillermooo/Vintageous/wiki/Using-jj-instead-of-Esc):
```js
{
    "keys": ["j", "k"],
    "command": "_enter_normal_mode",
    "args": {"mode": "mode_insert"},
    "context": [{"key": "vi_insert_mode_aware"}]
}
```

2. For  `Neovintageous` you can set these options in Sublime Text preferences to remap \<Esc\>:
``` shell
"vintageous_i_escape_jj": true

"vintageous_i_escape_jk": true
```


However neither works for me 🤷🏽‍♂️

#TODO 



## 👉 Cann't run turtle lib in python on ST
### 🙋‍♀️ issue description
i can't use sublime text to run turtle on python, because the default run-time env on ST of python is on `bash` , and the corresponding env is NOT activated.

#### 👌 workaround
👇 [==Add costumed build system==](https://blog.csdn.net/ShiAokai/article/details/83507924)
1. install ST & anaconda
2. install ST anaconda using pkg control in ST
3. modify configs of ST anaconda.
	1. default, system level (**python interpreter path**)
	2. user, individual level
	3. project, project level
4. [**new build system**](https://www.sublimetext.com/docs/build_systems.html)
	1. shell_cmd vs cmd
		1. shell_cmd & cmd designate the command pass on to shell. default shell here is `bash`  (idk 🤷 why it's not zsh or system default shell so that it is also zsh #unsolved  ). 
		2. here i use `"cmd": "python -u $file" ` for this setting. 
	
> **"cmd" : array of strings**
>- The executable to run, plus any arguments to pass to it. Shell constructs such as piping and redirection are not supported ---- see [shell_cmd](https://www.sublimetext.com/docs/build_systems.html#exec_option-shell_cmd) for related info.
>- May use [variables](https://www.sublimetext.com/docs/build_systems.html#variables).
>
>e.g.
> ``` shell
> "cmd": ["my_command", "-d", "$file"],
> ```


>**"shell_cmd" : string**
>- A shell command to execute. Unlike the [cmd](https://www.sublimetext.com/docs/build_systems.html#exec_option-cmd) option, this does allow piping and redirection. Will use `bash` on Mac and Linux machine, and `cmd.exe` on Windows.
>- May use [variables](https://www.sublimetext.com/docs/build_systems.html#variables).
> 
> e.g.
>```shell
>"shell_cmd": "my_command \"$file\" | other_command", 
>```

4.	
	2.  path: 
		1.  path is the working directory. if not explicited designated, working directory is found from `$PATH` (环境变量，一般指当前用户在系统上的用户环境变量).
		2.  here in order to be in anaconda base env, i manually assigned the path to the path of my base env directory `/User/Mir0/opt/anaconda/bin`
	3.  now everytime need to change run-time env of python, just change the `path` to the corresponding directory. 🎉
5.  remove the white box && troubleshooting
	1.  https://blog.csdn.net/qq_31347869/article/details/104724952


more on config-related docs, move [here](https://sublime-text-unofficial-documentation.readthedocs.io/en/latest/reference/build_systems/configuration.html)

```shell
// my anaconda config, named 'conda_base'.

// /Users/mir0/Library/Application Support/Sublime Text/Packages/User/conda_base.sublime-build

{
  	"cmd": ["python", "-u", "$file"],						// commands 	
  	"path":"/Users/mir0/opt/anaconda3/bin",					// path to interpretor env 
  	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",	// fetch error info form console
  	"selector": "source.python" 							// automatic selector identifier
}
```




## 👉 SublimeREPL Node: Error: connect ECONNREFUSED 

The error result in console is this:
```js
events.js:141
      throw er; // Unhandled 'error' event
      ^

Error: connect ECONNREFUSED 127.0.0.1:8000
    at Object.exports._errnoException (util.js:870:11)
    at exports._exceptionWithHostPort (util.js:893:20)
    at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1063:14)
```

The configuration is this: 
```js
// [path to Sublime Text]/Packages/SublimeREPL/config/NodeJS/repl.js

var rep = repl.start({
    //prompt:    null, //'> ',  
    prompt:    '> ', //'> ',  
    source:    null, //process.stdin,
    eval:      null, //require('vm').runInThisContext,
    useGlobal: true, //false
    useColors: false
});
```


The cause of error in source code is this:
```js
 // why this block??? with this block enabled i always got network error, it seems either node or sublimeREPL started a server on the background but it cannot reach the server from within this code block.
 
    var net = require('net');
    var ac_port = process.env.SUBLIMEREPL_AC_PORT;
    var client = new net.Socket();
    client.connect(ac_port, "localhost", function() {});

    client.on('data', function(data) {
        var strData = data.toString();
        var index = strData.indexOf(":");
        var json = strData.slice(index+1, strData.length - 1)
        var inData = JSON.parse(json);
        var wordIndex = inData.line.slice(inData.cursor_pos).search(/\b/);
        if(wordIndex !== 0){
            inData.line = inData.line.slice(0, inData.cursor_pos);
        }

        var send = function (_, completions) {
            var comps = completions[0];
            var msg = JSON.stringify([inData.line, comps]);
            var payload = msg.length + ":" + msg + ",";
            client.write(payload)
        }
        rep.rli.completer(inData.line, send);
    });
```

IDK what cause this and what this code is trying to do.




[node.js Error: connect ECONNREFUSED; response from server]: https://stackoverflow.com/questions/35199384/node-js-error-connect-econnrefused-response-from-server
[node.js simply not working, at all #364]: https://github.com/wuub/SublimeREPL/issues/364



## 👉 SublimeREPL FileNotFoundError(2, "No such file or directory: 'python'"

This is the error info: 
```shell
FileNotFoundError(2, "No such file or directory: 'python'")".
```

Reason:
Python within SublimeREPL cannot detect the conda by default, which means python from within default SublimeREPL is calling `python` from the system default envrionment (as shonw in `SublimeREPL/config/Python/repl.py`). The problem is there is no such thing called  `python` on default system settings, while the correct name for python is `python3`; so this means that you have to mannually change the calling name from `python` to `python3` in config file (`SublimeREPL/config/Python/repl.py`).



[FileNotFoundError(2, "No such file or directory: 'python'")".]: https://stackoverflow.com/questions/62945920/sublimerepl-filenotfounderror2-no-such-file-or-directory-python
["Anaconda can not spawn a new process..." I have sublime text error]: https://stackoverflow.com/questions/60673904/anaconda-can-not-spawn-a-new-process-i-have-sublime-text-error



## Ref

