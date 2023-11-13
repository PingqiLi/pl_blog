<template>
    <div class="article">
        <VCard
            :class="{'article-content': hasDrawer, 'article-content-mobile': !hasDrawer}"
            width="100%"
            variant="flat"
        >
            <VCardItem id="article-content">
                <VCardTitle v-if="name != 'xs'">
                    <span class="article-title"> {{ article.title }} </span>
                </VCardTitle>
                <VCardTitle v-if="name == 'xs'">
                    <span class="article-title-mobile"> {{ article.title }} </span> 
                </VCardTitle>
                <VCardSubtitle id="info">
                    {{ article && article.author ? article.author.username : '' }} · {{ formattedTime(article.created) }}
                </VCardSubtitle>
                <VDivider></VDivider>
                <VCardText>
                    <MdPreview :editorId="id" :modelValue="article.body" preview-theme="github"/>
                </VCardText>
            </VCardItem>
        </VCard>
    </div>

    <Drawer v-if="hasDrawer">
        <MdCatalog class="toc" :editorId="id" :scrollElement="scrollElement" />
    </Drawer>
    <VToolbar v-if="!hasDrawer" c   lass="tool-bar" density="compact">
        <VBtn icon @click="toggleDrawer">
            <VIcon>mdi-menu</VIcon>
        </VBtn>
    </VToolbar>
    
</template>

<script setup>
    import Drawer from "@/components/Drawer.vue";
    import { MdPreview, MdCatalog } from 'md-editor-v3';
    import 'md-editor-v3/lib/preview.css';
    import {ref, onMounted, onBeforeMount} from "vue";
    import {useRoute} from "vue-router";
    import axios from "axios";
    import { useDisplay } from 'vuetify'
    import { computed } from "vue";

    const route = useRoute();
    const { name } = useDisplay();
    const id = 'preview-only';
    const article = ref({});
    const scrollElement = document.documentElement;
    

    const hasDrawer = computed(() => {
        console.log("Display name:", name.value, "Has drawer:", name.value != "xs");
       if (name.value == "xs") return false;
       else if (name.value != "xs") return true;
    });

    const get_article_content = async () => {
        axios
            .get('/api/article/' + route.params.id)
            .then(response => {
                console.log("response:", response.data);
                article.value = response.data;
                console.log("author:", article.value.author.username);
            })
            .catch(error => {
                console.error("ERROR:", error);
            });
    }
    
    onBeforeMount(() => {
       console.log("Display name:", name.value)
    });
    onMounted(async () => await get_article_content());
    
    // watch(() => hasDrawer, () => console.log("hasDrawer:", hasDrawer.value));
        
</script>

<style scoped>
    .toc{
        margin-top: 4%;
        padding-left: 10%;
    }
    .tool-bar {
        display: flex;
        justify-content: center;
        align-items: center; 
        flex-wrap: wrap;
        margin-bottom: 20px;
    }
    .article {
        display: flex;
        justify-content: center;
        align-items: center; 
        flex-wrap: wrap;
    }
    .article-content {
        margin-top: -10px;
        margin-bottom: 20px;
        align-content: left;
        margin-right: 2.6%;
    }
    .article-content-mobile {
        margin-top: -10px;
        margin-bottom: 20px;
        align-content: left;
    }
    .article-title {
        font-family: Georgia, Arial, sans-serif;
        font-size: 35px;
        font-weight: bolder;
        color: black;
        padding: 5px 0 5px 0;
        white-space: normal; /* Allows the text to wrap to the next line */
        overflow: hidden; /* Keeps the overflow content hidden */
        text-overflow: ellipsis; /* Adds ellipsis when the text overflows */
        line-height: 1.5em; /* Height of each line */
        max-height: 3em; /* Maximum height of the container, equivalent to two lines */
        display: -webkit-box;
        -webkit-line-clamp: 2; /* Limit the number of lines to 2 */
        -webkit-box-orient: vertical;
    }

    .article-title-mobile {
        font-family: Georgia, Arial, sans-serif;
        font-size:  18px;
        font-weight: bolder;
        color: black;
        padding: 5px 0 5px 0;
        margin-bottom: 5%;
        white-space: normal; /* Allows the text to wrap to the next line */
        overflow: hidden; /* Keeps the overflow content hidden */
        text-overflow: ellipsis; /* Adds ellipsis when the text overflows */
        line-height: 1.5em; /* Height of each line */
        max-height: 4.6em; /* Maximum height of the container, equivalent to two lines */
        display: -webkit-box;
        -webkit-line-clamp: 3; /* Limit the number of lines to 2 */
        -webkit-box-orient: vertical;
    }

  
</style>
