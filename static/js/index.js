// The following code is based off a toggle menu by @Bradcomp
// source: https://gist.github.com/Bradcomp/a9ef2ef322a8e8017443b626208999c1
(function () {
    var burger = document.querySelector('.burger');
    var menu = document.querySelector('#' + burger.dataset.target);
    burger.addEventListener('click', function () {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });
})();

// query Selectors
const heroBody = document.querySelector('.hero-body');
const formProcess = document.querySelector('#form-process');
const btnProcess = document.querySelector('.button-process');
const btnLoading = document.querySelector('.button-loading');
const btndownload = document.querySelector('.button-download');

// File Upload Event
const input = document.querySelector('#file-upload');

input.addEventListener('change', fileUpload);

function fileUpload(e) {
    const file = document.querySelector('#file-upload-name');
    file.textContent = e.target.files[0].name;
    defaultButtonDisplay();
    clearNotification();
};

// Form submission Event
formProcess.addEventListener('submit', fileProcess);

function fileProcess(e) {
    e.preventDefault();
    // Grab file from form
    const formData = new FormData(formProcess)
    // makes ajax request
    $.ajax({
        type: 'POST',
        url: '/process',
        processData: false,
        contentType: false,
        cache: false,
        data: formData,
        success: function (data) {
            console.log(data)
            if (data.errors) {
                // Clear notifications first
                clearNotification();
                // On error display the a notification
                const error = data.errors.upload[0];
                createNotification(error, 'danger');
                defaultButtonDisplay();
            } else {
                // On success, show download button and hide loading button
                setTimeout(function () {
                    btnLoading.style.display = 'none';
                    btndownload.style.display = 'inline-flex';
                }, 1000);
            }
        }
    });
    // Add loading button and hide process button
    btnProcess.style.display = 'none';
    btnLoading.style.display = 'inline-flex';
};

// Download file Event handler
btndownload.addEventListener('click', fileDownload)

function fileDownload(e) {
    // e.preventDefault();
    console.log('downloading!');
    defaultButtonDisplay();
};

// Reset default button display
function defaultButtonDisplay() {
    btnProcess.style.display = 'inline-flex';
    btnLoading.style.display = 'none';
    btndownload.style.display = 'none';
};

// Clear notification
function clearNotification() {
    document.querySelectorAll('.notification').forEach(function(element){
        element.remove()
    });
};

// Create notification
function createNotification(message, className) {
    const messagesDiv = document.createElement('div');
    messagesDiv.textContent = message;
    switch (className) {
        case 'danger':
            messagesDiv.className = 'container notification is-danger';
            break;
        case 'success':
            messagesDiv.className = 'container notification is-success';
            break;
        default:
            messagesDiv.className = 'container notification is-primary';
    }
    heroBody.insertBefore(messagesDiv, heroBody.firstChild);
};