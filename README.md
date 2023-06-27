# `py-pdf-search`

## A python library for indexing and querying PDFS with a few lines of code.

`py-pdf-search` is a powerful Python library developed specifically for indexing and querying PDF documents, making it an ideal solution for patent search tasks.

Here are two examples demonstrating the usage of PY-PDF-SEARCH:

### Example 1: NLP Search

```python
from pdfagent import PDFAgent
import os

if __name__ == "__main__":
    agent = PDFAgent(
       "path/to/pdf_files",
        "openAIKEY"
        )

    res= agent.search("Find patent filings related to secure and scalable filing systems for medical records.")
    print(res)
```

### Example 2: Cosign Similarity Search

```python
from pdfagent import PDFAgent
import os

if __name__ == "__main__":
    agent = PDFAgent(
       "path/to/pdf_files",
        "openAIKEY"
        )

    res= agent.cosign_similarity("<PATH_TO_PDF>", k=3)
    print(res)
```

### Checkout the Presentation Here [Presentation Link](https://docs.google.com/presentation/d/1VKtHyzxR18cRrQyVJc_gwY57BEw4znUJzhIeSzXjH94/edit?usp=sharing)
