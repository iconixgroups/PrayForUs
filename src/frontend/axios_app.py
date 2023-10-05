```python
import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const registerUser = async (userDetails) => {
  try {
    const response = await axios.post(`${API_URL}/register`, userDetails);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const searchChurch = async (location) => {
  try {
    const response = await axios.get(`${API_URL}/churches?location=${location}`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const bookService = async (bookingDetails) => {
  try {
    const response = await axios.post(`${API_URL}/bookings`, bookingDetails);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const registerEvent = async (eventDetails) => {
  try {
    const response = await axios.post(`${API_URL}/events`, eventDetails);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const makeDonation = async (donationDetails) => {
  try {
    const response = await axios.post(`${API_URL}/donations`, donationDetails);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const registerAdmin = async (adminDetails) => {
  try {
    const response = await axios.post(`${API_URL}/admins`, adminDetails);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
```