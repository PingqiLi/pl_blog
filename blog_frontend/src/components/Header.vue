<template>
    <v-app-bar 
        flat
        class="bar-with-divider"
    >   
        <template v-slot:prepend>
            <VImg :src="favicon" alt="Website favicon" aspect-ratio="1"></VImg>
        </template>

        <VAppBarTitle>   
            <span class="app-icon" @click="buttonClicked('home')">PL Blog</span>
        </VAppBarTitle>
        
        <VBtn 
            icon class="button"
            @click="buttonClicked('search')"
        >
            <VIcon>mdi-magnify</VIcon>
        </VBtn>

        <VBtn 
            icon class="button"
            @click="buttonClicked('star')"
        >
            <VIcon>mdi-star</VIcon>
        </VBtn>

        <VBtn
            icon class="button"
            @click="buttonClicked('setting')"
        >
            <VIcon>mdi-cog</VIcon>
        </VBtn>
        
        <VBtn
            v-if="!isAuth"
            icon class="button"
            @click="buttonClicked('account')"
        >
            <VIcon>mdi-account</VIcon>
        </VBtn>

        <template v-slot:append>
            <div v-if="isAuth">
                <v-menu>
                    <template v-slot:activator="{ props }">
                        <v-btn 
                            v-if="hasIcon === false"
                            v-bind="props"
                            class="rounded-circle usericon" 
                            size="42"
                            @click="buttonClicked('user')"
                        >
                            <span class="username-text">{{ name }}</span>
                        </v-btn>
                    </template>

                    <v-card min-width="300">
                        <v-list>
                        <v-list-item
                            prepend-avatar="https://cdn.vuetifyjs.com/images/john.jpg"
                            title="John Leider"
                            subtitle="Founder of Vuetify"
                        >
                            <template v-slot:append>
                            <v-btn
                                variant="text"
                                :class="fav ? 'text-red' : ''"
                                icon="mdi-heart"
                                @click="fav = !fav"
                            ></v-btn>
                            </template>
                        </v-list-item>
                        </v-list>

                        <v-divider></v-divider>

                        <v-list>
                        <v-list-item>
                            <v-switch
                            v-model="message"
                            color="purple"
                            label="Enable messages"
                            hide-details
                            ></v-switch>
                        </v-list-item>

                        <v-list-item>
                            <v-switch
                            v-model="hints"
                            color="purple"
                            label="Enable hints"
                            hide-details
                            ></v-switch>
                        </v-list-item>
                        </v-list>

                        <v-card-actions>
                        <v-spacer></v-spacer>

                        <v-btn
                            variant="text"
                            @click="menu = false"
                        >
                            Cancel
                        </v-btn>
                        <v-btn
                            color="primary"
                            variant="text"
                            @click="menu = false"
                        >
                            Save
                        </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-menu>
            </div>
           
        </template>
    </v-app-bar>

</template>

<script setup>
    import { ref } from 'vue';
    import { isAuthenticated } from '@/utils/cookie';
    import faviconSrc from '/favicon.ico'

    const favicon = ref(faviconSrc);
    const name = 'PL';
    const hasIcon = false;
    const isAuth = isAuthenticated();
    console.log('isAuthenticated:', isAuth);

    const emits = defineEmits(['button-clicked']);
    const buttonClicked = (button) => {
        emits('button-clicked', button);
    }

</script>


<style scoped>
    .rounded-circle {
        display: flex;
        align-items: center;
        justify-content: center;
        color:#ffffff;
        background-color: #1d7ad1;
    }
    .username-text {
        font-size: 1.1rem;
        font-weight: 500;
        color: #ffffff;
        text-decoration: none;
    }
    .bar-with-divider{
        border-bottom: 1px solid rgba(0, 0, 0, 0.15);
    }
    .app-icon {
        display: inline-block;
        font-size: 1.5rem;
        font-weight: 500;
        color: #2d2727;
        text-decoration: none;
    }
    .usericon {
        margin-left: 10px;
        margin-right: 5px;
    }
    .button {
        margin-right: 0.2%;
    }
    .search-field {
        flex-grow: 1; /* Make the search field take up the remaining space */
        max-width: 400px; /* Or another max-width based on your design */
    }
    
    .header-end {
        color: #000000;
        border-width: 1px;
    }
</style>
