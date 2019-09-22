class Cart extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      propCartInfo: null,
      cartHTML:
        <div>
          <h4 className="d-flex justify-content-between align-items-center mb-3" >
            <span className="text-muted">Your cart</span>
            <span className="badge badge-secondary badge-pill">0</span>
          </h4>
          <ul className="list-group mb-3">
            <li className="list-group-item d-flex justify-content-between lh-condensed">
              <div>
                <h6 className="my-0">Nothing selected</h6>
              </div>
            </li>
            <li className="list-group-item d-flex justify-content-between">
              <span>Total (USD)</span>
              <strong>$0.00</strong>
            </li>
          </ul>
        </div>
      ,
      intMaxSeatId: props.intMaxSeatId
    };
    this.updateCart = this.updateCart.bind(this);
  }

  componentDidMount() {
    const mutationObserver = new MutationObserver(this.updateCart);
    mutationObserver.observe(document.body, {
      subtree: true,
      attributeOldValue: false
    });
  }

  componentDidUpdate() {
    if (this.props.cartInfo && !this.state.propCartInfo) {
      this.setState({
        propCartInfo: this.props.cartInfo
      });

      this.updateCart();
    }
  }

  updateCart() {
    const propsCartInfo = this.props.cartInfo;
    let tempCartInfo = [];

    if (!propsCartInfo) {
      let rawTickets = document.getElementsByClassName('current-selected');

      for (let i = 0; i < rawTickets.length; i++) {
        tempCartInfo.push({
          id: rawTickets[i].id,
          desc: rawTickets[i].getAttribute(['area-desc']),
          cost: rawTickets[i].getAttribute(['cost'])
        });
      }
    } else {
      tempCartInfo = JSON.parse(propsCartInfo)
    }
    console.log(tempCartInfo)

    if (tempCartInfo) {
      const cartInfo = tempCartInfo;

      let cost = 0.0;
      let items = [];

      for (let i = 0; i < cartInfo.length; i++) {
        items.push(
          <li className='list-group-item d-flex justify-content-between lh-condensed'>
            <div>
              <h6 className='my-0'>{cartInfo[i].id}</h6>
              <small className='text-muted'>
                {cartInfo[i].desc}
              </small>
              <span className='text-muted'>{`: $${parseFloat(cartInfo[i].cost).toFixed(2)}`}</span>
            </div>
          </li>
        )
        cost += parseFloat(cartInfo[i].cost);
      }

      if (items.length == 0) {
        items[0] =
          <li className="list-group-item d-flex justify-content-between lh-condensed">
            <div>
              <h6 className="my-0">Nothing selected</h6>
            </div>
          </li>
      }

      this.setState({
        cartHTML:
          <div>
            <h4 className="d-flex justify-content-between align-items-center mb-3">
              <span className="text-muted">Your cart</span>

              <span className="badge badge-secondary badge-pill">{cartInfo.length}</span>
            </h4>
            <ul className="list-group mb-3">
              {items}
              <li className="list-group-item d-flex justify-content-between">
                <span>Total (USD)</span>
                <strong>{`$${cost.toFixed(2)}`}</strong>
              </li>
            </ul>
            <input type='hidden' name='total_cost' value={cost.toFixed(2)} />
            <input type='hidden' name='Seats' value={JSON.stringify(tempCartInfo)} />
          </div>
      })
    }

    return null
  }

  render() {
    return <div>{this.state.cartHTML}</div>
  }
}
