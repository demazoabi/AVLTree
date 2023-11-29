
import random

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
   """Constructor, you are allowed to add more fields.
        
        @type key: int or None
        @param key: key of your node
        @type value: any
        @param value: data of your node
        """


   def __init__(self, key, value):

      self.key = key
      self.value = value
      self.left = None
      self.right = None
      self.parent = None
      self.height = 0
      self.size = 1
      if self.key == None:
         self.height = -1
         self.size = 0


   """"returns the Balance factor using a simple formula balance_factor = left.height-right.height
        @:rtype int or None
        @:returns: the balance facotr of tree
        """


   def get_balance_factor(self):
      # edge cases for right
      right = self.get_right().get_height()
      if not self.get_right().is_real_node():
         right = -1
      # edge cases for left
      left = self.get_left().get_height()
      if not self.get_left().is_real_node():
         left = -1
      return left - right


   """returns the key

        @rtype: int or None
        @returns: the key of self, None if the node is virtual
        """


   def get_key(self):
      return self.key


   """"
        updates the size of the nodes according to the size of it's descendets 
        """


   def update_size(self):
      self.size = 1 + self.get_left().get_size() + self.get_right().get_size()


   """returns the value

        @rtype: any
        @returns: the value of self, None if the node is virtual
        """


   def get_value(self):
      return self.value


   """returns the left child
        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child (if self is virtual)
        """


   def get_left(self):
      return self.left


   """returns the right child

        @rtype: AVLNode
        @returns: the right child of self, None if there is no right child (if self is virtual)
        """


   def get_right(self):
      return self.right


   """returns the parent 

        @rtype: AVLNode
        @returns: the parent of self, None if there is no parent
        """


   def get_parent(self):
      return self.parent


   """returns the height

        @rtype: int
        @returns: the height of self, -1 if the node is virtual
        """


   def get_height(self):
      return self.height

   """
   @:returns a string representing the node (b=BalanceFactor,h=height,s=size, k = key, p = parent)
   """
   def __repr__(self):
      if not self.is_real_node():
         return f"N! p={self.get_parent().get_key()}"
      return f" (b={self.get_balance_factor()},h={self.get_height()},s={self.get_size()},k= {self.key},p={self.get_parent().get_key()})"


   """returns the size of the subtree

        @rtype: int
        @returns: the size of the subtree of self, 0 if the node is virtual
        """


   def get_size(self):
      return self.size


   """sets key

        @type key: int or None
        @param key: key
        """


   def set_key(self, key):
      self.key = key


   """sets value

        @type value: any
        @param value: data
        """


   def set_value(self, value):
      self.value = value


   """sets left child

        @type node: AVLNode
        @param node: a node
        """


   def set_left(self, node):
      self.left = node


   """sets right child

        @type node: AVLNode
        @param node: a node
        """


   def set_right(self, node):
      self.right = node


   """sets parent

        @type node: AVLNode
        @param node: a node
        """


   def set_parent(self, node):
      self.parent = node


   """sets the height of the node

        @type h: int
        @param h: the height
        """


   def set_height(self, h):
      self.height = h


   """sets the size of node

        @type s: int
        @param s: the size
        """


   def set_size(self, s):
      self.size = s

   """"
   updates the height of the node using the formula h= 1+max(left.height,right.height)  O(1)
   """
   def update_height(self):
      self.height = 1 + max(self.left.get_height(), self.right.get_height())


   """returns whether self is not a virtual node 

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """


   def is_real_node(self):
      return not self.key == None


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
   """
        Constructor, you are allowed to add more fields.  

        """


   def __init__(self):
      self.root = None
      self.size = 0
      # add your fields here
   """
   sets the root of the tree, O(1)
   """
   def set_root(self,node):
      if node == None or node.is_real_node == False:
         self.root = None
      self.root = node
   ## right

   """
   perform a simple right rotation, "rewires" the tree using O(1) getters and setters of the AvlNode class
   O(1)
   @:param node - the "faulty" node with |BS| >= 2
   @:param child_node - the unbalanced child.
   """
   def right_right_rotation(self, node, child_node):
      ## performs "rewiring" of the node and child_node- the "faulty" son
      node.set_left(child_node.get_right())
      node.get_left().set_parent(node)
      child_node.set_right(node)
      child_node.set_parent(node.get_parent())
      # taking care of edge case (the child node is the new root)
      if child_node.get_parent() == None:
         self.set_root(child_node)
      # the child node is the left son of its new parent node
      elif child_node.get_parent().get_key() > child_node.get_key():
         child_node.get_parent().set_left(child_node)
      # the child node is the righ son of its new parent node
      else:
         child_node.get_parent().set_right(child_node)
      node.set_parent(child_node)
      # updating sizes Bottom- up
      node.update_size()
      node.update_height()
      child_node.update_size()
      child_node.update_height()


   """
   gets successor of node within the tree, worst case scenario O(log(n)) operations
   mean comlexity is O(1)
   @:param node - gets the node with the "closest" bigger value than the given node.
   """

   def successor(self,node):
      ## edge cases
      if node.is_real_node() == False:
         return -1
      # if the node has right son- its successor will be found in its right subtree
      if node.right.is_real_node():
         node = node.right
         while node.left.is_real_node():
            node = node.left
         return node
      our_key = node.key
      # else its found in its parent nodes
      while node.key <= our_key:
         node = node.parent
      return node

   ## complex R rotation
   """
   performs a RL rotation using right right followed by left left rotation
   O(1)+O(1) = O(1)
   :param node - the "faulty" node with |BS| >= 2
   :param child_node - the "faulty" son causing the |BS| >=2
   """
   def right_left_rotation(self, node, child_node):
      # pivot node is the node that takes part in rotations
      pivot_node = child_node.get_left()
      self.right_right_rotation(child_node, pivot_node)
      self.left_left_rotation(node, pivot_node)


   ## complex LR rotation
   """
   same as right_left_rotation, but mirrored """
   def left_right_rotation(self, node, child_node):
      # pivot node is the node that takes part in rotations
      pivot_node = child_node.get_right()
      self.left_left_rotation(child_node, pivot_node)
      self.right_right_rotation(node, pivot_node)
   """
   same as right_right
   """

   ## simple left rotation
   def left_left_rotation(self, node, child_node):
      # rewires the node, and child node
      node.set_right(child_node.get_left())
      node.get_right().set_parent(node)
      child_node.set_left(node)
      child_node.set_parent(node.get_parent())
      # edge case , child node is new root
      if child_node.get_parent() == None:
         self.set_root(child_node)
      #child node is new left son of its parent
      elif child_node.get_parent().get_key() > child_node.get_key():
         child_node.get_parent().set_left(child_node)
      else:
      # child node is new right son of its parent
         child_node.get_parent().set_right(child_node)
      node.set_parent(child_node)
      ## maintaining sizes bottom up
      node.update_size()
      node.update_height()
      child_node.update_size()
      child_node.update_height()


   """this method is given a node with |BF| > 2 and performs the respective rotation
        also corrects the height and size of its nodes
        @:param delete- changes the flow of the program if it's called from delete
        @:returns the amount of rotations 1 if L or R rotation, 2 if LR or RL rotation.
        """
   def perform_rotation(self, node, delete=False):
      ##first if-else - for choosing higher child
      if node.get_right().get_height() < node.get_left().get_height():
         child_node = node.get_left()
         retval = 0
         # choosing between simple rotation to complex rotation
         if child_node.get_balance_factor() > 0 or (delete and child_node.get_balance_factor() == 0):
            self.right_right_rotation(node, child_node)
            retval = 1
         else:
            self.left_right_rotation(node, child_node)
            retval = 2
      else:
        # choosing between simple rotation to complex rotation
         child_node = node.get_right()
         if child_node.get_balance_factor() > 0:
            self.right_left_rotation(node, child_node)
            retval = 2
         else:
            self.left_left_rotation(node, child_node)
            retval = 1
      # returning the cost of flips
      return retval


   """searches for a node in the dictionary corresponding to the key
         O(log(n))
        @type key: int
        @param key: a key to be searched
        @rtype: AVLNode
        @returns: node corresponding to key.
        """

   def search(self, key):
      node = self.get_root()
      # loops while we are visiting un-virtual nodes
      while node.is_real_node():
         # we got the node- return
         if node.get_key() == key:
            return node
         # is bigger than wanted node- go left
         elif node.get_key() > key:
            node = node.get_left()
         # go right
         elif node.get_key() < key:
            node = node.get_right()
      return None


   """inserts val at position i in the dictionary

        @type key: int
        @pre: key currently does not appear in the dictionary
        @param key: key of item that is to be inserted to self
        @type val: any
        @param val: the value of the item
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
   def insert(self, key, val):
      ##initing vars
      new_node = AVLNode(key, val)
      new_node.set_left(AVLNode(None, None))
      new_node.set_right(AVLNode(None, None))
      new_node.get_left().set_parent(new_node)
      new_node.get_right().set_parent(new_node)
      roll_count = 0
      ##empty tree - edge casess
      if self.root == None:
         self.set_root(new_node)
         self.size += 1
         return 0
      if self.root.is_real_node() == False:
         self.set_root(new_node)
         self.size += 1
         return 0
      travesed_node = self.root
      ##seeking stage
      while travesed_node != None or not travesed_node.is_real_node():
         travesed_node.set_size(travesed_node.get_size() + 1)
         if travesed_node.get_key() > key:
            if travesed_node.get_left().is_real_node():
               travesed_node = travesed_node.get_left()
               continue
            else:
               travesed_node.set_left(new_node)
               new_node.set_parent(travesed_node)
               break
         elif travesed_node.get_key() < key:
            if travesed_node.get_right().is_real_node():
               travesed_node = travesed_node.get_right()
               continue
            else:
               travesed_node.set_right(new_node)
               new_node.set_parent(travesed_node)
               break
      parent_node = travesed_node

      #re-balancing stage
      while not parent_node == None:
         orig_height = parent_node.get_height()
         # node.height = 1 + max{ node.left.height, node.right.height }
         parent_node.update_height()
         if abs(parent_node.get_balance_factor()) < 2 and orig_height == parent_node.get_height():
            break
         elif abs(parent_node.get_balance_factor()) < 2 and orig_height != parent_node.get_height():
            parent_node = parent_node.get_parent()
            # would work without continue, for clarification.
            continue
         else:
            roll_count = self.perform_rotation(parent_node)
      self.size += 1
      return roll_count


   """deletes node from the dictionary
      first it takes care of "edge cases" O(1)
      than it searches the successor of pointed node at O(logn)
      than it perform "re-wiring" of the tree at        O(1)
      than it climb and rebalances the tree at          O(logn)
                                                         ______
                                                         O(logn)
        @type node: AVLNode
        @pre: node is a real pointer to a node in self
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """


   def delete(self, node):
      # Edge cases
      if self.root.size == 0:
         self.set_root(None)
         return -1
      if self.root.size == 1:
         self.set_root(None)
         return 0
      #sets new parent nodes
      par_node = node.parent
      parentToCheck = node.parent
      # inting variables
      if node.left.is_real_node() == False and node.right.is_real_node() == False:
         if node.parent != None:
            if node.parent.right == node:
               par_node.set_right(AVLNode(None,None))
               par_node.get_right().set_parent(par_node)
            else:
               par_node.set_left(AVLNode(None, None))
               par_node.left.set_parent(par_node)
         else:
            self.set_root(None)
            return 0

      elif node.left.is_real_node() and node.right.is_real_node():
         successor = self.successor(node)
         successorParent = successor.parent
         if successorParent != node:
            parentToCheck = successor.parent
            successorRight = successor.get_right()
            successorParent.set_left(successorRight)
            successorRight.set_parent(successorParent)
            successor.set_right(node.right)
            node.right.set_parent(successor)
         successor.set_left(node.left)
         node.left.set_parent(successor)

         if node == self.root:
            parentToCheck = successor.parent
            self.set_root(successor)
            successor.set_parent(None)

         else:
            par_node = node.parent
            if par_node.left == node:
               par_node.set_left(successor)
            else:
               par_node.set_right(successor)
            successor.set_parent(par_node)
         if successorParent == node:
            parentToCheck = successor

      #
      else:
         if node.left.is_real_node() == False:
            node.left.set_parent(node)
            nodetoconect = node.right
         else:
            node.right.set_parent(node)
            nodetoconect = node.left
         if par_node != None:
            if node.parent.right == node:
               par_node.set_right(nodetoconect)
               nodetoconect.parent = par_node
            else:
               par_node.set_left(nodetoconect)
               nodetoconect.parent = par_node
         else:
            self.set_root(nodetoconect)
            self.root.parent = None
      self.size = self.size - 1
      #fixing tree and returning the cost of the method
      return self.fix_tree(parentToCheck)


   """returns an array representing dictionary using a recursive method
   this method loops over all the nodes of the array giving us a sorted array
   at O(n)

        @rtype: list
        @returns: a sorted list according to key of tuples (key, value) representing the data structure
        """


   def avl_to_array(self):
      # using recursion to print the tree
      if self.root == None or self.root.is_real_node()==False:
         return []
      # recursion function used only in father function "scope"
      def avl_to_array_rec(node, arr):
         if node.is_real_node():
            avl_to_array_rec(node.left, arr)
            arr.append((node.key, node.value))
            avl_to_array_rec(node.right, arr)
      array = []
      avl_to_array_rec(self.root, array)
      return array


   """returns the number of items in dictionary  at O(1)

        @rtype: int
        @returns: the number of items in dictionary        """


   def size(self):
      # edge case
      if self.root == None:
         return 0
      else:
         #else unecessary, used for clarification
         return self.get_root().get_size()


   """splits the dictionary at a given node
   first it takes care of "edge cases" at       O(1)
   than it creates left tree (containing smaller values)
   and right tree (containing bigger values)     O(1)
   then, it sets the left subtree of node and the right subtree 
   to left_tree and right_tree respectivly
   than it "climbs" the tree and compares every node to the original node value- if its bigger- it joins the node and 
   the right subtree of it to right_tree, else it joins the left subtree to the left_subtree respectively
        @type node: AVLNode
        @pre: node is in self
        @param node: The intended node in the dictionary according to whom we split
        @rtype: list
        @returns: a list [left, right], where left is an AVLTree representing the keys in the 
        dictionary smaller than node.key, right is an AVLTree representing the keys in the 
        dictionary larger than node.key.
        """


   def split(self, node):
      #inting vars and taking care of edge cases
      tot_cnt = 0
      if self.root.size <= 1:
         self.set_root(None)
         return AVLTree(), AVLTree()
      init_node_size = node.get_key()
      # initialising big_tree and small_tree
      left_tree = AVLTree()
      right_tree = AVLTree()
      left_tree.set_root(node.get_left())
      node.get_left().set_parent(None)
      right_tree.set_root(node.get_right())
      node.get_right().set_parent(None)
      node = node.get_parent()
      # climbing the tree
      while node != None:
         if node.get_key() > init_node_size:
            if node.get_right() == None:
               right_tree.insert(node.get_key(), node.get_value())
            else:
               #joining subtree to right tree
               curr_right = node.get_right()
               curr_tree = AVLTree()
               curr_right.set_parent(None)
               curr_tree.set_root(node.get_right())
               curr_tree.root.set_parent(None)
               key, value = node.get_key(), node.get_value()
               node = node.get_parent()
               tot_cnt += right_tree.join(curr_tree, key, value)
         else:
            if node.get_left() == None:
               left_tree.insert(node.get_key(), node.get_value())
               # joining subtree to left_tree
            else:
               #re-wiring the tree
               curr_left = node.get_left()
               curr_tree = AVLTree()
               curr_left.set_parent(curr_tree)
               curr_tree.set_root(node.get_left())
               curr_tree.root.set_parent(None)
               key, value = node.get_key(), node.get_value()
               node = node.get_parent()
               tot_cnt += left_tree.join(curr_tree, key, value)
      # taking care of rare edge- cases
      if left_tree.root.is_real_node == False:
         left_tree.set_root(None)
      if right_tree.root.is_real_node == False:
         right_tree.set_root(None)
          # returning trees as list
      return [left_tree, right_tree]


   """the join method joins two trees T1, T2 and node N if every key in T1< N < T2
      or vice versa (T2< N <T1), 
      takes care of "edge cases" (empty trees, or almost empty trees) at O(1)
      then it classifies if self is bigger or @param tree is bigger. at  O(1)
      then, it traverses down the tree and finds the relevant node to connect O(logn)
      performs rewiring of the tree according to the algorithm learned  O(1)
      and than calls the fix tree method (O(log(n))
                                                                  ___________
                                                                  O(logn)
        @type tree: AVLTree 
        @param tree: a dictionary to be joined with self
        @type key: int 
        @param key: The key separting self with tree
        @type val: any 
        @param val: The value attached to key
        @pre: all keys in self are smaller than key and all keys in tree are larger than key,
        or the other way around.
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        """

   def join(self, tree, key, val):
      #edge cases (empty tree or trees with one nodes.
      if not tree.root == None and tree.root.is_real_node() == False:
         tree.set_root(None)
      if not self.root== None and self.root.is_real_node() == False:
         self.set_root(None)
      if tree.root == None and self.root == None:
         self.insert(key, val)
         return 1
      elif self.root == None:
         self.set_root(tree.root)
         self.size = tree.size
         self.insert(key, val)
         return tree.root.height + 1
      elif tree.root == None:
         self.insert(key, val)
         return self.root.height + 1
      # initialsing variables
      t_height = tree.root.height
      n_node = AVLNode(key, val)
      # deciding if self tree is bigger or smaller
      if t_height <= self.root.height:
         min_height = t_height
         max_height = self.root.height
         h_tree = self
         d_tree = tree
      else:
         min_height = self.root.height
         max_height = t_height
         h_tree = tree
         d_tree = self
      result = abs(self.root.height - tree.root.height) + 1
      node = h_tree.root

      if h_tree.get_root().get_key() > d_tree.get_root().get_key():
         #getting to desired node to join
         while max_height >= min_height:
            node = node.left
            max_height = node.height
      else:
         #getting to desired node to join
         while max_height >= min_height:
            node = node.right
            max_height = node.height
      # rewiring the tree if key is smaller
      if key < h_tree.root.key:
         node.parent.set_left(n_node)
         n_node.set_parent(node.parent)
         n_node.set_left(d_tree.root)
         d_tree.root.set_parent(n_node)
         n_node.set_right(node)
         node.set_parent(n_node)
      else:
         #rewiring the if key is bigger
         node = node.parent.get_right()
         node.parent.set_right(n_node)
         n_node.set_parent(node.parent)
         n_node.set_right(d_tree.root)
         d_tree.root.set_parent(n_node)
         n_node.set_left(node)
         node.set_parent(n_node)
      # fixing tree.
      h_tree.fix_tree(n_node)
      self.set_root(h_tree.root)
      h_tree.root.update_size()
      self.size = h_tree.root.size
      return result


   """computes the range of the node using the "size" field of AvlNode.
   the method climbs up the tree, (while the parent != None) 
   every iteration it adds the size of every subtree who is smaller than the
   given node (not using key, we can know it from the "ordering" of the tree)
   the loops takes at max O(logn) iterations, and each loop makes O(1) operations
   for a total of O(log(n)) time. 

        @type node: AVLNode
        @pre: node is in self
        @param node: a node in the dictionary which we want to compute its rank
        @rtype: int
        @returns: the rank of node in self
        """


   def rank(self, node):
      ##inting variables
      traversed_node = node
      ctr = node.get_left().get_size() + 1
      # using algorithm learned in class
      while traversed_node.get_parent() != None:
         former_node = traversed_node
         traversed_node = traversed_node.get_parent()
         if traversed_node.get_right() == former_node:
            ctr += traversed_node.get_left().get_size() + 1

      return ctr


   """finds the i'th smallest item (according to keys) in self

        @type i: int
        @pre: 1 <= i <= self.size()
        @param i: the rank to be selected in self
        @rtype: int
        @returns: the item of rank i in self
        """


   def select(self, i):
      def select_rec(node, i):
         k = node.left.get_size() + 1
         if k == i:
            return node
         if i < k:
            return select_rec(node.left, i)
         if i > k:
            return select_rec(node.right, i - k)


      return select_rec(self.root, i)


   """returns the root of the tree representing the dictionary

        @rtype: AVLNode
        @returns: the root, None if the dictionary is empty
        """


   def get_root(self):
      return self.root

   """
   auxiliary method of delete and join, this method climbs the tree and finds "faulty nodes.
   it performs a limited amount of "flips" so it take O(logn) time
   """
   def fix_tree(self, node):
      ## rotation counter
      rot = 0
      ## climbing and fixing the tree
      while node != None:
         bf = node.get_balance_factor()
         ## variable set for clarity
         new_h = 1 + max(node.left.get_height(), node.right.get_height())
         if -1 <= bf <= 1:
            node.update_height()
            node.update_size()
            node = node.parent
         else:
            # perform rotation
            rot += self.perform_rotation(node, delete=True)
      return rot
   """
   @:return the "representation" of a tree, each node is printed with its BF, height, parent
   takes O(n) time.
   """

