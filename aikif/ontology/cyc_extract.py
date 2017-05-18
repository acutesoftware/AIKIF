# cyc_extract.py    written by Duncan Murray 19/7/2014
#

from rdflib import Graph
#from rdflib import URIRef, Literal, Namespace #, ConjunctiveGraph
from rdflib import RDF
from rdflib import RDFS

def main():
    ip_folder =  'S:\\DATA\\opendata\\ontology\\OpenCyc\\'

    fname = ip_folder + 'open-cyc.n3'   # 770,166 tuples
    #create_sample_file('open-cyc.n3', 'sample_open_cyc.n3', 5000)
    #small_fname = 'sample_open_cyc.n3' #  6618 tuples
    
    g = load_graph_from_rdf(fname)
    show_graph_summary(g)
    export(g, fname + ".CSV")

def load_graph_from_rdf(fname):
    """ reads an RDF file into a graph """
    print(("reading RDF from " + fname + "...."))
    store = Graph()
    store.parse(fname, format="n3")
    print(("Loaded " + str(len(store)) + " tuples"))
    return store
    
def show_graph_summary(g):
    """ display sample data from a graph """
    sample_data = []
    print(("list(g[RDFS.Class]) = " + str(len(list(g[RDFS.Class])))))
    # Get Subject Lists
    num_subj = 0
    for subj in g.subjects(RDF.type):
        num_subj += 1
        if num_subj < 5:
            sample_data.append("subjects.subject: " + get_string_from_rdf(subj))
    print(("g.subjects(RDF.type) = " + str(num_subj)))
    
    # Get Sample of Subjects, Predicates, Objects
    num_subj = 0
    for subj, pred, obj in g:
        num_subj += 1
        if num_subj < 5:
            sample_data.append("g.subject   : " + get_string_from_rdf(pred))
            sample_data.append("g.predicate : " + get_string_from_rdf(subj))
            sample_data.append("g.object    : " + get_string_from_rdf(obj))
            
    print(("g.obj(RDF.type) = " + str(num_subj)))
    
    
    print ("------ Sample Data ------")
    for line in sample_data:
        print(line)

def export(g, csv_fname):
    """ export a graph to CSV for simpler viewing """
    with open(csv_fname, "w") as f:
        num_tuples = 0
        f.write('"num","subject","predicate","object"\n')
        for subj, pred, obj in g:
            num_tuples += 1
            f.write('"' + str(num_tuples) + '",')
            f.write('"' + get_string_from_rdf(subj) + '",')
            f.write('"' + get_string_from_rdf(pred) + '",')
            f.write('"' + get_string_from_rdf(obj) + '"\n')
    print(("Finished exporting " , num_tuples, " tuples"))
    
def get_string_from_rdf(src):
    """ extracts the real content from an RDF info object """
    res = src.split("/") #[:-1]
    return "".join([l.replace('"', '""') for l in res[len(res) - 1]])
        
 
def create_sample_file(ip, op, num_lines): 
    """ make a short version of an RDF file """
    with open(ip, "rb") as f:
        with open(op, "wb") as fout:
            for _ in range(num_lines):
                fout.write(f.readline() )


    
main()
