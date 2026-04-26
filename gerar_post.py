import datetime

titulo = "Exemplo de Post Automático"
data = datetime.datetime.now().strftime("%Y-%m-%d")

conteudo = """
Este é um post gerado automaticamente.
"""

arquivo = f"_posts/{data}-post.md"

with open(arquivo, "w", encoding="utf-8") as f:
    f.write(f"""---
title: "{titulo}"
date: {data}
image: /assets/img/exemplo.jpg
---

{conteudo}
""")
