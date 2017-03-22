def selection_sort(items):
    """
    Sort list of items in ascending order using selection sort algorithm
    """
    for step in len(range(items)):
        # find the location of the smallest items in items[step]
        location_of_smallest = step
        for location in range(step, len(items)):
            # determine location of smallest
            if(items[location] < items[step]):
                location_of_smallest = location
        # Exchange items[step] with items[location_of_smallest]
        temporary = items[step]
        items[step] = items[location_of_smallest]
        items[location_of_smallest] = temporary