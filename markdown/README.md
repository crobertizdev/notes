# Markdown

# Table o Content

- [Heading](#heading)
- [Emphasis](#emphasis)
- [List](#list)
- [Link](#link)
- [Quote](#quot)
- [Horizontal Line](#horizontal-line)
- [Code](#code)
- [Table](#table)
- [Image](#image)
- [Github Markdown](#github-markdown)
  - [Todo List](#todo-list)
  - [Mention Someone](#mention-someone)
  - [Emojis](#emojis)
  - [LateX](#latex)

[Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

[Wikipedia](https://es.wikipedia.org/wiki/Markdown)

> Ctrl + Shift + V for preview in vscode

To give line breaks leave a line between each one

# Heading

```md
# my title

## my title h2

### my title h3

#### my title h4

##### my title h5

###### my title h6

standar
```

# my title h1

## my title h2

### my title h3

#### my title h4

##### my title h5

###### my title h6

standar

# Emphasis

```md
_Italic type_
**Bold**
~~Negative~~
```

_Italic type_

**Bold**

~~Negative~~

# List

## Ordered lists.

```md
1. apple
2. orange
3. purple
```

1. apple
2. orange
3. purple

## unordered lists

```md
- apple
- orange
- purple
```

- apple
- orange
- purple

# Link

```md
[Google](https://google.com 'Title Link')
```

[Google](https://google.com 'Title Link')

# Quot

```md
> Take your time
```

> Take your time

# Horizontal Line

```md
---
```

---

# Code

```md
`console.log('Hola mundo')`
```

`console.log('Hola mundo')`

````md
```js
const name = ['Alvaro', 'Jose', 'Maria'];

if (name[0] === name[1]) {
  console.log('Yes');
}
```
````

```js
const name = ['Alvaro', 'Jose', 'Maria'];

if (name[0] === name[1]) {
  console.log('Yes');
}
```

# Table

```md
| Fruits | Price |
| :----- | :---- |
| Apple  | 1$    |
| Grapes | 4$    |
| Orange | 2$    |
| Lemon  | 1$    |
| Peach  | 3$    |
| Melon  | 20$   |
```

| Fruits | Price |
| :----- | :---- |
| Apple  | 1$    |
| Grapes | 4$    |
| Orange | 2$    |
| Lemon  | 1$    |
| Peach  | 3$    |
| Melon  | 20$   |

# Image

```md
![vscode](https://images.unsplash.com/photo-1648737155328-0c0012cf2f20?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80 'Title Image')
```

![Steve Jobs](https://images.unsplash.com/photo-1648737155328-0c0012cf2f20?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80 'Title Image')

# Github Markdown

This only works on github

## Todo list

```md
- [x] Task 1
- [ ] Task 2
- [ ] Task 3
- [x] Task 4
```

- [x] Task 1
- [ ] Task 2
- [ ] Task 3
- [x] Task 4

## Mention someone

@crobertizdev

## Emojis

[Github emojis](https://gist.github.com/rxaviers/7360908)

```md
:kissing:
```

:kissing:

## LateX

[LATEX](https://es.wikipedia.org/wiki/LaTeX#S%C3%ADmbolos_matem%C3%A1ticos)

[Documentación](https://es.overleaf.com/learn)

### Extensions for vscode:

- LaTeX
- LaTeX Utilities
- LaTeX Workshop

[Formulas LateX mas comunes](https://wiki.geogebra.org/es/C%C3%B3digo_LaTeX_para_las_f%C3%B3rmulas_m%C3%A1s_comunes)

[Inserta fórmulas matemáticas creadas en LateX](https://medium.com/@luiscarlos_40534/inserta-f%C3%B3rmulas-matem%C3%A1ticas-creadas-en-latex-con-markdown-ab59f5a68211)

Mathematical operations:

```latex
The Gamma function satisfying

$$
\Gamma(n) = (n-1)!\quad\forall
n\in\mathbb N
$$

is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$
```

The Gamma function satisfying

$$
\Gamma(n) = (n-1)!\quad\forall
n\in\mathbb N
$$

is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

### Font size

```latex
$\huge 320$

$\ 320$

$\tiny 320$
```

$\huge 320$

$\ 320$

$\tiny 320$

### Fractions

```latex
${\frac{5}{12 + 2} + {12}}$
```

${\frac{5}{12 + 2} + {12}}$

### More

Espacio en blanco

```latex
$ \ $
```

$ \ $

Arrows

```latex
$\rightarrow$
```

$\rightarrow$
