jQuery(".fake-text").find('div').first().hide();
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
                    document.getElementById('content').innerText = "This news is not credible!"; 
                    document.getElementsByClassName('logo-box')[0].style.display = 'none';
                    return articleCredible;
                }else if (data.message === "True") {
                    articleCredible = true;
                    document.getElementById('content').innerText = "This news is credible!";
                    document.getElementsByClassName('logo-box')[0].style.display    = 'none';
                 return articleCredible;
                }
            })
            .catch(error => console.error('Error:', error));
    
        return false;
    
    }
document.getElementsByClassName('fake-text')[0].style.display    = 'none';

isCredibleOrNot();
 

