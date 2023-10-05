```python
import cypress from 'cypress'

cypress.config('baseUrl', 'http://localhost:3000')

cypress.describe('PrayForUs.in', function() {
  it('Landing Page', function() {
    cypress.visit('/')
    cypress.get('#signUpButton').should('be.visible')
    cypress.get('#searchBar').should('be.visible')
  })

  it('User Registration', function() {
    cypress.visit('/register')
    cypress.get('input[name="firstName"]').type('Test')
    cypress.get('input[name="lastName"]').type('User')
    cypress.get('input[name="email"]').type('testuser@gmail.com')
    cypress.get('input[name="password"]').type('password')
    cypress.get('button[type="submit"]').click()
    cypress.get('#paymentForm').should('be.visible')
  })

  it('User Profile', function() {
    cypress.visit('/profile')
    cypress.get('.favorites').should('be.visible')
    cypress.get('.bookings').should('be.visible')
    cypress.get('.donations').should('be.visible')
    cypress.get('.events').should('be.visible')
  })

  it('Church Listings', function() {
    cypress.visit('/churches')
    cypress.get('.church-details').should('be.visible')
  })

  it('Service Booking', function() {
    cypress.visit('/bookings')
    cypress.get('#bookingForm').should('be.visible')
  })

  it('Events Registration', function() {
    cypress.visit('/events')
    cypress.get('#eventForm').should('be.visible')
  })

  it('Donations', function() {
    cypress.visit('/donations')
    cypress.get('#donationForm').should('be.visible')
  })

  it('Church Admin Registration', function() {
    cypress.visit('/admin/register')
    cypress.get('#adminForm').should('be.visible')
  })
})
```