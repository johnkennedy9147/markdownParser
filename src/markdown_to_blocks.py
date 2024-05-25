def  markdown_to_blocks(markdown):
  blocks = markdown.split('\n\n')
  filtered_blocks = []
  for block in blocks:
    if block == "":
      continue
    filtered_blocks.append(block.strip())
  return filtered_blocks
