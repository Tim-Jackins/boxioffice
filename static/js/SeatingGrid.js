import React, { Component, createElement } from 'react';
import './SeatingGrid.css';
import './cursors.css';

class Seat extends Component {
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
    let baseName = 'seat-row-seat seat-yes';

    if (this.state.SeatStatus === '0') {
      baseName += '  can-select';
    } else {
      baseName += ' not-allowed';
    }

    if (this.state.isChosen) {
      baseName += ' current-selected';
    }

    return baseName;
  }

  render() {
    return React.createElement("li", {
      id: `${this.state.PhyRowId}${this.state.SeatNumber}`,
      "area-desc": this.state.AreaDesc,
      cost: this.state.cost,
      className: this.getClassName()
    }, React.createElement("span", {
      onClick: this.handleClick
    }));
  }

}

class SeatingGrid extends Component {
  constructor(props) {
    super(props);
    this.seatLayout = props.seatingData.seatLayout;
    this.intMaxSeatId = this.seatLayout.colAreas.intMaxSeatId;
    this.intMinSeatId = this.seatLayout.colAreas.intMinSeatId;
    this.makeSeatRow = this.makeSeatRow.bind(this);
    this.makeSeatArea = this.makeSeatArea.bind(this);
    this.makeFullSeatGrid = this.makeFullSeatGrid.bind(this);
  }

  makeSeatRow(rowInfo) {
    const {
      AreaDesc,
      AreaCode,
      AreaNum,
      seatRow
    } = rowInfo;
    let row = [];
    let realSeatIndex = 0;

    for (let seatGridNum = this.intMinSeatId; seatGridNum <= this.intMaxSeatId; seatGridNum++) {
      let seat = seatRow.objSeat[realSeatIndex];

      if (seat == null) {
        row.push(createElement('li', {
          className: 'seat-row-seat'
        }));
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
        };
        row.push(React.createElement(Seat, {
          "phy-row-id": seatRow.PhyRowId,
          "grid-seat-num": seatRow.GridRowId,
          "seat-number": seat.SeatNumber,
          "seat-status": seat.SeatStatus,
          "area-desc": seatData.AreaDesc
        }));
        realSeatIndex++;
      } else {
        row.push(createElement('li', {
          className: 'seat-row-seat'
        }));
      }
    }

    return React.createElement("ul", {
      className: "seat-area-row "
    }, React.createElement("li", {
      className: "seat-row-seat row-indicator"
    }, seatRow.PhyRowId), row);
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

    return React.createElement("div", {
      id: objArea.AreaId,
      className: "seat-area"
    }, React.createElement("div", {
      className: "seat-area-desc"
    }, objArea.AreaDesc), seatRows);
  }

  makeFullSeatGrid(seatLayout) {
    let seatAreas = [];

    for (const seatArea of seatLayout.colAreas.objArea) {
      seatAreas.push(this.makeSeatArea(seatArea));
    } //style={{ width: (this.intMaxSeatId + 1) * 30 + 'px' }}


    return React.createElement("div", {
      className: "col-md-4 order-md-2 mb-4"
    }, React.createElement("div", {
      className: "seat-selection",
      style: {
        width: (this.intMaxSeatId + 1) * 30 + 'px'
      }
    }, seatAreas, React.createElement("div", {
      className: "movie-screen "
    }, "Stage")));
  }

  render() {
    const {
      seatingData
    } = this.props;
    const seatLayout = seatingData.seatLayout;
    return React.createElement("div", null, this.makeFullSeatGrid(seatLayout));
  }

}

export default SeatingGrid;