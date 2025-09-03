# from scholarly import scholarly
# # Author info
# scholar_id = 'bXATl38AAAAJ' 
# author = scholarly.search_author_id(scholar_id)
# author = scholarly.fill(author, sections=['publications'])

# # Order by data
# publications = sorted(
#     author['publications'], 
#     key=lambda x: x.get('bib', {}).get('pub_year', 0), 
#     reverse=True
# )

# # 5 recents
# publications = publications[:5]

# # Markdown list
# pub_list = "\n".join([
#     f"- [{pub['bib']['title']}]({pub.get('pub_url', 'https://scholar.google.com')})"
#     for pub in publications
# ])

# # read readme
# with open("README.md", "r") as f:
#     readme = f.read()

# # find the place to replace
# marker_start = "<!--SCHOLAR-START-->"
# marker_end = "<!--SCHOLAR-END-->"

# # replace
# before = readme.split(marker_start)[0] + marker_start + "\n"
# after = "\n" + marker_end + readme.split(marker_end)[1]
# new_readme = before + pub_list + after

# # write on readme
# with open("README.md", "w") as f:
#     f.write(new_readme)
