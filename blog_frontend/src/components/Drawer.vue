<template>
    <div>
        <v-navigation-drawer 
            :class="{ 'mini-mode': mini }"
            :rail="mini"
            :permanent="mini"
        >
            <VBtn v-if="mini" @click="toggleMiniVariant" color="black" icon="mdi-arrow-expand-right" variant="plain"> </VBtn>
            <VBtn v-if="!mini" @click="toggleMiniVariant" color="black" icon="mdi-arrow-expand-left" variant="plain"> </VBtn>
            
            <slot v-if="!mini"></slot>
        </v-navigation-drawer>
    </div>
    
</template>

<script setup>
    import { ref } from 'vue'

    const mini = ref(false)

    const toggleMiniVariant = () => {
        mini.value = !mini.value
    }

</script>

<style scoped>
.mini-mode {
    border: none !important;
    width: 40px !important;
}
</style>