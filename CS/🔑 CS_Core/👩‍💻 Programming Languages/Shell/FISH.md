# [FISH](https://fishshell.com)

<img src="../../../../Assets/Pics/Terminal_Logo2_CRT_Flat.png" alt="Logo of Fish" style="zoom:50%;" />



fish is a smart and user-friendly command line shell for Linux, macOS, and the rest of the famil.

Some of the special features of fish are:

- **Extensive UI**: [Syntax highlighting](interactive.html#color), [Autosuggestions](interactive.html#autosuggestions), [tab completion](interactive.html#tab-completion) and selection lists that can be navigated and filtered.
- **No configuration needed**: fish is designed to be ready to use immediately, without requiring extensive configuration.
- **Easy scripting**: New [functions](language.html#syntax-function) can be added on the fly. The syntax is easy to learn and use.

## Where to go?

If this is your first time using fish, see the [tutorial](tutorial.html#tutorial).

If you are already familiar with other shells like bash and want to see the scripting differences, see [Fish For Bash Users](fish_for_bash_users.html#fish-for-bash-users).

For a comprehensive overview of fish’s scripting language, see [The Fish Language](language.html#language).

For information on using fish interactively, see [Interactive use](interactive.html#interactive).

## Configuration

To store configuration write it to a file called `~/.config/fish/config.fish`.

`.fish` scripts in `~/.config/fish/conf.d/` are also automatically executed before `config.fish`.

These files are read on the startup of every shell, whether interactive and/or if they’re login shells. Use `status --is-interactive` and `status --is-login` to do things only in interactive/login shells, respectively.

This is the short version; for a full explanation, like for sysadmins or integration for developers of other software, see [Configuration files](language.html#configuration).

## Resources

- The [GitHub page](https://github.com/fish-shell/fish-shell/)
- The official [Gitter channel](https://gitter.im/fish-shell/fish-shell)
- The official mailing list at [fish-users@lists.sourceforge.net](https://lists.sourceforge.net/lists/listinfo/fish-users)

If you have an improvement for fish, you can submit it via the GitHub page.

## Other help pages

- [Introduction](#)
- [Frequently asked questions](faq.html)
- [Interactive use](interactive.html)
- [The fish language](language.html)
- [Commands](commands.html)
- [Fish for bash users](fish_for_bash_users.html)
- [Tutorial](tutorial.html)
- [Writing your own completions](completions.html)
- [Design](design.html)
- [Release notes](relnotes.html)
- [License](license.html)