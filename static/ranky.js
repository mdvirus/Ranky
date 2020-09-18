const fetchAndUpdate = async () => {
    //Get the loader
    let loader = document.querySelector('.loader-wrapper');

    //Make the loader visible
    loader.classList.toggle("visible");

    const fetchUrl = window.location + "fetch";

    //Get the data from the api
    let response = await fetch(fetchUrl);
    let jsonData = await response.json();

    //Get and make the table invisible
    let table = document.querySelector('#ranky-table');
    table.style.display = "none";

    //Get the table body DOM node
    let dataTable = document.querySelector('#data-table');
    

    //Create and add row to the table body
    jsonData.forEach((user, idx) => {
        //Insert all the required row and cells
        let row = dataTable.insertRow();
        let rank = row.insertCell();
        let name = row.insertCell();
        let username = row.insertCell();
        let toph = row.insertCell();
        let dimik = row.insertCell();
        let uri = row.insertCell();
        let total = row.insertCell();

        //Set the values of the cells
        rank.innerText = idx + 1;
        name.innerText = user[1];
        username.innerText = user[2];
        toph.innerText = user[3];
        dimik.innerText = user[4];
        uri.innerText = user[5];
        total.innerText = user[0];
    });
    //We have finished loading and adding all the datas to the table. Now toggle the visibilty of the loader and display the table
    loader.classList.toggle('visible');
    //Wait for 1 seconds and the make the table visible
    setTimeout(() => {
        let table = document.querySelector('#ranky-table');
        table.style.display = "";
    }, 1000)
}