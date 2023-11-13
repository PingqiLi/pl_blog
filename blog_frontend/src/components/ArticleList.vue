<template>
    <div v-for="article in items"
            :key="article.id"
            id="articles"
            class="articles-list"
    >   
        <VCard 
            class="article-info" 
            variant="elevated"
            width="80%"
        >   

            <VImg v-if="name == 'xs'"
                :width="img_size.iWidth"
                aspect-ratio="16/9"
                cover
                src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
            ></VImg>

            <VRow>
                <VCol v-if="name != 'xs'" cols="4" xl="1" lg="2" md="3" sm="3" offset-lg="1" offset-md="1" offset-sm="-1">
                    <div class="img-container">
                        <VImg
                            :width="img_size.iWidth"
                            :height="img_size.iWidth"
                            cover
                            src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
                        ></VImg>
                    </div>
                </VCol>
                <VCol>
                    <VCardTitle>
                        <VRow>
                            <VCol cols="12">
                                <router-link v-if="name != 'xs'" class="article-link" :to="{ name: 'ArticleDetail', params: { id: article.id }}">
                                    <span class="article-title"> {{ article.title }} </span>
                                </router-link>
                                <router-link v-if="name == 'xs'" class="article-link" :to="{ name: 'ArticleDetail', params: { id: article.id }}">
                                    <span class="article-title-mobile"> {{ article.title }} </span>
                                </router-link>
                        
                            </VCol>
                        </VRow>
                    </VCardTitle>
                    <VCardText>
                        <VRow>
                            <VCol cols="12">
                                <div class="d-inline"> 
                                    <VIcon size="small">mdi-pencil</VIcon> 
                                    {{article.author.username}} 
                                    <VIcon size="small">mdi-calendar</VIcon> 
                                    {{ formattedTime(article.created) }} 
                                </div>
                            </VCol>
                        </VRow>
                    </VCardText>
                    <VCardText>
                        {{ article.abstract }}
                    </VCardText>
                    <VCardText cols="8" xl="9" lg="9" md="9" sm="9" xs="10">
                        <VRow>
                            <VCol cols="12">    
                                <VChip
                                    class="category ma-1"
                                    size="small"
                                >
                                    {{ article.category.title }}
                                </VChip>
                    
                                <VChip
                                    class="tag ma-1"
                                    v-for="tag in article.tags"
                                    :key="tag"
                                    size="small"
                                >
                                    {{ tag }}
                                </VChip>
                            </VCol>
                        </VRow>
                    </VCardText>
                </VCol>
            </VRow>
        </VCard>
    </div>
    

</template>

<script setup>
    import { ref, onMounted, onUnmounted, computed } from 'vue'
    import { useDisplay } from 'vuetify'
    import axios from "axios"


    const items = ref([]);
    const nextUrl = ref('/api/article/');
    const loading = ref(false);
    const fullyLoaded = ref(false);
    const { width, height, name } = useDisplay();
    
    
    const img_size = computed(() => {
        switch (name.value) {
            case 'xs': 
                return {iWidth: width.value - 80}
            case 'sm':
                return {iWidth: 160}
            case 'md': 
                return {iWidth: 180}
            case 'lg': 
                return {iWidth: 190}
            case 'xl': 
                return {iWidth: 200}
            case 'xxl': 
                return {iWidth: 200}
        }
    })


    const scrollHandler = () => { 
        const scrollHeight = document.documentElement.scrollHeight; 
        const scrollTop = document.documentElement.scrollTop; 
        const clientHeight = document.documentElement.clientHeight; 
        const distance = scrollHeight - scrollTop - clientHeight; 
        if (distance <= height.value / 2) { 
            load(); 
        } 
    }
    
    const load = async () => {
        console.log("url:", nextUrl.value)
        if (loading.value) return;
        loading.value = true; 
        if (!nextUrl.value) {
            fullyLoaded.value = true; 
            return;
        }
        axios.get(nextUrl.value)
            .then(response => {
                if (response.data.next) {
                    nextUrl.value = response.data.next;
                } else {
                    nextUrl.value = null;
                }
                items.value.push(... response.data.results);
                loading.value = false;
            })
            .catch(error => {
                console.error("ERROR:", error);
                loading.value = false;
            });
    }

    onMounted(() => {
        load();
        window.addEventListener('scroll', scrollHandler, false)
    });
    onUnmounted(() => {
        window.removeEventListener('scroll', scrollHandler, false)
    });
    
</script>

<style scoped>
.img-container {
    padding: 10px 0px 0px 0px;
    position: relative;
}

.articles-list {
    display: flex;
    justify-content: center;
    align-items: center; 
    flex-wrap: wrap;
}

.article-info {
    margin-bottom: 20px;
    padding: 20px 20px 20px 20px;
    align-content: center;
}
.article-link {
  text-decoration: none;
}

.article-title {
    font-family: Georgia, Arial, sans-serif;
    font-size: 26px;
    font-weight: bolder;
    color: black;
    padding: 5px 0 5px 0;
    margin-bottom: 1%;
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
    font-size: 20px;
    font-weight: bolder;
    color: black;
    padding: 3px 0 3px 0;
    margin-bottom: 5%;
    white-space: normal; /* Allows the text to wrap to the next line */
    overflow: hidden; /* Keeps the overflow content hidden */
    text-overflow: ellipsis; /* Adds ellipsis when the text overflows */
    line-height: 1.2em; /* Height of each line */
    max-height: 2.4em; /* Maximum height of the container, equivalent to two lines */
    display: -webkit-box;
    -webkit-line-clamp: 2; /* Limit the number of lines to 2 */
    -webkit-box-orient: vertical;
}

.category {
    color: rgb(43, 104, 174);
    margin-right: 4px;  
    margin-bottom: 2px;
}

.tag {
    margin-right: 4px;  
    margin-bottom: 2px;
}
</style>
