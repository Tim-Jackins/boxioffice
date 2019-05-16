import { Component, createElement } from 'react';

class Cart extends Component {
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
      console.log('another test');
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
      tempCartInfo = propsCartInfo;
    } //this.setState({ cartInfo: tempCartInfo })


    if (tempCartInfo) {
      const cartInfo = tempCartInfo; //this.state.cartInfo

      let cost = 0.0;
      let items = [];

      for (let i = 0; i < cartInfo.length; i++) {
        items.push(createElement('li', {
          className: 'list-group-item d-flex justify-content-between lh-condensed'
        }, [createElement('div', {}, [createElement('h6', {
          className: 'my-0'
        }, cartInfo[i].id), createElement('small', {
          className: 'text-muted'
        }, cartInfo[i].desc)]), createElement('span', {
          className: 'text-muted'
        }, '$' + parseFloat(cartInfo[i].cost).toFixed(2))]));
        cost += parseFloat(cartInfo[i].cost);
      }

      this.setState({
        cartHTML: createElement("div", null, createElement("h4", {
          className: "d-flex justify-content-between align-items-center mb-3"
        }, createElement("span", {
          className: "text-muted"
        }, "Your cart"), createElement("span", {
          className: "badge badge-secondary badge-pill"
        }, cartInfo.length)), createElement("ul", {
          className: "list-group mb-3"
        }, items, createElement("li", {
          className: "list-group-item d-flex justify-content-between"
        }, createElement("span", null, "Total (USD)"), createElement("strong", null, "$", cost.toFixed(2)))))
      });
    }

    return null;
  }

  render() {
    return createElement("div", null, this.state.cartHTML);
  }

}

export default Cart;