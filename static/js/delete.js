'use strict';

let buttons = document.getElementsByTagName("button");
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click',
        () => {
            let itemID = buttons[i].id
            fetch(`/items/${itemID}`, {
                method: "DELETE",
                headers: {
                "Content-Type": "application/json",
                },
            });

            window.alert('Item has been deleted.')
            location.reload();
}
    )};