import os 
import pandas as pd

def loadSearchSuggestionData():
    path = os.path.join(os.getcwd(), 'C:/Users/pacummi/OneDrive - Microsoft/Documents/DW/autocomplete-dw/autocomplete-dw-services/flaskr/resources/user-ct-test-collection-01.txt')
    df = pd.read_csv(path, 
                    sep=r"\t", # delimiter is tabs (data needs cleaning, but tabs is the best bet for now)
                    names=["AnonID", "Query", "QueryTime", "ItemRank", "ClickURL"],
                    engine="python")

    return df['Query'].tolist()

def querySearchSuggestions(searchString, ls):
    return {'suggestions': ['DUMMY']}