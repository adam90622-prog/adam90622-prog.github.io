---
layout: default
title: Code Kata
---

# Code Kata

{% for item in site.codekata %}
- [{{ item.title | default:item.path }}]({{ item.url }})
{% endfor %}
