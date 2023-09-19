# FAQ

[TOC]



## 👉 How to Circumvent GFW 🇨🇳
📄 [how to circumvent GFW](https://support.torproject.org/censorship/connecting-from-china/)

To get an updated version of Tor Browser, try the Telegram bot first: [https://t.me/gettor_bot](https://t.me/gettor_bot). If that doesn't work, you can send an email to [gettor@torproject.org](mailto:gettor@torproject.org) with the subject "windows", "macos", or "linux" for the respective operating system.

After the installation, Tor Browser will try to connect to the Tor network. If Tor is blocked in your location, Connection Assist will try to automatically connect using a bridge or Snowflake. But if that doesn't work, the second step will be to obtain a bridge that works in China.

There are three options to unblock Tor in China:
1. **[Snowflake](https://support.torproject.org/censorship/what-is-snowflake/):** uses ephemeral proxies to connect to the Tor network. It's available in Tor Browser and other Tor powered apps like Orbot. You can select Snowflake from Tor Browser's [built-in bridge menu](https://support.torproject.org/censorship/how-can-i-use-snowflake/).
2. **Private and unlisted obfs4 bridges:** contact our Telegram Bot [@GetBridgesBot](https://t.me/GetBridgesBot) and type `/bridges`. Or send an email to [frontdesk@torproject.org](mailto:frontdesk@torproject.org) with the phrase "private bridge cn" in the subject of the email. If you are tech-savvy, you can run your own [obfs4 bridge](https://community.torproject.org/relay/setup/bridge/) from outside China. Remember that bridges distributed by [BridgeDB](https://bridges.torproject.org/), and built-in obfs4 bridges bundled in Tor Browser most likely won't work.
3. **meek-azure:** makes it look like you are browsing a Microsoft website instead of using Tor. However, because it has a bandwidth limitation, this option will be quite slow. You can select meek-azure from Tor Browser's built-in bridges dropdown.

If one of these options above is not working, check your [Tor logs](https://support.torproject.org/connecting/connecting-2/) and try another option.

If you need help, you can also get support on Telegram [https://t.me/TorProjectSupportBot](https://t.me/TorProjectSupportBot) and [Signal](https://signal.me/#p/+17787431312).
