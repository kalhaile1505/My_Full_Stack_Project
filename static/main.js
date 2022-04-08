
function darkMode() {
    let page = document.body;
    page.classList.toggle("dark-mode");

}

const btn = document.querySelector(".mode");

const currentTheme = localStorage.getItem("theme");
if (currentTheme == "dark") {
    document.body.classList.add("dark-theme");
}

btn.addEventListener("click", function () {
    document.body.classList.toggle("dark-theme");

    let theme = "light";
    if (document.body.classList.contains("dark-theme")) {
        theme ="dark";
    }
    localStorage.setItem("theme", theme);

});


$(document).ready(function() {
    $("#hide-text").click(function(){
        $("p").toggle();
    });
});




