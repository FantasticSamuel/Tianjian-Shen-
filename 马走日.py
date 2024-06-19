#-*- coding: utf-8 -*
'''
author 钱瑞 2300011480
'''
import sys
sys.setrecursionlimit( 5000 )

class Vertex:
    def __init__( self, id ):
        self.id = id
        self.connection = {}
        self.property = property

    def add_property( self , property_name , property ) :
        self.property[ property_name ] = property

    def check_property( self , property_name ) :
        if property_name in self.property :
            return self.property[ property_name ]
        else :
            return None
    def add_connection( self , nbr , weight = 0 ) :
        self.connection[ nbr ] = weight

class Graph:
    def __init__( self ):
        self.vertices = {}
        self.numVertices = 0

    def add_Vertex( self, name ):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex( name )
        self.vertices[ name ] = newVertex
        return newVertex

    def get_Vertex( self , name ):
        if name in self.vertices:
            return self.vertices[ name ]
        else:
            return None

    def add_bilateral_Edge( self , f , t , weight = 0 ):
        if f not in self.vertices:
            self.add_Vertex( f )
        if t not in self.vertices:
            self.add_Vertex( t )
        self.vertices[ f ].add_connection( t , weight )
        self.vertices[ t ].add_connection( f , weight )

    def search( self , init_n , init_m ) :
        init_Vertex = self.get_Vertex( ( init_n , init_m ) )
        return self.__search( init_Vertex , { init_Vertex } )

    def __search( self , vertex , set_searched ) :
        ans = 0
        if len( set_searched ) == self.numVertices-1 :
            print( vertex.id , vertex.connection , set_searched )
            return 1
        for i in range( len( vertex.connection.keys() ) ) :
            if not ( self.get_Vertex( list( vertex.connection.keys() )[ i ] ) in set_searched ) :
                ans += self.__search( self.get_Vertex( list( vertex.connection.keys() )[ i ] ) , set_searched.union( { vertex } ) )
        return ans
'''
    def search( self , init_n , init_m,n,m ) :
        init_Vertex = self.get_Vertex( ( init_n , init_m ) )
        vis=set()
        set.add(init_m,init_n)
        return self.__search( ( init_n , init_m ), [ ( init_n , init_m ) ] )

    def __search( self , vertex , set_searched ) :
        ans = 0
        if len( set_searched ) == self.numVertices :
            print( self.get_Vertex( vertex ).id , list(self.get_Vertex( vertex ).connection.keys()) , set_searched )
            return 1
        nexts=list(self.get_Vertex( vertex ).connection.keys())
        for next_vertex in nexts:
            if not ( next_vertex in set_searched ):
                ans += self.__search(next_vertex , set_searched[:]+[next_vertex] )
        return ans
'''
'''
    def search( self , init_n , init_m ) :
        init_Vertex = self.get_Vertex( ( init_n , init_m ) )
        return self.__search( ( init_n , init_m ), [  ] )

    def __search( self , vertex , set_searched ) :
        ans = 0
        if len( set_searched ) == self.numVertices-1 :
            print( self.get_Vertex( vertex ).id , self.get_Vertex( vertex ).connection , set_searched )
            return 1
        for i in range( len( self.get_Vertex( vertex ).connection.keys() ) ) :
            if not ( list( self.get_Vertex( vertex ).connection.keys() )[ i ] in set_searched ) :
                ans += self.__search( list( self.get_Vertex( vertex ).connection.keys() )[ i ] , set_searched[:]+[ vertex ] )
        return ans
'''

n , m , init_n , init_m = list( map( int , input(  ).split(  ) ) )
G = Graph(  )
l_mov = [ ( 1,2 ) , ( 2,1 ) , ( -1,2 ) , ( -2,1 ) , ( 1,-2 ) , ( 2,-1 ) , ( -1,-2 ) , ( -2,-1 ) ]
#l_mov = [ ( 1 , 0 ) , ( -1 , 0 ) , ( 0 , 1 ) , ( 0 , -1 ) ]
for x in range( n ) :
    for y in range( m ) :
        G.add_Vertex( ( x , y ) )
for x in range( n ) :
    for y in range( m ) :
        for k in range( len( l_mov ) ) :
            mov = l_mov[ k ]
            if ( 0 <= mov[ 0 ]+x <= n-1 ) and ( 0 <= mov[ 1 ]+y <= m-1 ) :
                G.add_bilateral_Edge( ( x , y ) , ( mov[ 0 ]+x , mov[ 1 ]+y ) )
#for x in range( m ) :
#    for y in range( n ) :
#        print( G. )
print( G.search( init_n , init_m ) )

