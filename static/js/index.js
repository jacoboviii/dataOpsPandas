// The following code is based off a toggle menu by @Bradcomp
// source: https://gist.github.com/Bradcomp/a9ef2ef322a8e8017443b626208999c1
(function() {
    var burger = document.querySelector('.burger');
    var menu = document.querySelector('#'+burger.dataset.target);
    burger.addEventListener('click', function() {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });
})();

// File Upload Event
const input = document.querySelector('#file-upload');

input.addEventListener('change', fileUpload);

function fileUpload(e) {
    const file = document.querySelector('#file-upload-name')
    file.textContent = e.target.files[0].name
};

// Loading animation Event
const btnProcess = document.querySelector('.button-process');
const btnLoading = document.querySelector('.button-loading');
const btndownload = document.querySelector('.button-download');

btnProcess.addEventListener('click', fileProcess);

function fileProcess(e){
    btnProcess.style.display = 'none';
    btnLoading.style.display = 'inline-flex';

    setTimeout(function() {
        btnLoading.style.display = 'none';
        btndownload.style.display = 'inline-flex';
    }, 2000);
};
