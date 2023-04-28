document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('sendData').addEventListener('click', async () => {
        const data = {
            action: "button_click",
            timestamp: new Date().toISOString(),
        };

        const response = await fetch('http://localhost:5001/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        console.log(result);
    });
});
