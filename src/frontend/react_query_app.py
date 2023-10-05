```python
import { useQuery } from 'react-query'
import axios from 'axios'

# Fetching user details
const fetchUserDetails = async () => {
  const { data } = await axios.get('/api/userDetails')
  return data
}

# Fetching church details
const fetchChurchDetails = async () => {
  const { data } = await axios.get('/api/churchDetails')
  return data
}

# Fetching booking details
const fetchBookingDetails = async () => {
  const { data } = await axios.get('/api/bookingDetails')
  return data
}

# Fetching event details
const fetchEventDetails = async () => {
  const { data } = await axios.get('/api/eventDetails')
  return data
}

# Fetching donation details
const fetchDonationDetails = async () => {
  const { data } = await axios.get('/api/donationDetails')
  return data
}

# Fetching admin details
const fetchAdminDetails = async () => {
  const { data } = await axios.get('/api/adminDetails')
  return data
}

# Using react-query to manage data and state
export function useUserDetails() {
  return useQuery('userDetails', fetchUserDetails)
}

export function useChurchDetails() {
  return useQuery('churchDetails', fetchChurchDetails)
}

export function useBookingDetails() {
  return useQuery('bookingDetails', fetchBookingDetails)
}

export function useEventDetails() {
  return useQuery('eventDetails', fetchEventDetails)
}

export function useDonationDetails() {
  return useQuery('donationDetails', fetchDonationDetails)
}

export function useAdminDetails() {
  return useQuery('adminDetails', fetchAdminDetails)
}
```