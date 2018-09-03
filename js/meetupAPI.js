function fillMeetupFields (events) {

    let element = document.getElementById('meetup');
    let html = "<h3 class=\"title\"></h3><span class=\"date\"></span><span class=\"topic\"></span><a><span class=\"map-pointer\"></span><span class=\"venue\"></span></a><a class=\"link\"> find out more </a></a><hr class=\"dotted\">";

    for(i=0; i < events.length; i++){
        let meetupInfo = document.createElement('a');
        meetupInfo.className = 'meetup-info';
        meetupInfo.innerHTML = html;

        title           = meetupInfo.getElementsByClassName('title')[0];
        venue           = meetupInfo.getElementsByClassName('venue')[0];
        link            = meetupInfo.getElementsByClassName('link')[0];
        date            = meetupInfo.getElementsByClassName('date')[0];
        topic           = meetupInfo.getElementsByClassName('topic')[0];


        title.innerHTML = events[i].name;
        venue.innerHTML = events[i].venue.name + " \n" + events[i].venue.address_1 + "\n" + events[i].venue.city;
        link.href       = events[i].link;
        date.innerHTML  = events[i].local_date + "\n" + events[i].local_time;
        topic.innerHTML = events[i].description.substring(3, 200) + "...";
        // meetupInfo.href = events[i].link;
        element.appendChild(meetupInfo);
    }

}

$.ajax({
    url: "https://api.meetup.com/PyLadies-Berlin/events?&sign=true&photo-host=public&page=3",
    jsonp: "callback",
    dataType: "jsonp",
    data: {
        format: "json"
    },
    success: function(response) {
        let events = response.data;
        // console.log(events)
        fillMeetupFields(events);
    }
});
