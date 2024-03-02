class Book:
    def __init__(self, id, title, author, genre, publisher, pub_year, status = "Available"):
        self.id = int(id)
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.pub_year = pub_year
        self.status = status 

class AVLNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None
        self.height = 1  # Mặc định khi node được tạo, chiều cao là 1
    
class AVLTree:

# Các phương thức khởi tạo cấu trúc của một cây AVLTree cơ bản với chức năng thêm / xóa 
    
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def check_id_exists(self, node, id):
        if node is None:
            return False
        if id == node.book.id:
            return True
        elif id < node.book.id:
            return self.check_id_exists(node.left, id)
        else:
            return self.check_id_exists(node.right, id)

    def _insert(self, node, key, book):
        if not node:
            return AVLNode(book)
        if key < node.book.id:
            node.left = self._insert(node.left, key, book)
        elif key > node.book.id:
            node.right = self._insert(node.right, key, book)
        else:
            return node  

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Check for imbalance and perform rotations
        if balance > 1 and key < node.left.book.id:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.book.id:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.book.id:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.book.id:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, book):
        if book.id <= 0 or not isinstance(book.id, int):
            return
        self.root = self._insert(self.root, book.id, book)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.book.id:
            node.left = self._delete(node.left, key)
        elif key > node.book.id:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._find_min(node.right)
            node.book = temp.book
            node.right = self._delete(node.right, temp.book.id)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Balance the tree
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

# Các phương thức của cây phục vụ cho việc sắp xếp sách và lấy kết quả sách được sắp xếp theo inoder_traversal

    def _inorder_traversal_collect(self, node, books):
        if node:
            self._inorder_traversal_collect(node.left, books)
            books.append(node.book)
            self._inorder_traversal_collect(node.right, books)

    def collect_books(self):
        books = []
        self._inorder_traversal_collect(self.root, books)
        return books

# Các phương thức của cây phục vụ việc tìm kiếm sách dựa vào từ khóa (id / author hoặc genre)

    def _search_books_by_author_or_genre(self, node, keyword, found_books):
        if node is not None:
            self._search_books_by_author_or_genre(node.left, keyword, found_books)
            
            if keyword.lower() in node.book.author.lower() or keyword.lower() in node.book.genre.lower():
                found_books.append(node.book)

            self._search_books_by_author_or_genre(node.right, keyword, found_books)

    def search_books_by_author_or_genre(self, keyword):
        found_books = []
        self._search_books_by_author_or_genre(self.root, keyword, found_books)
        return found_books

    def _search_books_by_id(self, node, keyword, found_books):
        if node is not None:
            self._search_books_by_id(node.left, keyword, found_books)
            
            if keyword == node.book.id:
                found_books.append(node.book)

            self._search_books_by_id(node.right, keyword, found_books)

    def search_books_by_id(self, keyword):
        found_books = []
        self._search_books_by_id(self.root, keyword, found_books)
        return found_books

# Các phương thức của cây phục vụ việc mượn / trả sách dựa trên từ khóa book_id

    def _find_book(self, node, book_id):
        if node is None:
            return None
        if book_id < node.book.id:
            return self._find_book(node.left, book_id)
        elif book_id > node.book.id:
            return self._find_book(node.right, book_id)
        else:
            return node
        
    def borrow_book(self, book_id):
        node = self._find_book(self.root, book_id)
        if node is not None and node.book.status == "Available":
            node.book.status = "Unavailable"
            return True
        elif node is not None:
            return False
        else:
            return False

    def return_book(self, book_id):
        node = self._find_book(self.root, book_id)
        if node is not None and node.book.status == "Unavailable":
            node.book.status = "Available"
            return True
        elif node is not None:
            return False
        else:
            return False