<template>
    <div class="container pt-3">
        <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addBook">
            <i class="bi bi-plus"></i> Add Book
        </button>

        <!-- Add Book Modal -->
        <div class="modal fade" id="addBook" tabindex="-1" aria-labelledby="addBookLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <!-- Modal content -->
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addBookLabel">Add Book</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <!-- Form fields for new book -->
                        <div class="mb-3">
                            <label for="title" class="form-label">Title</label>
                            <input v-model="newBook.title" type="text" class="form-control" id="title">
                        </div>
                        <div class="mb-3">
                            <label for="description" class="form-label">Description</label>
                            <textarea v-model="newBook.description" class="form-control" id="description"></textarea>
                        </div>
                        <div class="mb-3" v-if="authors.length > 0">
                            <label for="authors" class="form-label">Authors</label>
                            <select v-model="newBook.authors" multiple class="form-control" id="authors">
                                <option v-for="author in authors" :value="author.id" :key="author.id">{{ author.name }}</option>
                            </select>
                        </div>
                        <div v-else>
                            Loading authors...
                        </div>
                        <div class="mb-3">
                            <label for="published" class="form-label">Published Date</label>
                            <input v-model="newBook.published" type="date" class="form-control" id="published">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <!-- Modal footer -->
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Close
                        </button>
                        <button type="button" class="btn btn-primary" @click="createBook" data-bs-dismiss="modal">
                            Save
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Book Table Component -->
        <BookTable 
            :books="books"
            @delete-book="deleteBook"
        />
    </div>
</template>

<script>
import BookTable from './BookTable.vue'

const baseUrl = 'http://localhost:8000'

export default {
    components: {
        BookTable
    },
    data() {
        return {
            books: [],
            authors: [],
            newBook: {
                title: '',
                description: '',
                authors: [],
                published: ''
            }
        }
    },
    async mounted() {
        // Fetch books
        const response = await fetch(`${baseUrl}/api/books/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        const data = await response.json()
        this.books = data.books;

        const modal = document.getElementById('addBook');
        modal.addEventListener('shown.bs.modal', this.updateAuthors);
    },
    methods: {
        async deleteBook(book) {
            if (confirm(`Are you sure you want to delete book '${book.title}'?`)) {
                const response = await fetch(`${baseUrl}${book.api}`, {
                    method: 'DELETE',
                })

                if (response.ok) {
                    // Refresh the book list after deletion
                    const newBooksData = await fetch(`${baseUrl}/api/books/`, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    }).then(response => response.json())

                    this.books = newBooksData.books
                }
            }
        },
        async createBook() {
            // Prepare authors data
            const authorsIds = this.newBook.authors.map(Number);

            const response = await fetch(`${baseUrl}/api/books/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    title: this.newBook.title,
                    description: this.newBook.description,
                    authors: authorsIds,
                    published: this.newBook.published
                })
            })
            const newBook = await response.json()
            this.books.push(newBook)

            // Reset newBook
            this.newBook.title = ''
            this.newBook.description = ''
            this.newBook.authors = []
            this.newBook.published = ''
        },
        async updateAuthors(){
            try {
                // Fetch authors for selection in new book form
                const authorsResponse = await fetch(`${baseUrl}/api/authors/`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                if (!authorsResponse.ok) {
                    throw new Error('Failed to fetch authors');
                }
                const authorsData = await authorsResponse.json()
                this.authors = authorsData.authors;
            } catch (error) {
                console.error(error);
                alert('Error fetching authors');
            }
        }
    }
}
</script>

<style scoped>
</style>
