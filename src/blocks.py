
def empty(s):
    return s != ''

def markdown_to_blocks(markdown):
    blocks = [str.strip() for str in markdown.split("\n\n")]
    return list(filter(empty, blocks))