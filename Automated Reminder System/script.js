/* Clean and Correct JavaScript Logic */
document.getElementById("reminderForm").addEventListener("submit", function (event) {
    event.preventDefault();

    // Get values
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;
    const selectedDelivery = document.getElementById("deliveryMethod").value;

    // 1. Validation BEFORE sending
    if (!title || !date || !time) {
        alert("ERROR: Please fill in the Title, Date, and Time fields.");
        return;
    }

    // 2. Send data to backend (Python Flask)
    fetch("/add_reminder", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            title: title,
            description: description,
            date: date,
            time: time,
            delivery: selectedDelivery
        })
    })
    .then(res => res.json())
    .then(data => {

        // 3. One clean final confirmation message
        alert(`
REMINDER SUCCESSFULLY SCHEDULED!
------------------------------------
Title: ${title}
Date: ${date}
Time: ${time}
Delivery Method: ${selectedDelivery}
Description: ${description || "(No description provided)"}

SERVER: ${data.message}
        `);
    })
    .catch(err => {
        console.error(err);
        alert("ERROR: Could not send reminder to server.");
    });
});
