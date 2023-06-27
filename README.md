# `py-pdf-search`

## A python library for indexing and querying PDFS with a few lines of code.

`py-pdf-search` is a powerful Python library developed specifically for indexing and querying PDF documents, making it an ideal solution for patent search tasks. Whether you're an individual inventor or a company looking to protect your intellectual property, this library simplifies the process of searching for relevant patents while ensuring compliance with existing designs.

Traditionally, conducting a patent search involved hiring experienced patent lawyers to manually sift through databases and documents. While this approach offers reliable results and expert advice, it can be expensive. Alternatively, patent search engines like the US Patent and Trademark Office provide a more affordable and quicker solution, but they may lack the nuance and expertise of experienced lawyers.

With PY-PDF-SEARCH, you can leverage the power of natural language processing (NLP) or cosine similarity search to find relevant patent documents. The library enables you to index your PDF files, allowing you to search for specific terms, phrases, or concepts. By automating the search process, you save time and reduce the risk of missing critical information.

Here are two examples demonstrating the usage of PY-PDF-SEARCH:

### Example 1: NLP Search

````
from pdfagent import PDFAgent
import os

if __name__ == "__main__":
    agent = PDFAgent(
       "path/to/pdf_files",
        "openAIKEY"
        )

    res= agent.search("Can you find a document that uses chemicals for mining?")
    print(res)

    ```
````

### Example 2: Cosign Similarity Search

````
from pdfagent import PDFAgent
import os

if __name__ == "__main__":
    agent = PDFAgent(
       "path/to/pdf_files",
        "openAIKEY"
        )

    res= agent.search("Can you find a document that uses chemicals for mining?")
    print(res)

    ```
````
