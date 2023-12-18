# Troubleshooting

[TOC]



## 👉 Termshark's Color is Wrong!
#wireshark 

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
At first, the wrong color version of termshark is installed through homebrew. I searched the internet and on results. 🤷‍♀️
Then, using `go isntall xxxx` I downloaded the second version of termshark. (though probably the same version number).
Then still no changes. The color is wrong and some sections is invisible. (During which time I tried above suggestions by termshark FAQ Page ⏫)
After I re-wrote the config file at `~/Library/Application Support/termshark/termshark.toml` several times the go-installed termshark seems to override the original termshark's configuration file at `termshark.toml` and the new default file is placed as the starting report goes "file not found at `~/Library/Application Support/termshark/termshark.toml`". The two installations are using the same file I guess. 
Then everything goes back at square and the color problem goes off as well! 🤷‍♀️ 
Amazing.


[What settings affect termshark's colors?]: https://github.com/gcla/termshark/blob/master/docs/FAQ.md#what-settings-affect-termsharks-colors
[termshark 2.2.x not visible 😱 #114]: https://github.com/gcla/termshark/issues/114



## 👉 Termshark: `panic: runtime error: index out of range [70] with length 70`
#Termshark


> 🔗 [panic: runtime error: index out of range [70] with length 70 #151](https://github.com/gcla/termshark/issues/151)
> I filed an issue for this on Github: first issue in my life 🤳🏿

All info is in this issue ;)


[Go “panic: runtime error: index out of range” when the length of array is not null]: https://stackoverflow.com/questions/39118941/go-panic-runtime-error-index-out-of-range-when-the-length-of-array-is-not-nu

