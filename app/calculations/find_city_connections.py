from copy import deepcopy

def connect_cities(locus_city, other_cities):

  def flatten(list2d):
    accum = []
    for l in list2d:
      accum += l
    return accum

  def id_not_in(list2d, _id):
    for l in list2d:
      if _id in l:
        return False
    return True

  def add_citynames(levels, cities):
    accum = []
    for l in levels:
      inner = []
      for item in l:
        city = next((c for c in cities if c['id'] == item), None)
        inner.append({
          'name': city['name'],
          'id': city['id'],
        })
      accum.append(inner)
    return accum

  def get_next_level(cities, ids):
    accum = []
    for _id in ids:
      city = next((c for c in cities if c['id'] == _id), None)
      accum.append(city['connections'])
    print('flat accumulator', flatten(accum))
    return list(set(flatten(accum)))


  def build(city, cities):
    city_copy = deepcopy(city)
    levels = []
    for n in range(4):
      if n == 0:
        levels.append(city_copy['connections'])
      else:
        next_level = get_next_level(cities, levels[n - 1])
        filtered_next_level = [_id for _id in next_level if id_not_in(levels, _id) and city_copy['id'] != _id]
        levels.append(filtered_next_level)
    with_citynames = add_citynames(levels, cities)
    city_copy['connections'] = with_citynames
    return city_copy
 
  return build(locus_city, other_cities)