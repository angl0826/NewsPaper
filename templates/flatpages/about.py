{% extends 'flatpages/default.html' %}

{% block title %}
{{ flatpage.title }}
{% endblock title %}

{% block content %}
    <h2>{{ flatpage.title }}</h2>
    <hr>
{{ flatpage.content }}
{{ flatpage.content }}
{% endblock content %}