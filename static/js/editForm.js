// Submit a put request for the completion of the edit form
'use strict';

const button = document.getElementsByClassName("edit-button")[0]
button.addEventListener('click',
    () => {
        const formInputs = {
            serialNumber: document.querySelector('#serial-number').value,
            warehouseID: document.querySelector('#warehouse-id').value,
        };

        const itemID = button.id
        fetch(`/items/${itemID}`, {
            method: "PUT",
            body: JSON.stringify(formInputs),
            headers: {
                "Content-Type": "application/json",
            },
        }).then(response => response.json())
            .then(responseJson => {
                alert(responseJson.status);
                window.location.href = `/items`;
            });

    }
);
