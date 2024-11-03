<template>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Title</th>
                <th scope="col">Description</th>
                <th scope="col">Authors</th>
                <th scope="col">Published</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(book, index) in books" :key="book.id">
                <th scope="row">{{ index + 1 }}</th>
                <td>
                    {{ book.title }}
                </td>
                <td>
                    {{ book.description }}
                </td>
                <td>
                    <ul>
                        <li v-for="author in book.authors" :key="author.id">
                            {{ author.name }}
                            <strong v-if="author.is_lead_author"> (Lead Author)</strong>
                        </li>
                    </ul>
                </td>
                <td>
                    {{ book.published }}
                </td>
                <td>
                    <button 
                        class="btn btn-sm btn-primary me-2" data-bs-toggle="modal" data-bs-target="#editBook"
                        @click="selectBook(book)"
                    >
                        <i class="bi bi-pencil-square"></i>
                    </button>
                    <button 
                        class="btn btn-sm btn-danger"
                        @click="$emit('delete-book', book)"
                    >
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>

    <!-- Edit Book Modal -->
    <div class="modal fade" id="editBook" tabindex="-1" aria-labelledby="editBookLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <!-- Modal content -->
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="editBookLabel">Edit Book</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <!-- Form fields for editing book -->
                    <div class="mb-3">
                        <label for="editTitle" class="form-label">Title</label>
                        <input v-model="bookEditData.title" type="text" class="form-control" id="editTitle">
                    </div>
                    <div class="mb-3">
                        <label for="editDescription" class="form-label">Description</label>
                        <textarea v-model="bookEditData.description" class="form-control" id="editDescription"></textarea>
                    </div>
                    <div class="mb-3" v-if="authors.length > 0">
                        <label class="form-label">Authors</label>
                        <div v-for="author in authors" :key="author.id" class="form-check">
                            <input class="form-check-input" type="checkbox" :value="author.id" v-model="bookEditData.selectedAuthors">
                            <label class="form-check-label">{{ author.name }}</label>
                            <div class="form-check ms-3">
                                <input class="form-check-input" type="checkbox" :value="author.id" v-model="bookEditData.leadAuthors" :disabled="!bookEditData.selectedAuthors.includes(author.id)">
                                <label class="form-check-label">Lead Author</label>
                            </div>
                        </div>
                    </div>
                    <div v-else>
                        Loading authors...
                    </div>
                    <div class="mb-3">
                        <label for="editPublished" class="form-label">Published Date</label>
                        <input v-model="bookEditData.published" type="date" class="form-control" id="editPublished">
                    </div>
                </div>
                <div class="modal-footer">
                    <!-- Modal footer -->
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                        Close
                    </button>
                    <button type="button" class="btn btn-primary" @click="editBook" data-bs-dismiss="modal">
                        Save
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
const baseUrl = 'http://localhost:8000'

export default {
    data() {
        return {
            selectedBook: null,
            bookEditData: {
                title: '',
                description: '',
                selectedAuthors: [],
                leadAuthors: [],
                published: ''
            },
            authors: []
        }
    },
    emits: ['delete-book'],
    props: {
        books: {
            type: Array,
            required: true
        }
    },
    async mounted() {
        // Fetch authors for selection in edit book form
        const authorsResponse = await fetch(`${baseUrl}/api/authors/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        const authorsData = await authorsResponse.json()
        this.authors = authorsData.authors;
    },
    methods: {
        async editBook() {
            // Prepare authors data
            const authorsData = this.bookEditData.selectedAuthors.map(authorId => {
                return {
                    id: authorId,
                    is_lead_author: this.bookEditData.leadAuthors.includes(authorId)
                };
            });

            const response = await fetch(`${baseUrl}${this.selectedBook.api}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    title: this.bookEditData.title,
                    description: this.bookEditData.description,
                    authors: authorsData,
                    published: this.bookEditData.published
                })
            });

            if (!response.ok) {
                alert('Failed to edit book!');
            } else {
                // Update the selectedBook with new data
                const updatedBook = await response.json();
                // Update the book in the books array
                Object.assign(this.selectedBook, updatedBook);
            }

            // Unselect the selected book
            this.selectedBook = null;
        },
        selectBook(book) {
            this.selectedBook = book;
            this.bookEditData.title = book.title;
            this.bookEditData.description = book.description;
            this.bookEditData.selectedAuthors = book.authors.map(author => author.id);
            this.bookEditData.leadAuthors = book.authors
                .filter(author => author.is_lead_author)
                .map(author => author.id);
            this.bookEditData.published = book.published;
        }
    }
}
</script>

<style scoped>
td, th {
    vertical-align: middle;
}
</style>
