<template>
    <div class="container pt-3">
        <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addAuthor">
            <i class="bi bi-plus"></i> Add Author
        </button>

        <!-- Modal -->
        <div class="modal fade" id="addAuthor" tabindex="-1" aria-labelledby="addAuthorLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addAuthorLabel">Add Author</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input v-model="newAuthor.name" type="text" class="form-control" id="name">
                        </div>
                        <div class="mb-3">
                            <label for="age" class="form-label">Age</label>
                            <input v-model="newAuthor.age" type="number" class="form-control" id="age">
                        </div>  
                        <div class="mb-3">
                            <label for="active" class="form-label">Active (true / false)</label>
                            <input v-model="newAuthor.active" type="text" class="form-control">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Close
                        </button>
                        <button type="button" class="btn btn-primary" @click="createAuthor" data-bs-dismiss="modal">
                            Save
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <AuthorTable 
            :authors="authors"
            @delete-author="deleteAuthor"
        />
    </div>
</template>

<script>
    import AuthorTable from './AuthorTable.vue'

    const baseUrl = 'http://localhost:8000'

    export default {
        components: {
            AuthorTable
        },
        data() {
            return {
                title: 'Computer Inventory',
                authors: [],
                newAuthor: {
                    name: '',
                    age: 0,
                    active: ''
                }
            }
        },
        async mounted() {
            const response = await fetch(`${baseUrl}/api/authors/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            const data = await response.json()
            this.authors = data.authors;
        },
        methods: {
            async deleteAuthor(author) {
                if (confirm(`Are you sure you want to delete author '${author.name}'?`)) {
                    const response = await fetch(`${baseUrl}${author.api}`, {
                        method: 'DELETE',
                    })

                    if (response.ok)
                        this.newAuthorsDataSet = await fetch(`${baseUrl}/api/authors/`, {
                            method: 'GET',
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        }).then(response => response.json())

                        this.authors = this.newAuthorsDataSet.authors
                }
            },
            async createAuthor() {
                // Convert active to boolean
                if (this.newAuthor.active == 'true') {
                    this.newAuthor.active = true
                } else {
                    this.newAuthor.active = false
                }

                const response = await fetch(`${baseUrl}/api/authors/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.newAuthor)
                })
                const newAuthor = await response.json()
                this.authors.push(newAuthor)
            }
        }
    }
</script>

<style scoped>
</style>