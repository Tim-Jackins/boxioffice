
//import SeatingGrid from './SeatingGrid.js';
//import Cart from './Cart.js';


class SeatSelector extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      error: null,
      isLoaded: false,
      seatLayout: JSON.parse(props.seatDataJSON).seatLayout,
      dates: JSON.parse(props.dateDataJSON),
      seatData: JSON.parse(props.seatDataJSON),
      userPicksDate: null,
      userPicksSelectedTickets: null,
      tempCart: null,
      showId: props.showId
    }

    this.showDates = this.showDates.bind(this)
    this.fillSeatChart = this.fillSeatChart.bind(this)
    this.handleDateSubmit = this.handleDateSubmit.bind(this)
    this.handleBookNow = this.handleBookNow.bind(this)
    this.updateCart = this.updateCart.bind(this);
  }

  componentDidMount() {
    const mutationObserver = new MutationObserver(this.updateCart);
    mutationObserver.observe(document.body, {
      subtree: true,
      attributeOldValue: false
    });

    this.setState({
      isLoaded: true
    })
  }

  showDates() {
    const dates = this.state.dates
    let htmlDates = []
    

    for (let date = 0; date < dates.length; date++) {
      htmlDates.push(React.createElement('option', {}, dates[date]['date']))
    }

    return htmlDates;
  }

  fillSeatChart(chosenDate) {
    const dates = this.state.dates

    for (let index = 0; index < dates.length; index++) {
      if (dates[index]['date'] === chosenDate) {
        const defaultSeatData = this.state.seatData
        dates[index]['soldSeats'][0].forEach(function(soldSeat) {
          //console.log(soldSeat)

          let AreaDesc = soldSeat['AreaDesc']
          let PhyRowId = soldSeat['PhyRowId']
          let SeatNumber = soldSeat['SeatNumber']

          defaultSeatData['seatLayout']['colAreas']['objArea'].forEach(function(section) {
            if (section['AreaDesc'] === AreaDesc) {
              section['objRow'].forEach(function(row) {
                if (row['PhyRowId'] === PhyRowId) {
                  row['objSeat'][SeatNumber+1]['SeatStatus'] = "1"
                  console.log(row['objSeat'][SeatNumber+1]['SeatStatus'])
                }
              })
            }
          })
          console.log(defaultSeatData)
        })
        this.setState( {seatData: defaultSeatData} )
      }
    }
    
  }

  handleDateSubmit(event) {
    const selectElement = document.getElementById('datePickSelect')
    let date = selectElement.options[selectElement.options.selectedIndex].text
    console.log('User picked ' + date)
    this.setState({
      userPicksDate: date
    })
    this.fillSeatChart(date)
    event.preventDefault()
  }

  handleBookNow() {
    let rawTickets = document.getElementsByClassName('current-selected')

    if (rawTickets.length === 0) {
      alert('You haven\'t selected any tickets!')
      console.log('')
    } else {
      let tempCartInfo = []

      for (let i = 0; i < rawTickets.length; i++) {
        tempCartInfo.push({
          id: rawTickets[i].id,
          desc: rawTickets[i].getAttribute(['area-desc']),
          cost: rawTickets[i].getAttribute(['cost'])
        })
      }

      console.log('User picked seats:');
      console.log(tempCartInfo);
      this.setState({
        userPicksSelectedTickets: tempCartInfo
      })
    }
  }


  updateCart() {
    let tempCartInfo = [];

    let rawTickets = document.getElementsByClassName('current-selected');

    for (let i = 0; i < rawTickets.length; i++) {
      tempCartInfo.push({
        id: rawTickets[i].id,
        desc: rawTickets[i].getAttribute(['area-desc']),
        cost: rawTickets[i].getAttribute(['cost'])
      });
    }
    this.setState({ tempCart: tempCartInfo })
  }


  render() {
    //const { data, numberOfSeats } = this.state
    const {
      error,
      isLoaded,
      seatLayout,
      dates,
      seatData,
      userPicksDate,
      userPicksSelectedTickets,
      tempCart,
      showId
    } = this.state

    if (error) {
      return React.createElement("div", null, "Error: ", error.message);
    } else if (!isLoaded) {
      return React.createElement("div", null, "Loading...")
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
      }, "Get tickets")))))))
    }
    else if (!userPicksSelectedTickets) {
      return React.createElement("div", {
        className: "container"
      }, React.createElement("div", {
        className: "row"
      }, React.createElement("div", {
        className: "col-md-8 order-md-1"
      }, React.createElement(SeatingGrid, {
        seatingData: seatData
      })), React.createElement("div", {
        className: "col-md-4 order-md-2 "
      }, React.createElement(Cart, null),
        
          React.createElement('input', {
            type: 'hidden',
            name: 'showId',
            value: showId}),

          React.createElement('input', {
            type: 'hidden',
            name: 'Seats',
            value: JSON.stringify(tempCart)}),
          
          React.createElement('input', {
            type: 'hidden',
            name: 'Date',
            value: userPicksDate}),

          React.createElement("button", {
            className: "btn btn-success"
            //onClick: this.handleBookNow
          }, "Make booking")
      )));
    }

  }
}
