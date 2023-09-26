# views.py
import markdown
from django.http import HttpResponse

def serve_markdown_index(request):
    # Read markdown content
    with open("index.html", "r") as file:
        html_content = file.read()

    return HttpResponse(html_content)

def serve_markdown_mp(request, mp_name=None):
    # Determine the markdown filename based on the URL path
    if mp_name:
        file_name = f"mps/{mp_name}.md"
    else:
        file_name = "mp_not_found.md"  # You can set a default file name here if you like

    # Try reading markdown content
    try:
        with open(file_name, "r") as file:
            md_content = file.read()
    except FileNotFoundError:
       file_name = "mp_not_found.md"  # You can set a default file name here if you like
       with open(file_name, "r") as file:
            md_content = file.read()

    # Convert to HTML
    html_content = markdown.markdown(md_content)

    return HttpResponse(html_content)