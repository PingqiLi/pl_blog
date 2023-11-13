<template>
    <div class="pagniation">
        <v-pagination
            v-if="Math.ceil(info.count / limit) > 1"
            v-model="currPage"
            :length="Math.ceil(info.count / limit)"
            total-visible="7"
            @update:model-value="handlePageChange"
        ></v-pagination>
    </div>
</template>

<script setup>
    import {ref} from "vue";
    import {useRoute, useRouter} from "vue-router";
    // const info = defineProps({
    //     count: Number,
    //     limit: Number,
    // });

    // const handlePageChange = (page) => {
    //     currPage.value = page;
    //     router.push({ query: { ...router.currentRoute.value.query, page: page } });
    // }

</script>