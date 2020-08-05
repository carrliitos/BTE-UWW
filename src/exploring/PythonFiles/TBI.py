# import modules from biothings_explorer
from biothings_explorer.hint import Hint
from biothings_explorer.user_query_dispatcher import FindConnection

ht = Hint()
# Find all potential representations of TBI
tbi_hint = ht.query("traumatic brain injury")
print(tbi_hint)
print()
# Select the correct representation of TBI
tbi = tbi_hint["Disease"][0]
print(tbi)
print()

# Find all potential representations of unipolar depression
depression_hint = ht.query("unipolar depression")
print(depression_hint)
print()
# Select the correct representation of depression
depression = depression_hint["Disease"][0]
print(depression)
print()

# help(FindConnection.__init__)
fc = FindConnection(input_obj=depression, output_obj=tbi, intermediate_nodes="BiologicalEntity")
# BTE finding connection
fc.connect(verbose=True)

print()
print("Displaying and filter results")
# Displaying and filter results
df = fc.display_table_view()
# because UMLS is not currently well-integrated in our ID-to-object translation system, removing UMLS-only entries here
patternDel = "^UMLS:C\d+"
filter = df.node1_id.str.contains(patternDel)
df = df[~filter]

fc.to_graphml("TBI.graphml")
fc.to_reasoner_std()

print(df.shape)
df.sample(10)

# Which diseases are mentioned the most
mentioned = df.node1_name.value_counts().head(10)
print(mentioned)

print()
print("fetch all articles connecting 'unipolar depression' and 'OBESITY DISORDER'")
# fetch all articles connecting 'unipolar depression' and 'OBESITY DISORDER'
articles = []
for info in fc.display_edge_info('unipolar depression', 'OBESITY DISORDER').values():
    if 'pubmed' in info['info']:
        articles += info['info']['pubmed']
print("There are "+str(len(articles))+" articles supporting the edge between unipolar depression and TBI. Sampling of 10 of those:")
x = [print("http://pubmed.gov/"+str(x)) for x in articles[0:10] ]

print("fetch all articles connecting 'OBESITY DISORDER' and 'TBI")
# fetch all articles connecting 'ABL1' and 'Imatinib
articles = []
for info in fc.display_edge_info('OBESITY DISORDER', 'Traumatic Brain Injury').values():
    if 'pubmed' in info['info']:
        articles += info['info']['pubmed']
print("There are "+str(len(articles))+" articles supporting the edge between OBESITY DISORDER and TBI. Sampling of 10 of those:")
x = [print("http://pubmed.gov/"+str(x)) for x in articles[0:10] ]