import os
import re
import shutil

# Paths
posts_dir = "/Users/tldoran/Documents/oransblog/content/Posts/"
attachments_dir = "/Users/tldoran/Documents/Obsidian Vault/assets/"
static_images_dir = "/Users/tldoran/Documents/oransblog/static/images/"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r") as file:
            content = file.read()
        
        # Step 2: Find all image links in Obsidian format (for example, ![[image.png]])
        images = re.findall(r'!\[\[([^\]]+\.(jpg|jpeg|png|gif|bmp|svg))\]\]', content)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image, ext in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"![[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                # Ensure the target directory exists
                target_image_dir = os.path.join(static_images_dir, os.path.dirname(image))
                os.makedirs(target_image_dir, exist_ok=True)  # Create directory if it doesn't exist
                shutil.copy(image_source, os.path.join(target_image_dir, os.path.basename(image)))

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
