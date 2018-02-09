class ListUtils:
    def print_list(list_items):
        print(list_items)
    def print_one_item(list_items, index):
        if(index < len(list_items) and index >= 0):
            print(list_items[index])
        else:
            print("Index out of bounds")
    def new_item(list_items, value):
        list_items.append(value)
        return list_items
    def new_item_at_beginning(list_items, value):
        list_items = [value] + list_items
        return list_items
    def remove_item(list_items, value):
        if value in list_items:
            list_items.remove(value)
        return list_items
    def reverse_list(list_items):
        list_items.reverse()
        return locals
    def qsort(list):
        if list == []: 
            return []
        else:
            pivot = list[0]
            lesser = qsort([x for x in list[1:] if x < pivot])
            greater = qsort([x for x in list[1:] if x >= pivot])
            return lesser + [pivot] + greater
