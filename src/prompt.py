prompt_template = """
Use the following pieces of information to provide a
helpful recommendation. If you don't know the answer, 
just say that you don't know, don't try to make up an 
answer.

Input (User Review): {input}
Output (Product Name): {output}
Response: {response}

Please provide a recommendation based on the given user 
review and product name. 

Only return the helpful recommendation below and nothing else.
Helpful recommendation:
"""
