// Handle actions for edit and delete buttons on items page.
'use strict';


let deleteButtons = document.getElementsByClassName("delete-button");
for (let i = 0; i < deleteButtons.length; i++) {
    deleteButtons[i].addEventListener('click',
        () => {
            let itemID = deleteButtons[i].id
            fetch(`/items/${itemID}`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
            });

            window.alert('Item has been deleted.')
            location.reload();
        }
    )
};

let editButtons = document.getElementsByClassName("edit-button");
for (let i = 0; i < editButtons.length; i++) {
    editButtons[i].addEventListener('click',
        () => {
            let itemID = editButtons[i].id
            window.location.href = `/edit-item-form?item-id=${itemID}`
        }
    )
};