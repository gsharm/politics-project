# views.py
import markdown
import os

from django.http import HttpResponse

def serve_markdown_index(request):
    return HttpResponse('''
    <html>
        <head>
            <title>Test Title</title>
        </head>
        <body>
            Test Body
        </body>
    </html>
    ''')

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
    # Convert the markdown content to HTML
    html_content = markdown.markdown(md_content)

    # Wrap the HTML content
    full_html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
        <title>MP Details</title>
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