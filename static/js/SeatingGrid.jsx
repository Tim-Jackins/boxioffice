class Seat extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isChosen: false,
      PhyRowId: this.props['phy-row-id'],
      GridSeatNum: props['grid-seat-num'],
      SeatNumber: props['seat-number'],
      SeatStatus: props['seat-status'],
      AreaDesc: props['area-desc'],
      cost: 2.5
    };
    this.handleClick = this.handleClick.bind(this);
    this.getClassName = this.getClassName.bind(this);
  }

  handleClick() {
    if (this.state.SeatStatus === '0') {
      this.setState(state => ({
        isChosen: !state.isChosen
      }));
    }

    console.log(`Seat ${this.state.PhyRowId}${this.state.SeatNumber} is ${!this.state.isChosen ? 'chosen' : 'removed'}`);
  }

  getClassName() {
    let baseName = 'seat-row-seat seat-yes'

    if (this.state.SeatStatus === '0') {
      baseName += '  can-select'
    } else {
      baseName += ' not-allowed'
    }

    if (this.state.isChosen) {
      baseName += ' current-selected'
    }

    return baseName
  }

  render() {
    return (
      <li id={`${this.state.PhyRowId}${this.state.SeatNumber}`}
        area-desc={this.state.AreaDesc}
        cost={this.state.cost}
        className={this.getClassName()}>
        <span onClick={this.handleClick} />
      </li>
    )
  }

}

class SeatingGrid extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      seatLayout: props.seatingData.seatLayout,
      bookedSeats: props.bookedData,
      intMaxSeatId: props.seatingData.seatLayout.colAreas.intMaxSeatId,
      intMinSeatId: props.seatingData.seatLayout.colAreas.intMinSeatId,
      makeSeatRow: this.makeSeatRow.bind(this),
      makeSeatArea: this.makeSeatArea.bind(this),
      makeFullSeatGrid: this.makeFullSeatGrid.bind(this)
    }

    console.log('FLAG')
    console.log(this.state.bookedSeats)
    console.log('END')

  }

  makeSeatRow(rowInfo) {
    const {
      AreaDesc,
      AreaCode,
      AreaNum,
      seatRow
    } = rowInfo
    let row = []
    let realSeatIndex = 0
    const bookedSeats = this.state.bookedSeats

    for (let seatGridNum = this.state.intMinSeatId; seatGridNum <= this.state.intMaxSeatId; seatGridNum++) {
      let seat = seatRow.objSeat[realSeatIndex]

      if (seat == null) {
        row.push(<li className='seat-row-seat' />)
      } else if (seat.GridSeatNum === seatGridNum) {
        let seatData = {
          "GridSeatNum": seatRow.GridRowId,
          "SeatStatus": seat.SeatStatus,
          "seatNumber": seat.SeatNumber,
          "GridRowId": seatRow.GridRowId,
          "PhyRowId": seatRow.PhyRowId,
          "AreaNum": AreaNum,
          "AreaCode": AreaCode,
          "AreaDesc": AreaDesc
        }
        let tempSeatStatus = seat.SeatStatus
        if (bookedSeats.includes(`${seatData.AreaDesc} ${seatData.PhyRowId}${seatData.seatNumber}`)) {
          tempSeatStatus = false
        }
        row.push(<Seat
          phy-row-id={seatRow.PhyRowId}
          grid-seat-num={seatRow.GridRowId}
          seat-number={seatData.seatNumber}
          seat-status={tempSeatStatus}
          area-desc={seatData.AreaDesc}
        />)
        realSeatIndex++;
      } else {
        row.push(<li className='seat-row-seat' />)
      }
    }

    return (
      <ul className="seat-area-row">
        <li className="seat-row-seat row-indicator">
          {seatRow.PhyRowId}</li>
        {row}</ul>
    )
  }

  makeSeatArea(objArea) {
    let seatRows = [];

    for (const seatRow in objArea.objRow) {
      let tempSeatRow = {
        "AreaDesc": objArea.AreaDesc,
        "AreaCode": objArea.AreaCode,
        "AreaId": objArea.AreaId,
        'seatRow': objArea.objRow[seatRow]
      };
      seatRows.push(this.makeSeatRow(tempSeatRow));
    }

    return (
      <div id={objArea.AreaId} className="seat-area">
        <div className="seat-area-desc">
          {objArea.AreaDesc}
        </div>
        {seatRows}
      </div>
    )
  }

  makeFullSeatGrid(seatLayout) {
    let seatAreas = [];

    for (const seatArea of seatLayout.colAreas.objArea) {
      seatAreas.push(this.makeSeatArea(seatArea));
    }

    return (
      <div className="col-md-4 order-md-2 mb-4">
        <div className="seat-selection" style={{ width: (this.state.intMaxSeatId + 1) * 30 + 'px' }}>
          {seatAreas}
          <div className="movie-screen">Stage</div>
        </div>
      </div>
    )
  }

  render() {
    const {
      seatingData
    } = this.props;
    const seatLayout = seatingData.seatLayout;
    return (<div>{this.makeFullSeatGrid(seatLayout)}</div>)
  }
}
