import React from 'react'
import { useRouter } from 'next/router'
import axios from './axios_app.py'
import { UserSchema, ChurchSchema, BookingSchema, EventSchema, DonationSchema, AdminSchema } from '../schemas.py'

export default function App() {
  const router = useRouter()

  const registerUser = async (userDetails) => {
    try {
      const response = await axios.post('/api/register', UserSchema.validate(userDetails))
      router.push('/profile')
    } catch (error) {
      console.error(error)
    }
  }

  const searchChurch = async (location) => {
    try {
      const response = await axios.get('/api/churches', { params: { location } })
      return ChurchSchema.validate(response.data)
    } catch (error) {
      console.error(error)
    }
  }

  const bookService = async (bookingDetails) => {
    try {
      const response = await axios.post('/api/bookings', BookingSchema.validate(bookingDetails))
      return response.data
    } catch (error) {
      console.error(error)
    }
  }

  const registerEvent = async (eventDetails) => {
    try {
      const response = await axios.post('/api/events', EventSchema.validate(eventDetails))
      return response.data
    } catch (error) {
      console.error(error)
    }
  }

  const makeDonation = async (donationDetails) => {
    try {
      const response = await axios.post('/api/donations', DonationSchema.validate(donationDetails))
      return response.data
    } catch (error) {
      console.error(error)
    }
  }

  const registerAdmin = async (adminDetails) => {
    try {
      const response = await axios.post('/api/admins', AdminSchema.validate(adminDetails))
      return response.data
    } catch (error) {
      console.error(error)
    }
  }

  return (
    <div>
      {/* Insert your UI components here */}
    </div>
  )
}