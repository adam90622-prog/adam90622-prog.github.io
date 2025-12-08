---
layout: default
title: Code Kata
---

# Code Kata 목록

<ul>
  {% for item in site.codekata %}
    <li>
      <a href="{{ item.url }}">{{ item.title }}</a>
    </li>
  {% endfor %}
</ul>
