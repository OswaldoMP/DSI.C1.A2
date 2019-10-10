from forest import Node, ParcialTree
from board import Coordinate
from anytree import RenderTree,PreOrderIter
from PIL import Image


a = Coordinate(0,0)
b = Coordinate(0,1)
c = Coordinate(0,2)
d = Coordinate(1,0)
# e = Coordinate(1,1)
f = Coordinate(1,2)
g = Coordinate(2,0)
h = Coordinate(2,1)
i = Coordinate(2,2)

a.neighbors = [b,d]
b.neighbors = [c,a]
c.neighbors = [f,b]
d.neighbors = [a,g]
#e.neighbors = [b,d,f,h]#Bloqueo
f.neighbors = [c,i]
g.neighbors = [d,h]
h.neighbors = [i,g]
i.neighbors = [f,h]

initial = a
finish = i

located = False
iteration = 0

root = Node(str(initial))#inicio 

stack_nodes = [root]
stack_coordinates = [initial]

def createTree(stack_coordinates, stack_nodes):
    for neighbor in stack_coordinates[-1].neighbors:
        if len(stack_coordinates) > 16:
            break
        stack_coordinates.append(neighbor)
        ############# Make Nodes #############
        new_node = Node(str(neighbor), stack_nodes[-1], 0)
        stack_nodes.append(new_node)
        ######################################
        createTree(stack_coordinates, stack_nodes)

        stack_coordinates.pop()
        stack_nodes.pop()

createTree(stack_coordinates, stack_nodes)#Crear árbol
##############################################
depth = 16
depthLimited = 4
##algoritmo depthLimit
for nivel in range(depth):#rango del árbol. Se uso una profundidad de 16.
    print('nivel: ', nivel)
    if located:
        break
        pass
    for node in PreOrderIter(root, maxlevel=nivel+depthLimited):#Liimite del rango que puede hacer la busqueda
        print('node: ',node)
        iteration = iteration + 1
        if node.name == str(finish):
            located = node
            break
            pass
        pass

# for pre,fill, node in RenderTree(root):
#     print('%s%s' % (pre,node.name))

print('iteration: ', iteration)
tree  = ParcialTree(located)
tree.render()
image = Image.open('Digraph.gv.png')
image.show()
