<template>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Age</th>
                <th scope="col">Active</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(author, index) in authors">
                <th scope="row">{{ index+1 }}</th>
                <td>
                    {{ author.name }}
                </td>
                <td>
                    <span class="badge bg-secondary">
                        {{ author.age }} years
                    </span>
                </td>
                <td>
                    <i>{{ author.active }}</i>
                </td>
                <td>
                    <button 
                        class="btn btn-sm btn-primary me-2" data-bs-toggle="modal" data-bs-target="#editAuthor"
                        @click="selectAuthor(author)"
                    >
                        <i class="bi bi-pencil-square"></i>
                    </button>
                    <button 
                        class="btn btn-sm btn-danger"
                        @click="$emit('delete-author', author)"
                    >
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>

    <!-- Modal -->
    <div class="modal fade" id="editAuthor" tabindex="-1" aria-labelledby="addAuthorLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="addAuthorLabel">Edit Author</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input v-model="authorEditData.name" type="text" class="form-control" id="name">
                    </div>
                    <div class="mb-3">
                        <label for="age" class="form-label">Age</label>
                        <input v-model="authorEditData.age" type="number" class="form-control" id="age">
                    </div>  
                    <div class="mb-3">
                        <label for="active" class="form-label">Active (true / false)</label>
                        <input v-model="authorEditData.active" type="text" class="form-control">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                        Close
                    </button>
                    <button type="button" class="btn btn-primary" @click="editAuthor" data-bs-dismiss="modal">
                        Save
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    const baseUrl = 'http://localhost:8000/'

    export default {
        data(){
            return{
                selectedAuthor: null,
                authorEditData: {
                    name: null,
                    age: null,
                    active: null
                }
            }
        },
        emits: ['delete-author'],
        props: {
            authors: {
                type: Array,
                required: true
            }
        },
        methods: {
            async editAuthor() {
                const response = await fetch(`${baseUrl}${this.selectedAuthor.api}`,{
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.authorEditData)
                })

                if (!response.ok){
                    alert('Failed to edit author!')
                } else {
                    this.selectedAuthor.name = this.authorEditData.name
                    this.selectedAuthor.age = this.authorEditData.age
                    this.selectedAuthor.active = this.authorEditData.active
                }
                
                // unseleting the selected author
                this.selectedAuthor = null;
            },

            selectAuthor(author){
                this.selectedAuthor = author
            }
        }
    }
</script>

<style scoped>
    td, th {
        vertical-align: middle;
    }
</style>