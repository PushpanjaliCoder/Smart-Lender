document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {

        e.preventDefault();

        document.getElementById("loader").style.display = "flex";

        setTimeout(function () {
            form.submit();
        }, 100);

    });

});