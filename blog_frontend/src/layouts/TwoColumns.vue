<template>
    <v-layout class="rounded rounded-md">
        <v-app-bar 
            flat
            class="bar-with-divider"
        >
            <VAppBarTitle>PL Blog</VAppBarTitle>
            
            <VBtn 
                icon class="search"
                @click="buttonClicked('search')"
            >
                <VIcon>mdi-magnify</VIcon>
            </VBtn>

            <VBtn 
                icon class="star"
                @click="buttonClicked('star')"
            >
                <VIcon>mdi-star</VIcon>
            </VBtn>

            <VBtn 
                icon class="setting"
                @click="buttonClicked('setting')"
            >
                <VIcon>mdi-cog</VIcon>
            </VBtn>

            <template v-slot:append>
                <v-avatar 
                    v-if="hasIcon === false"
                    color="purple"
                    size="36"
                    @click="buttonClicked('profile')"
                >
                    <span class="text-lg-h7">{{ name }}</span>
                </v-avatar>
                <v-avatar 
                    v-else
                    size="36"
                    @click="buttonClicked('profile')"
                >
                    <v-img
                        :width="300"
                        aspect-ratio="16/9"
                        cover
                        src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
                    >
                    </v-img>
                </v-avatar>

            </template>
        </v-app-bar>
  
        <v-navigation-drawer class="toc">
            <v-list>
                <v-list-item title="Drawer left"></v-list-item>
            </v-list>
        </v-navigation-drawer>
  
  
        <v-main class="d-flex" style="min-height: 100%;">
            <RouterView></RouterView>
        </v-main>
    </v-layout>
</template>

<script setup>
    import { ref } from 'vue';
    
    const name = 'PL';
    const hasIcon = false;
    const loggedIn = false;

    const emits = defineEmits(['button-clicked']);
    const buttonClicked = (button) => {
        emits('button-clicked', button);
    }
</script>

<style scoped>
    .bar-with-divider {
        border-bottom: 1px solid rgba(0, 0, 0, 0.12);
    }
    .setting {
        margin-right: 12px;
    }
    .toc {
        width: 15%;
    }

</style>