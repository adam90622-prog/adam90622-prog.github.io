---
layout: default
title: SQL Study
---

# SQL Study

<!-- 토글 1: KOREAN -->
<details>
  <summary><strong>KOREAN</strong></summary>

  ### 🇰🇷 SQL Study (KR)

  <ul>
    {% assign items_kr = site.sql_kr | sort: "order" %}
    {% for item in items_kr %}
      <li><a href="{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
  </ul>

</details>

---

<!-- 토글 2: ENGLISH -->
<details>
  <summary><strong>ENGLISH</strong></summary>

  ### 🇺🇸 SQL Study (EN)

  <ul>
    {% assign items_en = site.sql_us | sort: "order" %}
    {% for item in items_en %}
      <li><a href="{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
  </ul>

</details>

---

<!-- 토글 3: CHINESE -->
<details>
  <summary><strong>CHINESE</strong></summary>

  ### 🇨🇳 SQL Study (CN)

  <ul>
    {% assign items_cn = site.sql_cn | sort: "order" %}
    {% for item in items_cn %}
      <li><a href="{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
  </ul>

</details>

---

## Debug – sql_us list

<ul>
  {% for item in site.sql_us %}
    <li>{{ item.url }} — {{ item.title }}</li>
  {% endfor %}
</ul>
