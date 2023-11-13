<template>
  <VContainer fluid fill-height class="flex-column">
	
		<Header :store="store" @button-clicked="handleButtonClicked"></Header>
		
		<VMain class="main-content">
            <SignIn :dialog="showSignInDialog" @update:dialog="showSignInDialog = $event"></SignIn>
			<RouterView></RouterView>
		</VMain>
			
		<Footer v-if="hasFooter"></Footer>
			
  </VContainer >
</template>

<script setup>
    import { ref, computed, onMounted } from 'vue';
    import {useRoute, useRouter} from "vue-router";
    import Header from '@/components/Header.vue';
	import Footer from '@/components/Footer.vue';
    import {useStore} from '@/stores/useStore.js';
    import SignIn from '@/views/SignIn.vue';

    const router = useRouter();
    const route = useRoute();

    const store = useStore();
    const showSignInDialog = ref(false);
	const hasFooter = ref(false);
    // const hasFooter = computed(() => {
	// 	let regex = /^\/article\/\d+$/;
	// 	return regex.test(route.path);
	// });
    const hasDrawer = computed(() => {
		let regex = /^\/article\/\d+$/;
		return regex.test(route.path);
	});

    onMounted(() => {
		console.log('hasDrawer:', hasDrawer.value);
		console.log('hasFooter:', hasFooter.value);
	});

    const handleButtonClicked = (button) => {
        switch (button) {
            case 'home':
                router.push({ name: 'Home' });
                break;
            case 'search':
                console.log('search');
                break;
            case 'star':
                console.log('star');
                break;
            case 'setting':
                console.log('setting');
                break; 
            case 'account':
                showSignInDialog.value = true;
                break;
        }
    };

</script>

<style scoped>
	.main-content {
		margin-top: 15px;
	}

</style>