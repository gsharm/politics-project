# views.py
import markdown
from django.http import HttpResponse

def serve_markdown(request):
    # Read markdown content
    with open("sunak-v-starmer.md", "r") as file:
        md_content = file.read()

    # Convert to HTML
    html_content = markdown.markdown(md_content)

    return HttpResponse(html_content)
