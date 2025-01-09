<h1>Showcase</h1>

<div class="post-previews">
  {{ range .Site.RegularPages }}
    {{ if eq .Section "posts" }} <!-- Only show posts from the "posts" section -->
      <article class="post-preview">
        <h2><a href="{{ .Permalink }}">{{ .Title }}</a></h2>

        <!-- Show description if available or a truncated preview of the content -->
        <div class="post-description">
          {{ if .Description }}
            <p>{{ .Description }}</p>
          {{ else }}
            <p>{{ .Content | truncate 150 }}...</p>
          {{ end }}
        </div>

        <!-- Link to full post -->
        <a href="{{ .Permalink }}" class="read-more">Read More</a>
      </article>
    {{ end }}
  {{ end }}
</div>
