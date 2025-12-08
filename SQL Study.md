---
layout: default
title: SQL Study
---

# SQL Study

<details>
  <summary>SQL Study</summary>

  ### 🇰🇷 SQL Study (KR)
  <ul>
    {% assign items_kr = site.sql_kr | sort: "order" %}
    {% for item in items_kr %}
      <li><a href="{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
  </ul>

  ### 🇺🇸 SQL Study (EN)
  <ul>
    {% assign items_en = site.sql_us | sort: "order" %}
    {% for item in items_en %}
      <li><a href="{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
  </ul>

  ### 🇨🇳 SQL Study (CN)
  <ul>
    {% assign items_cn = site.sql_cn | sort: "order" %}
    {% for item in items_cn %}
      <li><a href="{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
  </ul>

</details>
