
//import SeatingGrid from './SeatingGrid.js';
//import Cart from './Cart.js';


class SeatSelector extends React.Component {
  constructor(props) {
    super(props)
    console.log("testing")
    console.log(document)
    this.state = {
      error: null,
      isLoaded: false,
      seatLayout: props.seatDataJSON.seatLayout,
      dates: props.dateDataJSON.dates,
      seatData: props.seatDataJSON,
      userPicksDate: null,
      userPicksSelectedTickets: null
    };
    this.showDates = this.showDates.bind(this);
    this.handleDateSubmit = this.handleDateSubmit.bind(this);
    this.handleBookNow = this.handleBookNow.bind(this);

  }

  componentDidMount() {
    this.setState({
      isLoaded: true
    })
  }

  showDates() {
    const dates = this.state.dates
    let htmlDates = []

    for (let date = 0; date < dates.length; date++) {
      htmlDates.push(React.React.createElement('option', {}, dates[date]))
    }

    return htmlDates;
  }

  handleDateSubmit(event) {
    const selectElement = document.getElementById('datePickSelect');
    let date = selectElement.options[selectElement.options.selectedIndex].text;
    console.log('User picked ' + date);
    this.setState({
      userPicksDate: date
    });
    event.preventDefault();
  }

  handleBookNow() {
    let rawTickets = document.getElementsByClassName('current-selected');

    if (rawTickets.length === 0) {
      alert('You haven\'t selected any tickets!');
      console.log('');
    } else {
      let tempCartInfo = [];

      for (let i = 0; i < rawTickets.length; i++) {
        tempCartInfo.push({
          id: rawTickets[i].id,
          desc: rawTickets[i].getAttribute(['area-desc']),
          cost: rawTickets[i].getAttribute(['cost'])
        });
      }

      console.log('User picked seats:');
      console.log(tempCartInfo);
      this.setState({
        userPicksSelectedTickets: tempCartInfo
      });
    }
  }

  render() {
    //const { data, numberOfSeats } = this.state
    const {
      error,
      isLoaded,
      //seatLayout,
      //intMaxSeatId,
      //intMinSeatId,
      //dates,
      seatData,
      userPicksDate,
      userPicksSelectedTickets
    } = this.state;

    if (true) {
      return React.createElement("span", null, "Here's the thing")
    }
    else if (error) {
      return React.createElement("div", null, "Error: ", error.message);
    } else if (!isLoaded) {
      return React.createElement("div", null, "Loading...");
    } else if (!userPicksDate) {
      
      return React.createElement("div", {
        className: "col-50"
      }, React.createElement("div", {
        className: "mx-auto",
        style: {
          width: 'auto'
        }
      }, React.createElement("div", {
        className: "container"
      }, React.createElement("form", {
        onSubmit: this.handleDateSubmit
      }, React.createElement("label", {
        htmlFor: "datePickSelect"
      }, "Dates and times"), React.createElement("div", {
        className: "row"
      }, React.createElement("div", {
        className: "col-sm-8"
      }, React.createElement("select", {
        className: "form-control",
        id: "datePickSelect"
      }, this.showDates())), React.createElement("div", {
        className: "col-sm-4"
      }, React.createElement("button", {
        type: "submit",
        className: "btn btn-primary"
      }, "Get tickets")))))));
    
    }
  }

}

const checkoutDomContainer = document.querySelector('#checkout_app');
ReactDOM.render(React.createElement(SeatSelector, Window.props), checkoutDomContainer);
