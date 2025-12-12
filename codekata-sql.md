---
layout: default
title: Code Kata – SQL
---

# Code Kata – SQL

{% assign kata_sql = site.codekata | where: "language", "sql" | sort: "order" %}
{% for item in kata_sql %}
- [{{ item.title }}]({{ item.url }})
{% endfor %}
