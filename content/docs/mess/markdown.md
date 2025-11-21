---
lastmod: 2025-09-17T13:00:00Z
publishDate: 2025-09-12T10:00:00Z
title: Markdown
tags: []
---

## Markdown的开始

Markdown 最初是 John Gruber 在 2004 年设计的，这里是他的[官方文档](https://daringfireball.net/projects/markdown/syntax)

它的设计目标很简单：

* 可读性第一（纯文本就应该好看）

* 写作优先，不追求复杂功能

## Markdown的规范问题

因为最初的 Markdown 没有正式规范，各个平台都各自扩展，造成“方言”问题。  
于是 2014 年一群开发者联合起来，制定了 CommonMark —— 它是 Markdown 的“正式标准”。[commonmark](https://commonmark.org/)

## Markdown语法

### 基本语法

#### 标题

| Type               | Get                |
| ------------------ | ------------------ |
| `# Heading 1`      | <h1>Heading 1</h1> |
| `## Heading 2`     | <h2>Heading 2</h2> |
| `### Heading 3`    | <h3>Heading 3</h3> |
| `#### Heading 4`   | <h4>Heading 1</h4> |
| `##### Heading 5`  | <h5>Heading 2</h5> |
| `###### Heading 6` | <h6>Heading 3</h6> |

#### 段落

| Type                                                                                                           | Get                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| <p>`I really like using Markdown.`</p> <p>`I think I'll use it to format all of my documents from now on.`</p> | <p>I really like using Markdown.</p> <p>I think I'll use it to format all of my documents from now on.</p> |

#### 换行

| Type                                                                                                                      | Get                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| ``This is the first line with two space.  ``<br>`This is the second line without two space.`<br>`This is the third line.` | This is the first line with two space.<br>This is the second line without two space. This is the third line. |

### test

Alerts

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

| 元素         | 降价    | 呈现             |
| ------------ | ------- | ---------------- |
| 已删除的文本 | ~~foo~~ | <del>foo</del>   |
| 插入的文本   | ++bar++ | <ins>bar</ins>   |
| 标记文本     | ==baz== | <mark>baz</mark> |
| 下标         | H~2~O   | H<sub>2</sub>O   |
| 上标         | 1^st^   | 1<sup>st</sup>   |

#### Tutorials

[markdown中文教程](https://markdown.com.cn/)

sdfjklsjdf
sdjfklsldfj
