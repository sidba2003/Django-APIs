<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            Django-APIs
        </div>

        <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#Authors-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Authors</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#Books-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Books</button>
            </li>
        </ul>
        <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" id="Authors-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0"><Authors/></div>
            <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">To show the Books</div>
        </div>
    </div>
</template>

<script>
import Authors from './components/Authors.vue'

export default {
    components: {
        Authors
    }
}
</script>
