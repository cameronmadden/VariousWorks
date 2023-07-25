#  File: TestBinaryTree.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

class Node (object):
    
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

  def __str__ (self):
    s = str(self.data)
    return s


class Tree (object):

  def __init__ (self):
    self.root = None
    # self.size = 0
    
  def insert (self, data):
    new_node = Node(data)
    if (self.root == None):
        self.root = new_node
        return
    else:
        current = self.root
        parent = self.root
        while (current != None):
            parent = current
            if (data < current.data):
                current = current.lchild
            else:
                current = current.rchild

        if (data < parent.data):
            parent.lchild = new_node
        else:
            parent.rchild = new_node

  # inorder traversal - left, center, right
  def in_order (self, root, resstr):
    if (root != None):
      resstr = self.in_order (root.lchild, resstr)
      resstr += (str(root.data) + ' ')
      resstr = self.in_order (root.rchild, resstr)
    return resstr

  # preorder traversal - center, left, right
  def pre_order (self, root, resstr):
    if (root != None):
      resstr += (str(root.data) + ' ')
      resstr = self.pre_order (root.lchild, resstr)
      resstr = self.pre_order (root.rchild, resstr)
    return resstr

  def post_order (self, root, resstr):
    if (root != None):
      resstr = self.post_order (root.lchild, resstr)
      resstr = self.post_order (root.rchild, resstr)
      resstr += (str(root.data) + ' ')
    return resstr

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
      resstr = ''
      current = self.root
      other_curr = pNode.root
      if self.pre_order(current, resstr) == pNode.pre_order(other_curr, resstr) \
         and self.in_order(current, resstr) == pNode.in_order(other_curr, resstr) \
         and self.post_order(current, resstr) == pNode.post_order(other_curr, resstr):
          return True
      else:
          return False


  # Returns a list of nodes at a given level from left to right
  def get_level (self, level):
      levelstart = 0
      nodelist = []
      root = self.root
      self.get_level_helper(root, level, levelstart, nodelist)
      
      return nodelist
    
  def get_level_helper(self, root, level, levelstart, nodelist):
      if (root != None):
          if levelstart == level:
              nodelist.append (root)
              #print (nodelist)
          self.get_level_helper(root.lchild, level, levelstart + 1, nodelist)
          self.get_level_helper(root.rchild, level, levelstart + 1, nodelist)
          
  # Returns the height of the tree
  def get_height (self):
      height_lst = []
      height = 0
      root = self.root
      if root == None:
          return -1
      self.get_height_helper(root, height, height_lst)
      max_height = max(height_lst)
      return max_height

  def get_height_helper (self, root, height, height_lst):
      if root != None:
          height_lst.append(height)
          self.get_height_helper(root.rchild, height + 1, height_lst)
          self.get_height_helper(root.lchild, height + 1, height_lst)


  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
      count = 0
      root = self.root
      c = self.num_nodes_helper(root, count)
      return c
    
  def num_nodes_helper(self, root, count):
      if root != None:
          count += 1
          count = self.num_nodes_helper(root.lchild, count)
          count = self.num_nodes_helper(root.rchild, count)
      return count        
              
      

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line))# converts elements into ints

    tree1 = Tree()
    for i in tree1_input:
        tree1.insert(i)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints

    tree2 = Tree()
    for i in tree2_input:
        tree2.insert(i)
    
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints

    tree3 = Tree()
    for i in tree3_input:
        tree3.insert(i)


    # Test your method is_similar()
    resstr = ''
    print (tree1.pre_order(tree1.root, resstr))
    print (tree1.in_order(tree1.root, resstr))
    print (tree1.post_order(tree1.root, resstr))
    # Print the various levels of two of the trees that are different
    
    print (tree1.get_level(3))

    print (tree1.num_nodes())
    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree

if __name__ == "__main__":
  main()
