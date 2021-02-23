def check_path(path):
    # return true/false depending on whether the path is valid or not.
    i = 0
    while i < len(path) -1:
        child = path[i]
        parent = path[i+1]
        if child not in parent.get_moves():
            return False
        i += 1
    return True
    
    
    
    
# added a get_path() method to keep track of the path from start to finish
#def get_path(self):
 #  path = [self]
  # child = self
   #while child.get_parent() != None:
    #   child = child.get_parent()
     #  path.append(child)
   #return path