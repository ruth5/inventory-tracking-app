// Submit a put request for the completion of the edit form
'use strict';

const button = document.getElementsByClassName("add-warehouse")[0]

button.addEventListener('click',
    () => {
        const formInputs = {
            warehouseName: document.querySelector('#warehouse-name').value,
            streetAddress: document.querySelector('#street-address').value,
            city: document.querySelector('#city').value,
            state: document.querySelector('#state').value,
            postalCode: document.querySelector('#postal-code').value,
            country: document.querySelector('#country').value,
        };

        fetch('/warehouses', {
            method: "POST",
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
