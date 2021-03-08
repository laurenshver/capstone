function get_rate(form) {
    var rate = form.elements['rate'];
    for (var index = 0; index < rate.length; index++) {
        if (rate[index].checked) {
            return rate[index].value;
        }
    }
}

function get_date(form) {
    return new Date(form.elements['start'].value);
}

function get_rental_length(form){
    var length = form.elements['rlength'];
    return parseInt(length.value);
}

Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}

Date.prototype.addHours = function(h) {
    this.setTime(this.getTime() + (h*60*60*1000));
    return this;
  }

function estimate_end_date() {
    var form = document.forms['rental-length'];
    var rate = get_rate(form);
    var start = get_date(form);
    var length = get_rental_length(form);
    
    if (rate == 'daily'){
        return start.addDays(length);
    } else if (rate == 'weekly'){
        return start.addDays(7*length);
    } else if (rate == 'monthly'){
        return start.addDays(30*length); 
    } else if (rate == 'hourly') {
        if (length < 4){
            alert("Hourly minimum is 4 hours");
            return "";
        } else {
            return start.addHours(length);
        }   
    } else {
        return start;
    }
    
    
}

