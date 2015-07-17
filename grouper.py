class Grouper(object):
   
   def __init__(self, init=[]):
      mapping = self._mapping = {}
      for x in init:
         mapping[x] = [x]
        
   def join(self, a, *args):      
      mapping = self._mapping
      set_a = mapping.setdefault(a, [a])

      for arg in args:
         set_b = mapping.get(arg)
         if set_b is None:
            set_a.append(arg)
            mapping[arg] = set_a
         elif set_b is not set_a:
            if len(set_b) > len(set_a):
               set_a, set_b = set_b, set_a
            set_a.extend(set_b)
            for elem in set_b:
               mapping[elem] = set_a

   def joined(self, a, b):      
      mapping = self._mapping
      try:
          return mapping[a] is mapping[b]
      except KeyError:
          return False

   def __iter__(self):      
      seen = set()
      for elem, group in self._mapping.iteritems():
          if elem not in seen:
              yield group
              seen.update(group)
