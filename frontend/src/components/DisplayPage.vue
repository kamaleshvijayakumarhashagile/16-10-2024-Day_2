<template>
    <div>
        <div class="navbar">
            <img src="../assets/HashAgile.png" alt="Logo" class="logo" />
            <div class="navbar-right">
                <button class="view-details-button" :disabled="!hasUploadedData" @click="goToDisplayPage">View Details</button>
            </div>
        </div>

        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
        <div v-else-if="candidate" class="candidate-card">
            <h1>Welcome to HashAgile!</h1>
            <h3>{{ candidate.first_name }} {{ candidate.last_name }}</h3>
            <div class="candidate-info">
                <div class="info-row">
                    <p><strong>Email:</strong> {{ candidate.email }}</p>
                </div>
                <div class="info-row">
                    <p><strong>Phone:</strong> {{ candidate.phone_number }}</p>
                </div>
                <div class="info-row">
                    <p><strong>Experience:</strong> {{ candidate.experience }}</p>
                </div>
                <div class="info-row">
                    <p><strong>Notice Period:</strong> {{ candidate.notice_period }}</p>
                </div>
                <div class="info-row">
                    <p><strong>Education:</strong> {{ candidate.education }}</p>
                </div>
                <div class="info-row">
                    <p><strong>Year of Passing:</strong> {{ candidate.year_of_passing }}</p>
                </div>
                <div class="info-row">
                    <p><strong>College:</strong> {{ candidate.college }}</p>
                </div>
                <div class="info-row">
                    <p><strong>Location:</strong> {{ candidate.address }}</p>
                </div>
                <div class="info-row">
                    <p><strong>Skills:</strong> {{ candidate.technical_skills }}</p>
                </div>
                <div class="info-row">
                    <p><strong>Intern Experience:</strong> {{ candidate.internship_experience_in_months }} months</p>
                </div>
                <div class="info-row" v-if="candidate.resume">
                    <p>
                        <strong>Resume:</strong>
                        <a :href="`http://localhost:5000/resumes/${candidate.resume}`" download>Download Resume</a>
                    </p>
                </div>
            </div>
        </div>

        <div v-else class="candidate-card no-details">
            <h1>Sorry! You need to upload your details first.</h1>
            <button @click="goToUploadPage" class="upload-button">Go to Upload Page</button>
        </div>
    </div>
</template>

<script>
export default {
    name: "DisplayPage",
    data() {
        return {
            candidate: null,
            errorMessage: null,
        };
    },
    async created() {
        const email = localStorage.getItem('email'); 
        if (!email) {
            this.errorMessage = "No email found. Please log in.";
            return;
        }
        try {
            const response = await fetch(`http://localhost:5000/api/user_details/${email}`);
            if (response.ok) {
                this.candidate = await response.json(); 
            } else {
                this.errorMessage = "Error fetching candidate data. Please try again.";
                console.error("Error fetching candidate data");
            }
        } catch (error) {
            this.errorMessage = "Error connecting to the API. Please check your network.";
            console.error("Error connecting to the API", error);
        }
    },
    methods: {
        goToUploadPage() {
            this.$router.push({ name: 'UploadPage' });
        }
    }
};
</script>

<style scoped>
body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    margin: 0;
}


.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 30px;
    background-color: #f8f9fa;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    z-index: 1000;
}

.logo {
    width: 150px;
}

.candidate-card {
    border-radius: 8px;
    padding: 30px;
    margin: 100px auto;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    background-color: #fff;
    max-width: 500px;
    text-align: left;
}

.candidate-card h1 {
    margin: 0;
    color: #007bff;
}

.candidate-card h3 {
    margin: 10px 0;
    color: #333;
}

.candidate-info {
    margin-top: 20px; /* Add margin for spacing */
}

.info-row {
    margin-bottom: 15px; /* Add space between each row */
}

.info-row p {
    margin: 0; /* Remove default margin */
    color: #555;
}

.error-message {
    color: red;
    text-align: center;
    margin: 20px 0;
}

.no-details {
    text-align: center;
}

.upload-button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.upload-button:hover {
    background-color: #0056b3;
}

.view-details-button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-left: auto;
    margin-right: 10%;
}
.view-details-button:hover {
    background-color: #0056b3;
}
</style>
