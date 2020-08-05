from biothings_explorer.user_query_dispatcher import SingleEdgeQueryDispatcher

seqd = SingleEdgeQueryDispatcher(output_cls = "ChemicalSubstance", 
								input_cls = "Gene",
								pred = "physically_interacts_with",
								input_id = "NCBIGene",
								values = "1017")

query = seqd.query(verbose = True)
print(query)