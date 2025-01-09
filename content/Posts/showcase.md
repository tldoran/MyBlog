---
title: "Showcase"
description: "A showcase of all my blog posts"
excludeFmHome: true
---

<div class="showcase">
  <h1>{{ .Title }}</h1>
  <p>{{ .Description }}</p>

  <div class="posts-preview">
    {{ range where .Site.RegularPages "Type" "posts" }}
      {{ if ne .File.BaseFileName "showcase" }} <!-- Exclude the showcase file itself -->
        <article class="post-preview">
          <h2><a href="{{ .Permalink }}">{{ .Title }}</a></h2>
          <time datetime="{{ .Date }}">{{ .Date.Format "January 2, 2006" }}</time>
          {{ if .Params.description }}
            <p>{{ .Params.description }}</p>
          {{ else }}
            <p>{{ .Summary }}</p>
          {{ end }}
          <a href="{{ .Permalink }}">Read more</a>
        </article>
      {{ end }}
    {{ end }}
  </div>
</div>
