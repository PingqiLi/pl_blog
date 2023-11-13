<template>
    <v-dialog v-model="localDialog">
        <VRow
            class="fill-height"
            justify="center"
            align-content="space-evenly"
        >     
            <VCol cols="12" md="4"> 
                <VCard class="signin-form">
                    <v-toolbar
                        dark
                        prominent
                    >
                        <v-toolbar-title><div class="text-h5">Sign In</div></v-toolbar-title>

                        <v-spacer></v-spacer>

                        <v-btn icon @click="localDialog=false">
                            <v-icon>mdi-close</v-icon>
                        </v-btn>
                    </v-toolbar>

                    <VCardTitle class="title">
                        
                    </VCardTitle>
                    <VCardText>
                        <v-form fast-fail>
                        <v-text-field v-model="email" label="Username or Email"></v-text-field>
                        <v-text-field v-model="password" label="Password" type="password"></v-text-field>
                        <router-link :to="{name: 'ResetPassword'}" class="text-body-2 font-weight-regular">
                            <span>Forgot Password?</span>
                        </router-link>
                        <v-btn type="submit" color="#F5F5F5" block @click.prevent="submitForm">Sign in</v-btn>
                        </v-form>
                        <div class="mt-2">
                        <router-link :to="{name: 'SignUp'}" class="text-body-2" @click="localDialog=false">
                            Don't have an account? Sign Up
                        </router-link>
                        </div>
                    </VCardText>
                </VCard>
            </VCol>
        </VRow>
    </v-dialog>

</template>
<script setup>
import axios from 'axios';
import { ref, watch } from 'vue'
import { isAuthenticated } from '@/utils/cookie.js';

const props = defineProps(['dialog']);
const emit = defineEmits(['update:dialog']);
const localDialog = ref(props.dialog);
// const store = useStore();
const email = ref('');
const password = ref('');


watch(
    () => props.dialog,
    (newVal) => {
        localDialog.value = newVal;
    }
);

watch(
    localDialog,
    (newVal) => {
        emit('update:dialog', newVal);
    }
);

const submitForm = () => {
    console.log('Data being sent:', 
        'email: ', email.value, 
        'password:', password.value);
    axios.post('/api/token/', 
        {
            email: email.value,
            password: password.value,
        }, 
        {
            headers: {
                'Content-Type': 'application/json',
            }
        })
    .then(function(response) {
        console.log('Response:', response);

        // close the dialog
        localDialog.value = false;
    })
    .catch(function (error) {
        console.error('Error during authentication:', error);
    })
    .finally(function() {
        setTimeout(() => {
            // console.log('Request completed:', isAuthenticated());
        }, 1000); // Delay of 1 second
    });
};

   
</script>

<style scoped>
.signin-form {
    margin-top: 5%;
}
.title {
    margin-top: 1%;  
    margin-bottom: 3%;  
}
</style>