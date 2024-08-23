document.getElementById('crime-report-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    const formData = {
        firstName: document.getElementById('first-name').value,
        lastName: document.getElementById('last-name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        message: document.getElementById('message').value,
        victim: document.querySelector('input[name="victim"]:checked').value,
        witness: document.querySelector('input[name="witness"]:checked').value
    };
    
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'Data saved successfully') {
            alert(data.message);
            document.getElementById('crime-report-form').reset();
        } else {
            alert('There was an error: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error. Please try again.');
    });
});
