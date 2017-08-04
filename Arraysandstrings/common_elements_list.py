#https://stackoverflow.com/questions/2864842/common-elements-comparison-between-2-lists
def common_elements1(a, b):
  a.sort()
  b.sort()
  i, j = 0, 0
  common = []
  while i < len(a) and j < len(b):
    if a[i] == b[j]:
      common.append(a[i])
      i += 1
      j += 1
    elif a[i] < b[j]:
      i += 1
    else:
      j += 1
  return ''.join(str(common))

def common_elements2(a,b):

  return list(set(a) & set(b))


def common_elements3(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return ''.join(str(result))

def common_elements4(list1, list2):
    return [element for element in list1 if element in list2]

#print 'Common values:', ', '.join(map(str, common_elements1([1, 2, 4, 8], [1, 4, 9])))
print common_elements1([1, 2, 4, 8], [1, 4, 9])
print common_elements2([1, 2, 4, 8], [1, 4, 9])
print common_elements3([1, 2, 4, 8], [1, 4, 9])