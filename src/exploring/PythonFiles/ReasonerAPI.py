from biothings_explorer.user_query_dispatcher import SingleEdgeQueryDispatcher

seqd = SingleEdgeQueryDispatcher(output_cls = "ChemicalSubstance", 
								input_cls = "Disease",
								pred = "physically_interacts_with",
								input_id = "NCBIGene",
								values = "1017")

query = seqd.query(verbose = True)

output = seqd.to_reasoner_std() # Still need to read documentation for this method
print()
print(output.keys())
# output: dict_keys(['query_graph', 'knowledge_graph', 'results'])
queryGraph = output["query_graph"]
knowledgeGraphNodes = output["knowledge_graph"]["nodes"][:5]
knowledgeGraphEdges = output["knowledge_graph"]["edges"][:5]
# output["results"][:5] 

print("\nQuery Graph:")
print(queryGraph)
print("\nKnowledge Graph Nodes:")
print(knowledgeGraphNodes)
print("\nKnowledge Graph Edges:")
print(knowledgeGraphEdges)