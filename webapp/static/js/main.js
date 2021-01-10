const popupConfirmation = () => {
    deleteBtn = document.getElementById("delete-confirm-btn");

    document.querySelectorAll('.badge-danger').forEach(item => {
        item.addEventListener('click', () => {
            deleteBtn.href = item.href;
            deleteBtn.innerHTML = "Delete";
            document.getElementById('actionText').innerHTML = "Delete";
            document.getElementById('smactionText').innerHTML = "delete";
        });
    });

    document.querySelectorAll('.badge-warning').forEach(item => {
        item.addEventListener('click', () => {
            deleteBtn.href = item.href;
            deleteBtn.innerHTML = "Clear";
            document.getElementById('actionText').innerHTML = "Clear";
            document.getElementById('smactionText').innerHTML = "clear";
        });
    });
}

popupConfirmation();