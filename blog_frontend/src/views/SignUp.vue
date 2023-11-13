<template>
	<v-container
	  class="fill-height d-flex justify-center align-center"
	  fluid
	  style="background-image: url('/signup_background.jpg'); background-size: cover;"
	>

	  <v-card class="pa-5 signup-form rounded-xl" style="background: rgba(255, 255, 255, 0.9);">
		<v-card-title class="text-h4 card-title">Welcome</v-card-title>
		<v-card-text>
		  <v-form ref="form" v-model="valid">
			<v-text-field 
				class="field" 
				label="Username" 
				required 
				:rules="usernameRules"
				v-model="username"
			></v-text-field>
			<v-text-field 
				class="field" 
				label="Email" 
				required 
				:rules="emailRules"
				v-model="email"
				></v-text-field>
			<v-text-field
				class="field"
				label="Password"
				type="password"
				required
				:rules="passwordRules"
				v-model="password"
			></v-text-field>
			<v-text-field
				class="field"
				label="Confirm Password"
				type="password"
				required
				:rules="confirmPasswordRules"
			></v-text-field>
			<v-row>
				<v-col cols="4" offset="4">
					<v-btn
						class="submit-button"
						prepend-icon="mdi-upload"
						rounded="lg"
						flat
						size="large"
						type="submit"
						style="background: rgba(255, 255, 255, 0.85);"
						@click="submitForm"
					>
						Submit
					</v-btn>
				</v-col>
			</v-row>
			
		  </v-form>
		</v-card-text>
	  </v-card>
	  
	</v-container>
  </template>
  
<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const valid = ref(true);
const form = ref(null);
const username = ref('');
const email = ref('');
const password = ref('');

const usernameRules = [
	(v) => !!v || 'Username is required',
	(v) => v.length >= 8 || 'Username must be at least 8 characters',
	(v) => v.length <= 16 || 'Username must be less than 16 characters.'
      
];

const emailRules = [
	(v) => !!v || 'Email is required',
	(v) => /.+@.+/.test(v) || 'Email must be valid',
];

const passwordRules = [
	(v) => !!v || 'Password is required',
	(v) => v.length >= 8 || 'Password must be at least 8 characters',
	(v) => {
		let count = 0;
		if (/[A-Z]/.test(v)) count++;
		if (/[a-z]/.test(v)) count++;
		if (/[0-9]/.test(v)) count++;
		if (/\W|_/.test(v)) count++;
		if (count >= 3) return true;
		return 'Password must include at least one capital letter.';
	},
];

const confirmPasswordRules = [
	(v) => !!v || 'Confirming password is required',
	(v) => v === password.value || 'Passwords must match',
];

const submitForm = async () => {
    if (form.value.validate()) {
        console.log('Data being sent:', 
            'username: ', username.value, 
            'email:', email.value,
            'password:', password.value);

        try {
            const response = await axios.post('/api/user/', {
                username: username.value,
                email: email.value,
                password: password.value,
            }, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            
            console.log(response);
            router.push({ name: 'Home' });
            return Promise.resolve('Success');
        } catch (error) {
            console.error('Error:', error);
            alert('Error creating account.');
            return Promise.reject(error);
        } finally {
            console.log('Request completed');
        }
    }
};


</script>
  
<style scoped>

.card-title {
	margin-bottom: 5%;
}

.signup-form {
	width: 100%;
	max-width: 500px;
}

.field {
	margin-bottom: 15px;
}

.submit-button {
	width: 100%;
}

</style>
  