
chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    // use `url` here inside the callback because it's asynchronous!

    // Use the Fetch API to send a POST request to the Flask server
    fetch('http://localhost:5000/receive_url', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
    
});

    function isCredibleOrNot(){
        var articleCredible = true;
        fetch('http://localhost:5000/data')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.message === "False") {
                    articleCredible = false;
                    document.getElementById('content').innerText = "This news is fake!"; 
                    return articleCredible;
                }else if (data.message === "True") {
                    articleCredible = true;
                    document.getElementById('content').innerText = "This news is credible!";
                    return articleCredible;
                }
            })
            .catch(error => console.error('Error:', error));
    
        return false;
    
    }

isCredibleOrNot();
 

