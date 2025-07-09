import markdown
from pathlib import Path

# Đường dẫn file markdown và css
md_path = input("MD: ")
html_name = input("HTML: ")
markdown_path = Path(md_path)

output_path = Path(f"{html_name}.html")

# Đọc nội dung
md_text = markdown_path.read_text(encoding="utf-8")


# Chuyển markdown thành HTML body
html_body = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])

# Gói vào khung HTML hoàn chỉnh
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown to HTML</title>
</head>
<body>
    <main class="markdown-body">
    {html_body}
    </main>
</body>
</html>
"""

# Ghi ra file
output_path.write_text(html_template, encoding="utf-8")
print("✅ File HTML đã được tạo tại output.html")
