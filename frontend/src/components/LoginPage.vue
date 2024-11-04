<template>
    <div class="navbar">
        <img src="../assets/HashAgile.png" alt="Logo" class="logo" />
    </div>
    <div class="login-container">
        <h2 class="login-title">Login Page</h2>
        <form @submit.prevent="handleLogin">
            <div class="form-group">
                <label for="email">Email:</label>
                <input
                    v-model="formData.email"
                    placeholder="Enter your email"
                    type="text"
                    id="email"
                    required
                />
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input
                    v-model="formData.password"
                    placeholder="Enter your password"
                    type="password"
                    id="password"
                    required
                />
            </div>
            <button type="submit" class="green-button">Login</button>
            <p class="signup-prompt">
                Don't have an account? <router-link to="/signup">Sign Up</router-link>
            </p>
        </form>
        <div v-if="message" class="error-message">{{ message }}</div>
    </div>
</template>

<script>
import { loginUser } from '../api'; // Ensure this function is defined to call your login endpoint
import { useToast } from 'vue-toastification';

export default {
    name: 'LoginPage',
    data() {
        return {
            formData: {
                email: '',
                password: ''
            },
            message: ''
        };
    },
    methods: {

async handleLogin() {
    const toast = useToast();
    try {
        const response = await loginUser(this.formData);
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('email', this.formData.email); // Store email

        // Fetch user details
        const userDetailsResponse = await fetch(`http://localhost:5000/api/user_details/${this.formData.email}`);
        
        if (userDetailsResponse.ok) {
            const userDetails = await userDetailsResponse.json();
            // Save user details to local storage or Vuex store as needed
            localStorage.setItem('userDetails', JSON.stringify(userDetails));
            this.$router.push('/display'); // Redirect to display page if details exist
        } else {
            // If user details do not exist, redirect to upload page
            this.$router.push('/upload'); 
        }

        toast.success('Login successful!');
    } catch (error) {
        this.message = error.response?.data?.message || 'Invalid credentials. Please try again.';
        toast.error(this.message);
    }
}


    }
};
</script>

<style>
/* General Styles */
body {
    font-family: 'Arial', sans-serif;
    background-color: #f0f2f5;
    margin: 0;
    padding: 0;
}

/* Navbar Styles */
.navbar {
    display: flex;
    justify-content: flex-start;
    padding: 30px;
    background-color: #f8f9fa;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Login Container Styles */
.login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 50px;
    padding: 40px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    width: 400px;
    margin-left: auto;
    margin-right: auto;
}

.login-title {
    margin-bottom: 20px;
    font-size: 28px;
    font-weight: bold;
    color: #333;
    letter-spacing: 1px;
}

/* Form Group Styles */
.form-group {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    width: 100%;
}

/* Label Styles */
label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #555;
}

/* Input Styles */
input {
    padding: 12px;
    border: 1px solid #ced4da;
    border-radius: 4px;
    width: 100%;
    font-size: 16px;
}

input:focus {
    border-color: #28a745;
    outline: none;
}

/* Button Styles */
.green-button {
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 12px 15px;
    cursor: pointer;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    transition: background-color 0.3s;
}

.green-button:hover {
    background-color: #218838;
}

/* Signup Prompt Styles */
.signup-prompt {
    margin-top: 10px; 
    color: #555; 
    font-size: 14px; 
}

/* Error Message Styles */
.error-message {
    color: red; 
    margin-top: 10px; 
    font-weight: bold; 
}
</style>
