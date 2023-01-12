# TShark

[TOC]



A terminal user-interface for tshark, inspired by Wireshark.

## Documentation

See the [termshark user guide](https://github.com/gcla/termshark/blob/master/docs/UserGuide.md), and my best guess at some [FAQs](https://github.com/gcla/termshark/blob/master/docs/FAQ.md). For a summary of updates, see the [ChangeLog](https://github.com/gcla/termshark/blob/master/CHANGELOG.md#changelog).



## Dependencies

Termshark depends on these open-source packages:

- [tshark](https://www.wireshark.org/docs/man-pages/tshark.html) - command-line network protocol analyzer, part of [Wireshark](https://wireshark.org/)
- [tcell](https://github.com/gdamore/tcell) - a cell based terminal handling package, inspired by termbox
- [gowid](https://github.com/gcla/gowid) - compositional terminal UI widgets, inspired by [urwid](http://urwid.org/), built on [tcell](https://github.com/gdamore/tcell)

Note that tshark is a run-time dependency, and must be in your `PATH` for termshark to function. Version 1.10.2 or higher is required (approx 2013).

