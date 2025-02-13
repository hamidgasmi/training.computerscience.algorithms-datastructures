import sys
from collections import namedtuple

Edge = namedtuple('Edge', ['start', 'len'])

class Suffix_Tree:
  def __init__(self, text):
    self.text = text
    self.text_len = len(self.text)
    self.build_suffix_tree()

  def search_edge_to_break(self, node, suffix_starting_pos):
    
    node_from = node
    node_to = -1
    common_len = 0  
    len_limit = 0
    for child in self.nodes[node]:

      edge = self.nodes[node][child]

      i = 0
      len_limit = min(edge.len, self.text_len - suffix_starting_pos)
      while i < len_limit and self.text[edge.start + i] == self.text[suffix_starting_pos + i]:
        common_len += 1
        i += 1

      if common_len > 0:
        node_to = child
        break
    
    if common_len > 0 and common_len == len_limit:
      if self.text_len - suffix_starting_pos <= len_limit:
        return(node_from, node_to, 0, common_len)
      else:
        (node_from, node_to, parent_len, sub_common_len) = self.search_edge_to_break(node_to, suffix_starting_pos + common_len)
        return(node_from, node_to, parent_len + common_len, sub_common_len)

    else:
      
      return(node_from, node_to, 0, common_len)

  def build_suffix_tree(self):
    
    # List of dictionaries:
    # {Node ID, (suffix start position, suffix length)}
    self.nodes = []
    self.nodes.append(dict()) # Node 0
    self.suffix_start_position = dict() # (key, value) : (Node ID, Suffix starting position)
    for i in range(self.text_len):

      suffix_text_len = self.text_len - i

      (node_from, node_to, parent_len, common_len) = self.search_edge_to_break(0, i)
      
      if common_len > 0:
        
        # Remove the previous edge from the node
        edge_to_break = self.nodes[node_from].pop(node_to)

        # Insert the new common edge
        new_common_edge = Edge(edge_to_break.start, common_len)
        new_common_node = len(self.nodes)
        self.nodes.append(dict())
        self.nodes[node_from][new_common_node] = new_common_edge
        node_from = new_common_node

        # Modify the existing edge
        existing_edge = Edge(edge_to_break.start + common_len, edge_to_break.len - common_len)
        self.nodes[node_from][node_to] = existing_edge

      # Insert new node for the suffix i:
      new_suffix_edge = Edge(i + common_len + parent_len, suffix_text_len - common_len - parent_len)
      new_suffix_node = len(self.nodes) 
      self.nodes.append(dict())
      self.nodes[node_from][new_suffix_node] = new_suffix_edge
      self.suffix_start_position[new_suffix_node] = i

  def edges_labels(self):
    labels = []

    for node in range(len(self.nodes)):
      for child in self.nodes[node]:
        edge = self.nodes[node][child]
        labels.append(self.text[edge.start:edge.start + edge.len])
        
    return labels

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  
  suffix_tree = Suffix_Tree(text)

  print("\n".join(suffix_tree.edges_labels()))
  