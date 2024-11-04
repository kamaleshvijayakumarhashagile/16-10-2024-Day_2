<template>
    <div class="navbar">
        <img src="../assets/HashAgile.png" alt="Logo" class="logo" />
    </div>
    <div class="signup-container">
        <h2 class="signup-title">SIGN UP / REGISTER</h2>
        <form @submit.prevent="handleSignup">
            <div class="form-group">
                <label for="email">Email:</label>
                <input v-model="formData.email" placeholder="Enter email" type="email" id="email" required />
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input v-model="formData.password" placeholder="Enter your password" type="password" id="password" required />
            </div>
            <button type="submit" class="green-button">Sign Up</button>
            <p class="login-prompt">Already have an account? <router-link to="/login">Login</router-link></p>
        </form>
        <div v-if="message" class="error-message">{{ message }}</div>
    </div>
</template>

<script>
import { registerUser } from '../api';
import { useToast } from 'vue-toastification';

export default {
    name: "SignupPage",
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

        


        async handleSignup() {
            const toast = useToast(); // Access toast instance
            try {
                const response = await registerUser(this.formData);
                toast.success(response.data.message || 'Registration successful!'); // Use toast for success
                this.$router.push('/login'); // Redirect after signup
            } catch (error) {
                this.message = error.response?.data?.message || 'An error occurred. Please try again.';
                toast.error(this.message); // Use toast for error
            }
        }
    }
};
</script>

<style scoped>
.signup-container {
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

.signup-title {
    margin-bottom: 20px;
    font-size: 28px;
    font-weight: bold;
    color: #000000;
    letter-spacing: 1px;
}

.form-group {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    width: 100%;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #555;
}

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
}

.green-button:hover {
    background-color: #218838;
}

.login-prompt {
    margin-top: 10px;
    color: #555;
    font-size: 14px;
}

.error-message {
    color: red;
    margin-top: 10px;
    font-weight: bold;
}
</style>
