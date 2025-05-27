from scholarly import scholarly

# Your Google Scholar ID (from the URL)
scholar_id = 'bXATl38AAAAJ' 

# Retrieve author information by ID
author = scholarly.search_author_id(scholar_id) 

# Fill in the author's data with publications
author = scholarly.fill(author, sections=['publications'])

# Get the 5 most recent publications
publications = author['publications'][:10]

# Create the markdown list
pub_list = "\n".join([f"- {pub['bib']['title']}" for pub in publications])

# Read current README.md
with open("README.md", "r") as f:
    readme = f.read()

# Define markers
marker_start = "<!--SCHOLAR-START-->"
marker_end = "<!--SCHOLAR-END-->"

# Replace between markers
before = readme.split(marker_start)[0] + marker_start + "\n"
after = "\n" + marker_end + readme.split(marker_end)[1]
new_readme = before + pub_list + after

# Write the updated README.md
with open("README.md", "w") as f:
    f.write(new_readme)