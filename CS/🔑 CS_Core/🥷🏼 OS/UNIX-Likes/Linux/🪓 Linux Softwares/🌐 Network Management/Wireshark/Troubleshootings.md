# Troubleshootings

[TOC]



## 👉 Termshark's Color is Wrong!
### Possible Cause #1
If termshark's background is a strange color like dark blue or orange, maybe a tool like base16-shell has remapped some of the colors in the 256-color-space, but termshark is unaware of this. Try setting this in `termshark.toml`:
```toml
[main]
  ignore-base16-colors = true
```

### What Settings Affect Termshark's Colors?
1️⃣ First of all, your terminal emulator's `TERM` variable determines the range of colors available to termshark e.g. `xterm-16color`, `xterm-256color`.

2️⃣ If you also have `COLORTERM=truecolor` set, and the terminal emulator has support, 24-bit color will be available. Termshark will emit these 24-bit ANSI color codes and color should be faithfully reproduced.

🔗 More at:
[What settings Affect Termshark's Colors?]: https://github.com/gcla/termshark/blob/master/docs/FAQ.md#what-settings-affect-termsharks-colors

### My Solution
At first, the wrong color version of termshark is installed through homebrew. I searched internet and on results. 🤷‍♀️
Then, using `go isntall xxxx` i downloaded the second version of termshark. (though probably same version number).
Then still no changes. The color is wrong and some sections is invisible. (During which time i tried above suggestions by termshark FAQ Page ⏫)
After i re-wrote the config file at `~/Library/Application Support/termshark/termshark.toml` saveral times the go-installed termshark seems overrides the orignial termshark's configuration file at `termshark.toml` and the new default file is placed as the starting report goes "file not found at ~/Library/Application Support/termshark/termshark.toml". The two installation are using the same file i guess. 
Then everything goes back at square and the color problem goes off as well! 🤷‍♀️ 
Amazing.


[What settings affect termshark's colors?]: https://github.com/gcla/termshark/blob/master/docs/FAQ.md#what-settings-affect-termsharks-colors
[termshark 2.2.x not visible 😱 #114]: https://github.com/gcla/termshark/issues/114

