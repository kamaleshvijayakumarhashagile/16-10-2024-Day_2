<template>
    <div class="app-container">
        <div class="navbar">
            <img src="../assets/HashAgile.png" alt="Logo" class="logo" />
            <div class="navbar-right">
                <button class="view-details-button" :disabled="!hasUploadedData" @click="goToDisplayPage">View Details</button>
            </div>
        </div>
        <div class="form-container">
            <h1>AI Recruiter</h1>
            <div v-if="submissionStatus" class="message">{{ submissionStatus }}</div>
            <form @submit.prevent="handleSubmit">
                <div class="form-group">
                    <label for="resume">Upload Resume:</label>
                    <input type="file" @change="handleFileUpload" id="resume" accept=".pdf,.doc,.docx" required />
                </div>
                <div class="form-group">
                    <label for="firstName">First Name:</label>
                    <input v-model="formData.firstName" type="text" id="firstName" placeholder="Enter your Firstname" required />
                </div>
                <div class="form-group">
                    <label for="lastName">Last Name:</label>
                    <input v-model="formData.lastName" type="text" id="lastName" placeholder="Enter your Lastname" required />
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input v-model="formData.email" type="email" id="email" placeholder="Enter your email" required />
                </div>
                <div class="form-group">
                    <label for="phone">Phone:</label>
                    <input v-model="formData.phone" type="tel" id="phone" maxlength="12" placeholder="Enter your phone number" required />
                </div>
                <div class="form-group">
                    <label for="address">Address:</label>
                    <input v-model="formData.address" type="text" id="address" placeholder="Enter your address" required />
                </div>
                <div class="form-group">
                    <label for="experience">Experience:</label>
                    <input v-model="formData.experience" type="text" id="experience" placeholder="Enter your experience" />
                </div>
                <div class="form-group">
                    <label for="noticePeriod">Notice Period:</label>
                    <input v-model="formData.noticePeriod" type="text" id="noticePeriod" placeholder="Enter your notice period" />
                </div>
                <div class="form-group">
                    <label for="education">Education:</label>
                    <input v-model="formData.education" type="text" id="education" placeholder="Enter your education" />
                </div>
                <div class="form-group">
                    <label for="yearPassing">Year of Passing:</label>
                    <input v-model="formData.yearPassing" type="number" id="yearPassing" placeholder="Enter your year of passing" />
                </div>
                <div class="form-group">
                    <label for="college">College:</label>
                    <input v-model="formData.college" type="text" id="college" placeholder="Enter your college name" />
                </div>
                <div class="form-group">
                    <label for="technicalSkills">Technical Skills:</label>
                    <textarea v-model="formData.technicalSkills" id="technicalSkills" placeholder="Enter your technical skills" required></textarea>
                </div>
                <div class="form-group">
                    <label for="internExperience">Internship Experience:</label>
                    <input v-model="formData.internExperience" type="number" id="internExperience" placeholder="Enter your internship experience in months" />
                </div>
                <div class="form-group">
                    <label for="position">Position:</label>
                    <input v-model="formData.position" type="text" id="position" placeholder="Enter your desired position" required />
                </div>
                <div class="form-group">
                    <label for="companyName">Company Name:</label>
                    <input v-model="formData.companyName" type="text" id="companyName" placeholder="Enter your current company name" required />
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: 'UploadPage',
    data() {
        return {
            formData: {
                firstName: '',
                lastName: '',
                email: '',
                phone: '',
                address: '',
                experience: '',
                noticePeriod: '',
                education: '',
                yearPassing: '',
                college: '',
                technicalSkills: '',
                internshipExperience: '',
                position: '',
                companyName: '',
                resume: '',
            },
            submissionStatus: '',
            hasUploadedData: false,
        };
    },
    methods: {
        handleFileUpload(event) {
    this.formData.resume = event.target.files[0]; 
},

        
        async handleSubmit() {
            const url = `http://localhost:5000/upload_details`;

            const formData = new FormData();
            for (const key in this.formData) {
                console.log(key, this.formData[key])  //check
                formData.append(key, this.formData[key]); 
            }

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    body: formData,
                });

                if (response.ok) {
                    this.submissionStatus = 'Resume submitted successfully!';
                    this.resetForm();
                    this.hasUploadedData = true;
                } else {
                    const errorData = await response.json();
                    this.submissionStatus = errorData.message || 'Error submitting resume. Please try again. No file error ';
                }

            } catch (error) {
                console.error('Submission error:', error);
                this.submissionStatus = 'Error submitting resume. Please try again.';
            }
        },
        resetForm() {
            this.formData = {
                resume: null,
                firstName: '',
                lastName: '',
                email: '',
                phone: '',
                address: '',
                internshipExperience: '',
                experience: '',
                position: '',
                technicalSkills: '',
                companyName: '',
                noticePeriod: '',
                education: '',
                college: '',
                yearPassing: '',
            };
            this.submissionStatus = '';
        },
        goToDisplayPage() {
            this.$router.push({ name: 'DisplayPage' });
        },
    },
};
</script>

<style scoped>
.app-container {
    text-align: center;
    padding: 0;
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
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

.navbar-right {
    display: flex;
    justify-content: flex-end;
    width: 100%;
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

.logo {
    width: 200px;
    margin-right: 20px;
}

.form-container {
    
    max-width: 600px;
    margin: auto;
    padding-bottom: 40px;
    margin-top: 10%;
}

form {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 10px;
    align-items: center;
}

.form-group {
    display: contents;
}

input,
select, 
textarea {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    grid-column: 2 / 3;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.message {
    margin-top: 20px;
    font-size: 1.2em;
    color: green;
}
</style>
