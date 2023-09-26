# views.py
import markdown
import os

from django.http import HttpResponse

def serve_markdown_index(request):
    mps = list_mps()
    html_links = [f'<a href="/mps/{mp}/">{mp.replace("-", " ").title()}</a><br>' for mp in mps]
    
    html_content = f'''
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
    </head>
    <body>
        <h2>List of MPs:</h2>
        {"\n".join(html_links)}
    </body>
    </html>
    '''
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
    # Wrap the HTML content to include the CSS
    html_content = markdown.markdown(md_content)
    full_html_content = f'''
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
    </head>
    <body>
        {html_content}
    </body>
    </html>
    '''
    return HttpResponse(full_html_content)


def list_mps():
    """List all the markdown files in the mps/ directory."""
    files = os.listdir('mps/')
    return [f[:-3] for f in files if f.endswith('.md')]