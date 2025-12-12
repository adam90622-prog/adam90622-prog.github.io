---
layout: default
title: Code Kata – Python
---

# Code Kata – Python

{% assign kata_python = site.codekata | where: "language", "python" | sort: "order" %}
{% for item in kata_python %}
- [{{ item.title }}]({{ item.url }})
{% endfor %}
