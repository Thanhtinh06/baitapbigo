let s = "12:02:00M";

function timeConversion(s) {
  // Write your code here
  let time = s.substr(-2);
  let hour = Number(s.substr(0, 2));
  let part = s.slice(2, s.length - 2);
  if (time === "PM" && hour >= 1 && hour < 12) {
    hour += 12;
    return hour.toString() + part;
  }
  if (time === "AM" && hour === 12) {
    hour -= 12;
    return "00" + part;
  }

  return s.slice(0, 8);
}
