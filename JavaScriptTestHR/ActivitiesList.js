function Activity(amount) {
  this.amount = amount;
  function setAmount(value) {
    if (value <= 0) {
      return false;
    }
    amount = value;
    return true;
  }
  function getAmount() {
    return this.amount;
  }
}

function Payment(amount, receiver) {
  Payment.prototype = new Activity(amount);
  Payment.prototype.receiver = receiver;

  function setReceiver(receiver) {
    Payment.prototype.receiver = receiver;
  }
  function getReceiver() {
    return Payment.prototype.receiver;
  }
}
function Refund(amount, sender) {
  Payment.prototype = new Activity(amount);
  Payment.prototype.sender = sender;

  function setReceiver(sender) {
    Payment.prototype.sender = sender;
  }
  function getReceiver() {
    return Payment.prototype.sender;
  }
}
