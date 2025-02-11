#portfolio file is used to retrive and add data from using chromadb
import pandas as pd
import chromadb 
import uuid

class Portfolio:
    #on initilization of the class, we will load the data from the csv file and create a collection in the chromadb
    def __init__(self,file_path="/Users/varadaraj/MachineLearning/GenAi Projects/Cold Email Generator/app/resource/my_portfolio.csv"):
        self.file_path=file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name = 'portfolio')
    
    #add data into the db 
    def load_portfolio(self):
        if not self.collection.count():
            for _,row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links:":row["Links"]},
                                    ids=str(uuid.uuid4()))
    
    #retrive data from the db with vector search matching of skills,
    #we are retriving only metadata ie links from the db
    def query_links(self,skills):
        return self.collection.query(query_texts=skills,n_results=2).get('metadatas',[])