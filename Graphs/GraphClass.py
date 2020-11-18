
class Graph():

    def __init__(self):
        ''' constructor: empty dictionary of key value pairs
        '''
        self.adjacencyList = {}
        
    def __validateInput(self, inputToValidate, typeToValidate) -> bool:
        ''' method that validates input to a given type or isEmpty
            In: all inputToValidate 
                all typeToValidate 
            Out: bool validInput
        '''
        # empty input handling
        if(not inputToValidate or not typeToValidate):
            return False
        
        # type validation
        validInput = isinstance(inputToValidate,typeToValidate)
        if(not validInput): return False
        
        return True
        
    def __checkVertex(self, vertex: str) -> bool:
        ''' method that validates if vertex exist in graph
            In: str vertex 
            Out: bool validInput
        '''
        # input type validation
        if(not self.__validateInput(vertex,str)): return False
        
        # try calling for key, throws error if key does not exist
        try:
            self.adjacencyList[vertex]
            return True
        
        except:
            return False
    
    def hasEdgeBetween(self, vertex1: str, vertex2: str) -> bool:
        ''' method that checks weather vertex 1 has an edge to vertex 2
        '''
        # input type validation
        if(not self.__validateInput(vertex1,str)): return False
        if(not self.__validateInput(vertex2,str)): return False
        
        # check if vertex/nodes exist
        if(not self.__checkVertex(vertex1)): return 'vertex1 not in graph'
        if(not self.__checkVertex(vertex2)): return 'vertex2 not in graph'
        
        # check inside vertex 1 for vertex 2
        for i in self.adjacencyList[vertex1]:
            if(i==vertex2):
                return True
        
        return False
        
    def addVertex(self, vertex: str) -> str:
        ''' method that adds a node/vertex
            In: str vertex
            Out: str key added
        '''
        # input type validation
        if(not self.__validateInput(vertex,str)): return 'Invalid Input'
        
        # check for duplicate
        if(self.__checkVertex(vertex)): return 'Key already exist'
        
        # add to adjacencyList
        self.adjacencyList[vertex]=[]

        return vertex
    
    def addEdge_undirected(self, vertex1: str, vertex2: str) -> str:
        ''' method that adds an edge/link between two vertices both ways
        '''
        # validate both inputs
        if(not self.__validateInput(vertex1,str)): return 'Invalid Input'
        if(not self.__validateInput(vertex2,str)): return 'Invalid Input'
        
        # check if vertex/nodes exist
        if(not self.__checkVertex(vertex1)): return 'vertex1 not in graph'
        if(not self.__checkVertex(vertex2)): return 'vertex2 not in graph'
        
        # check if already connected between each other
        if(self.hasEdgeBetween(vertex1,vertex2) and self.hasEdgeBetween(vertex1,vertex2)): 
            return 'vertexes already connected'
        
        # add two way connection
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)
        
        return '"'+vertex1+'"' + ' undirected conection to ' + '"'+vertex2+'"'
        
            
        
#%% Testing methods

test = Graph()

#add nodes
test.addVertex('a')
test.addVertex('b')
test.addVertex('c')

#add edge between 'a' and 'b' 
test.addEdge_undirected('a','b')
test.addEdge_undirected('a','c')

for i in test.adjacencyList['a']:
    print(i)
    
    
    
    

    


