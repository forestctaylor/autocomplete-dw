import os 
import pandas as pd

def loadSearchSuggestionData():
    path = os.path.join(os.getcwd(), 'C:/Users/pacummi/OneDrive - Microsoft/Documents/DW/autocomplete-dw/autocomplete-dw-services/flaskr/resources/user-ct-test-collection-01.txt')
    df = pd.read_csv(path, 
                    sep=r"\t", # delimiter is tabs (data needs cleaning, but tabs is the best bet for now)
                    names=["AnonID", "Query", "QueryTime", "ItemRank", "ClickURL"],
                    engine="python")

    return [str(entry) for entry in df['Query'].to_list()]

def querySearchSuggestions(searchString, ls):
    """
    TODO: Make search more efficient. This bare-bones, worst-case O(n) approach is algorithmically no better than a 
    tree-based + DFS approach, but practically it may still be more performant to traverse a tree with DFS.
    """

    searchString = str(searchString)
    suggestions = []

    for entry in ls:
        #print(f'Checking {entry}')
        if entry.startswith(searchString): # Greedy query algorithm
            if entry not in suggestions:
                suggestions.append(entry)
        if len(suggestions) > 9:
            break

    return {'suggestions': suggestions}