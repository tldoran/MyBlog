---
title: "Showcase"
date: 2025-01-09
showcasePage: true
---

<div class="showcase">
  <h1>Showcase</h1>
  <div class="post-previews">
    {{ range where .Site.RegularPages "Section" "posts" }}
      {{ if not .Params.excludeFromHome }}
        <article class="post-preview">
          <h2 class="post-title">
            <a href="{{ .Permalink }}">{{ .Title | markdownify }}</a>
          </h2>
          <div class="post-description">
            {{ if .Description }}
              <p>{{ .Description }}</p>
            {{ else }}
              <p>{{ .Content | truncate 150 }}...</p>
            {{ end }}
          </div>
          <a href="{{ .Permalink }}" class="read-more">Read More</a>
        </article>
      {{ end }}
    {{ end }}
  </div>
</div>
