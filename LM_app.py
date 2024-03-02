import tkinter as tk
from tkinter import messagebox
from avl_tree import Book, AVLTree
import json

class Library_Management:

    # Hàm kích hoạt giao diện   
    def __init__(self, root):
        self.root = root
        self.root.title("Book Inventory")     
        self.book_tree = AVLTree()
        self.load_books_from_json() 
        self.create_widgets()

    # Hàm truy cập dữ liệu file "Book_data.json"
    def load_books_from_json(self):
        file_path = 'Book_data.json' 
        with open(file_path, 'r') as file:
            books_list = json.load(file)
            for book_info in books_list:
                book = Book(book_info['id'], book_info['title'], book_info['author'],
                            book_info['genre'], book_info['publisher'], book_info['pub_year'],
                            book_info['status'])
                self.book_tree.insert(book)

    # Hàm cập nhật dữ liệu file "Book_data.json"
    def save_books_to_json(self):
        file_path = 'Book_data.json' 
        books = self.book_tree.collect_books()
        books_list = [book.__dict__ for book in books]
        with open(file_path, 'w') as file:
            json.dump(books_list, file, indent=4)

    # Hàm thiết kế các thành phần giao diện
    def create_widgets(self):
        for i in range(20):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        self.label_id = tk.Label(self.root, text="ID:")
        self.label_id.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
        self.entry_id = tk.Entry(self.root)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

        self.label_title = tk.Label(self.root, text="Title:")
        self.label_title.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W+tk.E)
        self.entry_title = tk.Entry(self.root)
        self.entry_title.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W+tk.E)

        self.label_author = tk.Label(self.root, text="Author:")
        self.label_author.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
        self.entry_author = tk.Entry(self.root)
        self.entry_author.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

        self.label_genre = tk.Label(self.root, text="Genre:")
        self.label_genre.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W+tk.E)
        self.entry_genre = tk.Entry(self.root)
        self.entry_genre.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W+tk.E)

        self.label_publisher = tk.Label(self.root, text="Publisher:")
        self.label_publisher.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
        self.entry_publisher = tk.Entry(self.root)
        self.entry_publisher.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

        self.label_pub_year = tk.Label(self.root, text="Publication Year:")
        self.label_pub_year.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W+tk.E)
        self.entry_pub_year = tk.Entry(self.root)
        self.entry_pub_year.grid(row=4, column=3, padx=5, pady=5, sticky=tk.W+tk.E)

        self.button_add = tk.Button(self.root, text="Add Book", command=self.add_book, borderwidth=8, highlightthickness=2)
        self.button_add.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W+tk.E)

        self.button_display = tk.Button(self.root, text="Display Books", command=self.display_books, borderwidth=8, highlightthickness=2)
        self.button_display.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

        self.button_delete = tk.Button(self.root, text="Delete Book", command=self.delete_book, borderwidth=8, highlightthickness=2)
        self.button_delete.grid(row=5, column=2, padx=5, pady=5, sticky=tk.W+tk.E)

        self.button_delete = tk.Button(self.root, text="Clear Listbox", command=self.clear_listbox, borderwidth=8, highlightthickness=2)
        self.button_delete.grid(row=5, column=3, padx=5, pady=5, sticky=tk.W+tk.E)

        self.label_search = tk.Label(self.root, text="Search by ID")
        self.label_search.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
        self.entry_search_by_id = tk.Entry(self.root)
        self.entry_search_by_id.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

        self.label_search = tk.Label(self.root, text="Search by Author or Genre:")
        self.label_search.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
        self.entry_search_by_author_or_genre = tk.Entry(self.root)
        self.entry_search_by_author_or_genre.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

        self.button_search = tk.Button(self.root, text="Search", command=self.search_books, borderwidth=8, highlightthickness=2)
        self.button_search.grid(row=6, column=2, padx=5, pady=5, sticky=tk.W+tk.E)

        self.label_search = tk.Label(self.root, text="Enter ID for borrow / return:")
        self.label_search.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
        self.entry_id_for_borrow_or_return = tk.Entry(self.root)
        self.entry_id_for_borrow_or_return.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

        self.button_search = tk.Button(self.root, text="Borrow", command=self.borrow_book, borderwidth=8, highlightthickness=2)
        self.button_search.grid(row=8, column=2, padx=5, pady=5, sticky=tk.W+tk.E)

        self.button_search = tk.Button(self.root, text="Return", command=self.return_book, borderwidth=8, highlightthickness=2)
        self.button_search.grid(row=8, column=3, padx=5, pady=5, sticky=tk.W+tk.E)

        self.listbox_books = tk.Listbox(self.root, width=100, height=30)
        self.listbox_books.grid(row=9, column=0, columnspan=4, padx=20, pady=20, sticky=tk.W+tk.E)

    # Hàm phục vụ cho việc nhập thông tin sách
    def add_book(self):
        id = self.entry_id.get().strip()
        title = self.entry_title.get().strip()
        author = self.entry_author.get().strip()
        genre = self.entry_genre.get().strip()
        publisher = self.entry_publisher.get().strip()
        pub_year = self.entry_pub_year.get().strip()

        if not id or not title or not author or not genre or not publisher or not pub_year:
            messagebox.showerror("Error", "Please enter full book info.")
            return

        try:
            id = int(id)
            pub_year = int(pub_year)
            author = str(author)
            genre = str(genre)
            publisher = str(publisher)
            if id < 0:
                messagebox.showerror("Error", "ID must be positive integer")
                return
            elif pub_year > 2024:
                messagebox.showerror("Error", "Pub_year is not valid")
                return              
            if self.book_tree.check_id_exists(self.book_tree.root, id):
                messagebox.showerror("Error", "A book with this ID already exists in the Library.")
                return
            new_book = Book(id, title, author, genre, publisher, pub_year) 
            self.book_tree.insert(new_book)  
            messagebox.showinfo("Success", "Book added successfully!")
            self.save_books_to_json()
            self.clear_entry_fields()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. ID (>0) and Publication Year must be integers.")
            self.clear_entry_fields()
    
    # Hàm hiển thị thông tin các sách có trong dữ liệu
    def display_books(self):
        self.listbox_books.delete(0, tk.END) 
        books = self.book_tree.collect_books()
        for book in books:
            self.listbox_books.insert(tk.END, f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publisher: {book.publisher}, Publication Year: {book.pub_year}, Status: {book.status}")

    # Hàm phục vụ việc tìm kiếm thông tin sách theo từ khóa (id / author hoặc genre)
    def search_books(self):
        keyword_id = self.entry_search_by_id.get().strip()
        keyword_author_or_genre = self.entry_search_by_author_or_genre.get().strip()

        if not keyword_id and not keyword_author_or_genre :
            messagebox.showerror("Error", "Please Enter Search key")
            return
        
        if keyword_id:
            try:
                keyword_id = int(keyword_id)
            except ValueError:
                messagebox.showerror("Invalid Input", "ID must be an integer.")
                return

        found_books_set = set()

        if keyword_id:
            found_books_id = self.book_tree.search_books_by_id(keyword_id)
            for book in found_books_id:
                found_books_set.add(book)

        if keyword_author_or_genre:
            found_books_author_or_genre = self.book_tree.search_books_by_author_or_genre(keyword_author_or_genre)
            for book in found_books_author_or_genre:
                found_books_set.add(book)

        self.listbox_books.delete(0, tk.END)
        if found_books_set:
            for book in sorted(found_books_set, key=lambda x: x.id): 
                self.listbox_books.insert(tk.END, f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publisher: {book.publisher}, Publication Year: {book.pub_year}, Status: {book.status}")
        else:
            messagebox.showinfo("Search Result", "No books found in the Library.")

        self.clear_entry_fields()

    # Hàm phục vụ cho việc mượn sách (Nhập từ khóa id để mượn)
    def borrow_book(self):
        book_id = self.entry_id_for_borrow_or_return.get()
        try:
            book_id = int(book_id)
            result = self.book_tree.borrow_book(book_id)
            if result:
                messagebox.showinfo("Success", f"Book ID {book_id} has been successfully borrow.")
                self.save_books_to_json()
                self.clear_entry_fields()
            else:
                self.clear_entry_fields()
                messagebox.showerror("Error", f"Book ID {book_id} is not available or does not exist in Library.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. ID must be an integer.")
            self.clear_entry_fields()

    # Hàm phục vụ cho việc trả sách (Nhập từ khóa id để trả)
    def return_book(self):
        book_id = self.entry_id_for_borrow_or_return.get()
        try:
            book_id = int(book_id)
            result = self.book_tree.return_book(book_id)
            if result:
                messagebox.showinfo("Success", f"Book ID {book_id} has been successfully returned.")
                self.save_books_to_json()   
                self.clear_entry_fields()            
            else:
                messagebox.showerror("Error", f"Book ID {book_id} was not checked out or does not exist in the Library.")
                self.clear_entry_fields()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. ID must be an integer.")
            self.clear_entry_fields()

    # Hàm phục vụ cho việc xóa sách (nhập id để xóa)
    def delete_book(self):
        book_id = self.entry_id.get().strip()
        if not book_id:
            messagebox.showerror("Error", "Please Enter ID")
            return
        try:
            book_id = int(book_id)
            if not self.book_tree.check_id_exists(self.book_tree.root, book_id):
                messagebox.showinfo("Not Found", f"Book ID {book_id} has not existed in the library.")
                self.clear_entry_fields()
                return
            self.book_tree.delete(book_id)
            messagebox.showinfo("Success", f"Book ID {book_id} has been successfully deleted.")
            self.save_books_to_json()
            self.clear_entry_fields()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. ID must be an integer.")
            self.save_books_to_json()
            self.clear_entry_fields()

    # Hàm để xóa các ô nhập phục vụ cho lần nhập mới
    def clear_entry_fields(self):
        self.entry_id.delete(0, tk.END)
        self.entry_title.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)
        self.entry_genre.delete(0, tk.END)
        self.entry_publisher.delete(0, tk.END)
        self.entry_pub_year.delete(0, tk.END)
        self.entry_search_by_id.delete(0, tk.END)
        self.entry_search_by_author_or_genre.delete(0, tk.END)
        self.entry_id_for_borrow_or_return.delete(0, tk.END)

    # Hàm xóa nội dung list box
    def clear_listbox(self):
        self.listbox_books.delete(0, tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = Library_Management(root)
    root.mainloop()