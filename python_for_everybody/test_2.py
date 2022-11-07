    while i > 0:
      contents = random.randrange(len(self.contents))
      newContents = self.contents.pop(contents)
      new_list.append(newContents)
      i -= 1
      len_contents -= 1
      if len_contents == 0 and i >= 1:
        self.contents = deep_contents
        len_contents = i
    return new_list

    new_list = []
    i = number
    len_contents = len(self.contents)
    deep_contents = copy.deepcopy(self.contents) # they recommend using copy module deepcopy() is from that 
    for i in range(number):
      contents = random.sample(self.contents, min(number, len(self.contents)))
      new_list.append(contents)
    return new_list















