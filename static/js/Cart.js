class Cart extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      propCartInfo: null,
      cartHTML: null,
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
    } //this.setState({ cartInfo: tempCartInfo })
    

    if (tempCartInfo) {
      const cartInfo = tempCartInfo; //this.state.cartInfo

      let cost = 0.0;
      let items = [];

      for (let i = 0; i < cartInfo.length; i++) {
        items.push(React.createElement('li', {
          className: 'list-group-item d-flex justify-content-between lh-condensed'
        }, [React.createElement('div', {}, [React.createElement('h6', {
          className: 'my-0'
        }, cartInfo[i].id), React.createElement('small', {
          className: 'text-muted'
        }, cartInfo[i].desc)]), React.createElement('span', {
          className: 'text-muted'
        }, '$' + parseFloat(cartInfo[i].cost).toFixed(2))]));
        cost += parseFloat(cartInfo[i].cost);
      }

      this.setState({
        cartHTML: React.createElement("div", null, React.createElement("h4", {
          className: "d-flex justify-content-between align-items-center mb-3"
        }, React.createElement("span", {
          className: "text-muted"
        }, "Your cart"), React.createElement("span", {
          className: "badge badge-secondary badge-pill"
        }, cartInfo.length)), React.createElement("ul", {
          className: "list-group mb-3"
        }, items, React.createElement("li", {
          className: "list-group-item d-flex justify-content-between"
        }, React.createElement("span", null, "Total (USD)"), React.createElement("strong", null, "$", cost.toFixed(2)))),
          React.createElement('input', {
            type: 'hidden',
            name: 'total_cost',
            value: cost.toFixed(2)
          })
        )
      });
    }

    return null;
  }

  render() {
    return React.createElement("div", null, this.state.cartHTML)
  }
}
