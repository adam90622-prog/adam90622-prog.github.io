---
layout: default
title: Code Kata
---

# Code Kata

## Python Code Kata

{% assign kata_python = site.codekata | where: "language", "python" | sort: "order" %}
{% for item in kata_python %}
- [{{ item.title }}]({{ item.url }})
{% endfor %}

---

## SQL Code Kata

{% assign kata_sql = site.codekata | where: "language", "sql" | sort: "order" %}
{% for item in kata_sql %}
- [{{ item.title }}]({{ item.url }})
{% endfor %}
