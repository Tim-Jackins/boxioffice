
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
      displaySeatData: null,
      userPicksDate: null,
      userPicksDateIndex: null,
      userPicksSelectedTickets: null,
      tempCart: null,
      showId: props.showId
    }

    this.showDates = this.showDates.bind(this)
    //this.fillSeatChart = this.fillSeatChart.bind(this)
    this.handleDateSubmit = this.handleDateSubmit.bind(this)
    this.handleBookNow = this.handleBookNow.bind(this)
    this.checkTickets = this.checkTickets.bind(this)
    this.updateCart = this.updateCart.bind(this)
    this.goBack = this.goBack.bind(this)

  }

  componentDidMount() {
    const mutationObserver = new MutationObserver(this.updateCart);
    mutationObserver.observe(document.body, {
      subtree: true,
      attributeOldValue: false
    })

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
  /*
    fillSeatChart(chosenDate) {
      const dates = this.state.dates
      const seatData = this.state.seatData
      
      for (let index = 0; index < dates.length; index++) {
        if (dates[index]['date'] === chosenDate) {
          const defaultSeatData = {...seatData}
  
          //Object.assign({}, defaultSeatData, this.state.seatData)
          
          console.log(dates[index]['soldSeats'][0])
          
          dates[index]['soldSeats'][0].forEach(function (soldSeat) {
            //console.log(soldSeat)
  
            let AreaDesc = soldSeat['AreaDesc']
            let PhyRowId = soldSeat['PhyRowId']
            let SeatNumber = soldSeat['SeatNumber']
            /*
            defaultSeatData['seatLayout']['colAreas']['objArea'].forEach(function (section) {
              if (section['AreaDesc'] === AreaDesc) {
                section['objRow'].forEach(function (row) {
                  if (row['PhyRowId'] === PhyRowId) {
                    row['objSeat'][SeatNumber - 1]['SeatStatus'] = "1"
                    //console.log(PhyRowId + '|' + SeatNumber)
                  }
                })
              }
            })*/
  //console.log(defaultSeatData)
  /*})
  console.log(defaultSeatData['seatLayout']['colAreas']['objArea'][0]['objRow'][2]['objSeat'])

  this.setState({ displaySeatData: defaultSeatData })
}
}
}*/

  handleDateSubmit(event) {
    const selectElement = document.getElementById('datePickSelect')
    let date = selectElement.options[selectElement.options.selectedIndex].text

    let dateDict = this.state.dates

    let dateIndex = null
    for (let i = 0; i < dateDict.length; i++) {
      if (dateDict[i]['date'] == date) {
        dateIndex = i
      }
    }
    console.log(dateIndex)

    this.setState({
      userPicksDate: date,
      userPicksDateIndex: dateIndex
    })

    //console.log(this.state.seatData['seatLayout']['colAreas']['objArea'][0]['objRow'][2]['objSeat'])
    //console.log('Filling Seats')
    //this.fillSeatChart(date)
    //console.log(this.state.seatData['seatLayout']['colAreas']['objArea'][0]['objRow'][2]['objSeat'])

    event.preventDefault()
  }

  handleBookNow() {
    let rawTickets = document.getElementsByClassName('current-selected')

    if (rawTickets.length === 0) {
      alert('You haven\'t selected any tickets!')
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

  checkTickets(event) {
    let rawTickets = document.getElementsByClassName('current-selected')
    if (rawTickets.length === 0) {
      event.preventDefault()
      alert('You haven\'t selected any tickets!')
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


  goBack() {
    this.setState({ userPicksDate: null })
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
      userPicksDateIndex,
      userPicksSelectedTickets,
      tempCart,
      showId
    } = this.state


    if (error) {
      return React.createElement("div", null, "Error: ", error.message);
    } else if (!isLoaded) {
      return React.createElement("div", null, "Loading...")
    } else if (!userPicksDate) {
      return (
        <div className="col-50">
          <div className="mx-auto" style={{ width: 'auto' }}>
            <div className="container">
              <form onSubmit={this.handleDateSubmit}>
                <label htmlFor="datePickSelect">Dates and times</label>
                <div className="row">
                  <div className="col-sm-8">
                    <select className="form-control" id="datePickSelect">
                      {this.showDates()}
                    </select>
                  </div>
                  <div className="col-sm-4">
                    <button type="submit" className="btn btn-primary">Get tickets</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      )
    }
    else if (!userPicksSelectedTickets) {
      return (
        <div className="container">
          <div className="row">
            <div className="col-md-8 order-md-1">
              <button type='button'
                className='btn btn-secondary'
                onClick={this.goBack}>
                <i className='fas fa-arrow-left' style={{ 'fontSize': '10px' }} />
                <span>Back</span>
              </button>
            </div>
            <div className="col-md-8 order-md-2">
              <SeatingGrid seatingData={seatData} bookedData={dates[userPicksDateIndex]['soldSeats']} />
            </div>
            <div className="col-md-4 order-md-3">
              <Cart />
              <button className="btn btn-success">Make booking</button>
            </div>
          </div>
          <input type='hidden' name='showId' value={showId} />
          <input type='hidden' name='Date' value={userPicksDate} />
        </div>
      )
    }
  }
}
