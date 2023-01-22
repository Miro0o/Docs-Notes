# Encoding

[TOC]



## Res

【【CTF全套120集】清华大学顶尖蓝莲花战队站教你学CTF从零基础内卷成大佬！| ctf入门| ctf比赛| ctf夺旗赛|ctfweb】 https://www.bilibili.com/video/BV1DL4y1T7v7/?p=8&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



## Intro

Encoding, in an universal explanation. is the mapping between two sets. 

In CS, encoding in general map a set of character to a set of value/character. 

In fact, the classic cryptographic methods are all based on encoding methods. ↗️ [Classic Cryptography](Classic Cryptography/Classic Cryptography.md).



### Encoding :vs: Encryption & Cryptography :vs: Hashing

> :link: https://www.geeksforgeeks.org/encryption-encoding-hashing/

#### Encoding

In the Encoding method, data is transformed from one form to another. The main aim of encoding is to transform data into a form that is readable by most of the systems or that can be used by any external process.
It can’t be used for securing data, various publicly available algorithms are used for encoding.

Encoding can be used for **reducing the size** of audio and video files. Each audio and video file format has a corresponding coder-decoder (codec) program that is used to code it into the appropriate format and then decodes for playback.

#### Encryption 

Encryption in encoding technique in which message is encoded by using encryption algorithm in such a way that only authorized personnel can access the message or information.

It is a special type of encoding that is used for transferring private data, for example sending a combination of username and password over the internet for email login.

In encryption, data to be encrypted(called plain-text) is transformed using an encryption algorithm like AES encryption or RSA encryption using a secret key called cipher. The encrypted data is called cipher-text, and finally, the secret key can be used by the intended recipient to convert it back to plain-text.

There are two types of encryption algorithms – symmetric and asymmetric encryption.
In case of symmetric encryption data is encoded and decoded with the help of same key, for example AES encryption algorithm but in case of asymmetric encryption algorithm, data is encrypted with help of two keys, namely public and private key, for example. [RSA algorithm](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/).

![img](../../../../Assets/Pics/Encryption_vs_Encoding_vs_Hashing_1.png)

#### Hashing

In hashing, data is converted to the hash using some hashing function, which can be any number generated from string or text. Various hashing algorithms are MD5, SHA256. Data once hashed is non-reversible.

Hash function can be any function that is used to map data of arbitrary size to data of fixed size. The data structure [hash table](https://www.geeksforgeeks.org/hashing-data-structure/) is used for storing of data.

For example: When you send pictures and text messages over WhatsApp over StackOverflow(posting in questions), images are sent to different server and text is sent to a different server for efficiency purposes. So for verifying images that the images are not tampered in between data transfer over the internet, hashing algorithm like MD5 can be used.

![img](../../../../Assets/Pics/Encryption_vs_Encoding_vs_Hashing_2.png)



## Encoding Schemes

The number of characters encoded has a direct relationship to the length of each representation which typically is measured as the number of bytes. **Having more characters to encode essentially means needing lengthier binary representations.**



### Single-Byte Encoding



### Multi-Byte Encoding



## 🔠 Charset & Character Encoding development

A charset is a set of characters.  Usually a new charset comes along with a new encoding mechanism.



> :link: http://en.wikipedia.org/wiki/Character_encoding
>
> Character encoding is the process of assigning numbers to graphical characters, especially the written characters of human language, allowing them to be stored, transmitted, and transformed using digital computers. The numerical values that make up a character encoding are known as "code points" and collectively comprise a "code space", a "code page", or a "character map".

Character encoding or just simply encoding in CS refers to the mapping processing /mechanism from a charset to numerical values, which is to be used in digital devices (computer) for communication /storages / etc.. 

A **"code point**" is an integer reference to a particular character.

### [ASCII](https://www.ascii-code.com)

**ASCII**, stands for American Standard Code for Information Interchange. It's a **7-bit character code** where every single bit represents a unique character. 

Besides ASCII code, there are various extended ASCII which use 8-bit cahracter encoding. 

**Windows-1252** is probably the most-used 8-bit character encoding in the world. 

On [this webpage](https://www.ascii-code.com) you will find 8 bits, 256 characters, **ASCII table according to Windows-1252** (code page 1252) which is a superset of ISO 8859-1 in terms of printable characters. In the range 128 to 159 (hex 80 to 9F), ISO/IEC 8859-1 has invisible control characters, while Windows-1252 has writable characters. 

Find other extended ASCII codes on ↗️ https://www.ascii-code.com



### Extended ASCII

#### EASCII





#### ANSI (or formally, Windows-1252)

> :link: https://stackoverflow.com/questions/701882/what-is-ansi-format

ANSI encoding is a slightly generic term used to refer to the standard code page on a system, usually Windows. It is more properly referred to as [Windows-1252](http://en.wikipedia.org/wiki/Windows-1252) on Western/U.S. systems. (It can represent certain other [Windows code pages](http://en.wikipedia.org/wiki/Windows_code_page) on other systems.) This is essentially an [extension of the ASCII character set](http://en.wikipedia.org/wiki/Extended_ASCII) in that **it includes all the ASCII characters with an additional 128 character codes**. This difference is due to the fact that "ANSI" encoding is 8-bit rather than 7-bit as ASCII is (ASCII is almost always encoded nowadays as 8-bit bytes with the [MSB](https://en.wikipedia.org/wiki/Most_significant_bit) set to 0). See the article for an explanation of why this encoding is usually referred to as ANSI.

The name "ANSI" is a misnomer, since it doesn't correspond to any actual ANSI standard, but the name has stuck. ANSI is not the same as UTF-8.



### GBxxx

#### GB2312-1980

计算机发明之处及后面很长一段时间，只用应用于美国及西方一些发达国家，ASCII能够很好满足用户的需求。但是当天朝也有了计算机之后，为了显示中文，必须设计一套编码规则用于将汉字转换为计算机可以接受的数字系统的数。

天朝专家把那些127号之后的奇异符号们（即EASCII）取消掉，规定：一个小于127的字符的意义与原来相同，但两个大于127的字符连在一起时，就表示一个汉字，前面的一个字节（高字节）从0xA1用到 0xF7，后面一个字节（低字节）从0xA1到0xFE，这样我们就可以组合出大约7000多个简体汉字了。在这些编码里，还把数学符号、罗马希腊的 字母、日文的假名们都编进去了，连在ASCII里本来就有的数字、标点、字母都统统重新编了**两个字节长的编码**，这就是常说的"全角"字符，而原来在127号以下的那些就叫"半角"字符了。

![img](../../../../Assets/Pics/201105031137227086.png)

<small>GB2312编码表的开始部分</small>



#### GBK

由于GB 2312-80只收录6763个汉字，有不少汉字，如部分在GB 2312-80推出以后才简化的汉字（如"啰"），部分人名用字（如中国前总理朱镕基的"镕"字），台湾及香港使用的繁体字，日语及朝鲜语汉字等，并未有收录在内。于是厂商微软利用GB 2312-80未使用的编码空间，收录GB 13000.1-93全部字符制定了GBK编码。根据微软资料，GBK是对GB2312-80的扩展，也就是CP936字码表 (Code Page 936)的扩展（之前CP936和GB 2312-80一模一样），最早实现于Windows 95简体中文版。虽然GBK收录GB 13000.1-93的全部字符，但编码方式并不相同。GBK自身并非国家标准，只是曾由国家技术监督局标准化司、电子工业部科技与质量监督司公布为"技术规范指导性文件"。原始GB13000一直未被业界采用，后续国家标准GB18030技术上兼容GBK而非GB13000。

#### GB 18030

GB 18030，全称：国家标准GB 18030-2005《信息技术 中文编码字符集》，是中华人民共和国现时最新的内码字集，是GB 18030-2000《信息技术 信息交换用汉字编码字符集 基本集的扩充》的修订版。与GB 2312-1980完全兼容，与GBK基本兼容，支持GB 13000及Unicode的全部统一汉字，共收录汉字70244个。GB 18030主要有以下特点： 

- 与UTF-8相同，采用多字节编码，**每个字可以由1个、2个或4个字节组成**。 
- 编码空间庞大，最多可定义161万个字符。
- 支持中国国内少数民族的文字，不需要动用造字区。
- 汉字收录范围包含繁体汉字以及日韩汉字。

![img](../../../../Assets/Pics/201105031137222069.jpg)

<small>GB18030编码总体结构</small>

本规格的初版使中华人民共和国信息产业部电子工业标准化研究所起草，由国家质量技术监督局于2000年3月17日发布。现行版本为国家质量监督检验总局和中国国家标准化管理委员会于2005年11月8日发布，2006年5月1日实施。此规格为在中国境内所有软件产品支持的强制规格。



### BIG5

Big5，又称为大五码或五大码，是使用繁体中文（正体中文）社区中最常用的电脑汉字字符集标准，共收录13,060个汉字。中文码分为内码及交换码两类，Big5属中文内码，知名的中文交换码有CCCII、CNS11643。Big5虽普及于台湾、香港与澳门等繁体中文通行区，但长期以来并非当地的国家标准，而只是业界标准。倚天中文系统、Windows等主要系统的字符集都是以Big5为基准，但厂商又各自增加不同的造字与造字区，派生成多种不同版本。2003年，Big5被收录到CNS11643中文标准交换码的附录当中，取得了较正式的地位。这个最新版本被称为Big5-2003。 

**Big5码是一套双字节字符集，使用了双八码存储方法，以两个字节来安放一个字。**第一个字节称为"高位字节"，第二个字节称为"低位字节"。"高位字节"使用了0x81-0xFE，"低位字节"使用了0x40-0x7E，及0xA1-0xFE。在Big5的分区中：



### Unicode

[Unicode](https://home.unicode.org) is a character set. It defines that a character can be represented by 1, 2, 4bytes. While another different character set, ASCII, defines that a character represented by 1 bytes, and GB2312 defines that a character represented by 2 bytes. 

Unicode is now the universal standard for encoding all human languages. And yes, it even includes [emojis](https://unicode.org/emoji/charts/full-emoji-list.html) 😅🤣🤺👋🏻🙏🏿💃🏻🙉🎳🏂🍑🇦🇷



> **About the Unicode Consortium**
>
> The Unicode Consortium is the standards body for the internationalization of software and services.
>
> - Founded in 1988, incorporated in 1991
> - Public benefit, 501(c)3 non-profit organization
> - Open source standards, data, and software development
> - Orchestrates the contributions of 100s of professionals, expert volunteers, and language experts
> - 30+ [organizational members](https://home.unicode.org/membership/members/) across corporate, academic, and governmental institutions
> - Funded by [membership dues](https://home.unicode.org/membership/membership-levels/) and [donations](https://home.unicode.org/support-unicode/)
>
> 
>
> :link: more on https://home.unicode.org/about-unicode/



| Unicode Character | code point |
| ----------------- | ---------- |
| A                 | U+0041     |
| a                 | U+0061     |
| 0                 | U+0030     |
| 9                 | U+0039     |
| !                 | U+0021     |
| Ø                 | U+00D8     |
| ڃ                 | U+0683     |
| ಚ                 | U+0C9A     |
| 𠜎                | U+2070E    |
| 😁                 | U+1F601    |



Unicode 使用4字节的数字来表达每个字母、符号，或者表意文字(ideograph)。每个数字代表唯一的至少在某种语言中使用的符号。（并不是所有的数字都用上了，但是总数已经超过了65535，所以2个字节的数字是不够用的。）被几种语言共用的字符通常使用相同的数字来编码，除非存在一个在理的语源学(etymological)理由使不这样做。不考虑这种情况的话，每个字符对应一个数字，每个数字对应一个字符。即不存在二义性。不再需要记录"模式"了。U+0041总是代表'A'，即使这种语言没有'A'这个字符。

Unicode是一套字符集，在其之下有不同的编码方案。UTF-32/ UTF-16/ UTF-8是其中三种字符编码方案。

#### UTF-8

> :link: https://blog.hubspot.com/website/what-is-utf-8

UTF-8 stands for 8-bit Unicode Transformation Format. It is **another encoding scheme for Unicode which employs a variable length of bytes to encode**. While it uses a single byte to encode characters generally, it can use a higher number of bytes if needed, thus saving space. Remember that one byte consists of eight bits, hence the “-8” in its name.

More specifically, UTF-8 converts a code point (which represents a single character in Unicode) into a set of one to four bytes. The first 128 characters in the Unicode library — the characters we saw in ASCII — are represented as one byte. Characters that appear later in the Unicode library are encoded as two-byte, three-byte, and eventually four-byte binary units.



| UNICODE CHARACTER | CODE POINT | UTF-8 BINARY ENCODING               |
| ----------------- | ---------- | ----------------------------------- |
| A                 | U+0041     | 01000001                            |
| a                 | U+0061     | 01100001                            |
| 0                 | U+0030     | 00110000                            |
| 9                 | U+0039     | 00111001                            |
| !                 | U+0021     | 00100001                            |
| Ø                 | U+00D8     | 11000011 10011000                   |
| ڃ                 | U+0683     | 11011010 10000011                   |
| ಚ                 | U+0C9A     | 11100000 10110010 10011010          |
| 𠜎                | U+2070E    | 11110000 10100000 10011100 10001110 |
| 😁                 | U+1F601    | 11110000 10011111 10011000 10000001 |



#### UTF-16

TODO

#### UTF-32

TODO





[Guide to Character Encoding]: https://www.baeldung.com/java-char-encoding
[字符集和字符编码]: https://www.cnblogs.com/notbecoder/p/4840783.html
[字符集和字符编码（Charset & Encoding）]: https://www.runoob.com/w3cnote/charset-encoding.html



## 🪄 Encodings in cryptography

### Base64



### Base32



### URL encoding



### JS obfuscation

↗️  [JS Obfuscation](../../../Software Engineering/🖥️ FrontEndDev/⬆️ FrontendOptimization/JS Obfuscation.md)



#### JSfuck



#### Jother



#### aaencode





### 📚 More encoding methods in cryptography

More of this part is included in ↗️ [CTF/Crypto](../../👻 CTF/Misc/Crypto/Crypto.md).





## Other encodings

TODO



## Ref