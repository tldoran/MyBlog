---
title: "Showcase"
date: 2025-01-09
showcasePage: true
---

<h1>Showcase</h1>

{{ range .Site.RegularPages }}
  {{ if eq .Section "posts" }} <!-- Filter only posts -->
    <div class="post-preview">
      <h2><a href="{{ .Permalink }}">{{ .Title }}</a></h2>

      <!-- Show description if available or a truncated preview of the content -->
      <p>
        {{ if .Description }}
          {{ .Description }}
        {{ else }}
          {{ .Content | truncate 150 }}...
        {{ end }}
      </p>

      <a href="{{ .Permalink }}" class="read-more">Read More</a>
    </div>
  {{ end }}
{{ end }}
