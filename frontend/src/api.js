import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Adjust this if necessary

export const registerUser = (userData) => {
    const formData = new FormData();
    
    // Append each field from userData to the FormData object
    for (const key in userData) {
        if (userData[key] !== null) {
            formData.append(key, userData[key]);
        }
    }

    return axios.post(`${API_URL}/register`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
};

export const loginUser = (credentials) => {
    return axios.post(`${API_URL}/login`, credentials);
};
