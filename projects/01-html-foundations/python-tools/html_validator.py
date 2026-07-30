from bs4 import BeautifulSoup


def validate_and_prettify(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    # Basic structure tags
    required_tags = ["html", "head", "body", "title"]

    # Semantic tags
    semantic_tags = ["header", "nav", "main", "footer"]

    print("=== Basic Structure Validation ===")
    for tag in required_tags:
        if soup.find(tag):
            print(f"✓ <{tag}> tag found")
        else:
            print(f"✗ <{tag}> tag is MISSING")

    print("\n=== Semantic Tags Validation ===")
    for tag in semantic_tags:
        if soup.find(tag):
            print(f"✓ <{tag}> tag found")
        else:
            print(f"✗ <{tag}> tag is MISSING")

    print("\n=== Prettified HTML ===")
    print(soup.prettify())


# Test with your conference page
validate_and_prettify("projects/01-html-foundations/conference.html")
