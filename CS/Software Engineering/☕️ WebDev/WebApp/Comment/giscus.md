# [giscus](https://giscus.app/)



:link: [Introducing giscus](https://laymonage.com/posts/giscus)

[TOC]



## Intro

<big>A [quick start](https://www.secrss.com/articles/10325) with giscus. 🚀</big>



<img src="../../../../../Assets/Pics/octocat.png" alt=":octocat:" style="zoom:40%;" /> 💬 💎

Giscus is **a comments system powered by [GitHub Discussions](https://docs.github.com/en/discussions)** . Let visitors leave comments and reactions on your website via GitHub! Heavily inspired by [utterances](https://github.com/utterance/utterances).

> utterances is based on GitHub issues system
>
> while giscus is based on GitHub Discussions system



- [Open source](https://github.com/giscus/giscus). 🌏
- No tracking, no ads, always free. 📡 🚫
- No database needed. All data is stored in GitHub Discussions. <img src="../../../../../Assets/Pics/octocat.png" alt=":octocat:" style="zoom:40%;" />
- Supports [custom themes](https://github.com/giscus/giscus/blob/main/ADVANCED-USAGE.md#data-theme)! 🌗
- Supports [multiple languages](https://github.com/giscus/giscus/blob/main/CONTRIBUTING.md#adding-localizations). 🌐
- [Extensively configurable](https://github.com/giscus/giscus/blob/main/ADVANCED-USAGE.md). 🔧
- Automatically fetches new comments and edits from GitHub. 🔃
- [Can be self-hosted](https://github.com/giscus/giscus/blob/main/SELF-HOSTING.md)! 🤳

> Note giscus is still under active development. GitHub is also still actively developing Discussions and its API. Thus, some features of giscus may break or change over time.



## How it works

When giscus loads, the [GitHub Discussions search API](https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-discussions#search) is used to find the Discussion associated with the page based on a chosen mapping (URL, `pathname`, `<title>`, etc.). If a matching discussion cannot be found, the giscus bot will automatically create a discussion the first time someone leaves a comment or reaction.

To comment, visitors must authorize the [giscus app](https://github.com/apps/giscus) to [post on their behalf](https://docs.github.com/en/developers/apps/identifying-and-authorizing-users-for-github-apps) using the GitHub OAuth flow. Alternatively, visitors can comment on the GitHub Discussion directly. You can moderate the comments on GitHub.

If you're using giscus, consider [starring 🌟 giscus on GitHub](https://github.com/giscus/giscus) and adding the [`giscus`](https://github.com/topics/giscus) topic [to your repository](https://docs.github.com/en/github/administering-a-repository/classifying-your-repository-with-topics)! 🎉



## Advanced usage

You can add additional configurations (e.g. allowing specific origins) by following the [advanced usage guide](https://github.com/giscus/giscus/blob/main/ADVANCED-USAGE.md).

To use giscus with React, Vue, or Svelte, check out the [giscus component library](https://github.com/giscus/giscus-component).



## Migrating

If you've previously used other systems that utilize GitHub Issues (e.g. [utterances](https://github.com/utterance/utterances), [gitalk](https://github.com/gitalk/gitalk)), you can [convert the existing issues into discussions](https://docs.github.com/en/discussions/managing-discussions-for-your-community/moderating-discussions#converting-an-issue-to-a-discussion). After the conversion, just make sure that the mapping between the discussion titles and the pages are correct, then giscus will automatically use the discussions.