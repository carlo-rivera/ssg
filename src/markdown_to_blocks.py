def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped = map(lambda block: block.strip(), blocks)
    filtered = filter(lambda block: block != "", stripped)
    return list(filtered)