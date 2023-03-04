function filter_direction() {
    const filter = document.getElementsByClassName('form-select'); 
    console.log(filter[0].value);
    const search = document.getElementById("dashboard-name");
    console.log(search.innerHTML)
    const button = document.createElement('a');
    button.setAttribute('href', "/filter?search="+search.innerHTML+"&&filter="+filter[0].value);
    button.click();
    // $.get("/filter?search="+search.innerHTML+"&&filter="+filter[0].value, function (response) {
    //     if (response) {
    //         console.log('success')
    //     } else {
    //         console.log('not success')
            
    //     }
    // });
}