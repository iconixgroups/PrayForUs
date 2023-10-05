import React from 'react';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      userDetails: {},
      churchDetails: [],
      paymentDetails: {},
      bookingDetails: {},
      eventDetails: {},
      donationDetails: {},
      adminDetails: {},
    };
  }

  registerUser = (userDetails) => {
    axios.post('/api/register', userDetails)
      .then(response => {
        this.setState({ userDetails: response.data });
      })
      .catch(error => {
        console.error('Error during user registration:', error);
      });
  }

  searchChurch = (location) => {
    axios.get(`/api/churches?location=${location}`)
      .then(response => {
        this.setState({ churchDetails: response.data });
      })
      .catch(error => {
        console.error('Error during church search:', error);
      });
  }

  bookService = (bookingDetails) => {
    axios.post('/api/book', bookingDetails)
      .then(response => {
        this.setState({ bookingDetails: response.data });
      })
      .catch(error => {
        console.error('Error during service booking:', error);
      });
  }

  registerEvent = (eventDetails) => {
    axios.post('/api/event', eventDetails)
      .then(response => {
        this.setState({ eventDetails: response.data });
      })
      .catch(error => {
        console.error('Error during event registration:', error);
      });
  }

  makeDonation = (donationDetails) => {
    axios.post('/api/donate', donationDetails)
      .then(response => {
        this.setState({ donationDetails: response.data });
      })
      .catch(error => {
        console.error('Error during donation:', error);
      });
  }

  registerAdmin = (adminDetails) => {
    axios.post('/api/admin', adminDetails)
      .then(response => {
        this.setState({ adminDetails: response.data });
      })
      .catch(error => {
        console.error('Error during admin registration:', error);
      });
  }

  render() {
    return (
      <div>
        {/* Insert your components here */}
      </div>
    );
  }
}

export default App;