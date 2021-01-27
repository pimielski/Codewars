# TODO: complete this class

class PaginationHelper:
        
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return int(self.item_count() / self.items_per_page) + (self.item_count() % self.items_per_page != 0)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, pages_index):
        
        if pages_index == 0:
            return self.items_per_page
        if pages_index in range(1, self.page_count()):
            if self.item_count() % self.items_per_page != 0 and pages_index + 1 == self.page_count():
                return self.item_count() % self.items_per_page
            else: return self.items_per_page
        else: return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        
        if item_index not in range(0,self.item_count()):
            return -1
        else:
            return int(item_index / self.items_per_page)

collection = range(1, 15)
helper = PaginationHelper(collection, 5)

print('item count:',helper.item_count())
print('page count:',helper.page_count())
print('page item count:',helper.page_item_count(2))
print('page index:',helper.page_index(8))



