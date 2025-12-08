---
layout: default
title: Analysis Study
---

# Analysis Study

데이터 분석 과정을 정리한 글 목록입니다.

<ul>
  {% for item in site.analysis %}
    <li>
      <a href="{{ item.url }}">{{ item.title }}</a>
    </li>
  {% endfor %}
</ul>
