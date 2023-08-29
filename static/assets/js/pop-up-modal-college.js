var my_popup = document.getElementById("exampleModal");
    function showPopUp() {
        my_popup.style.display = "block";
    }
    function hidePopUp() {
        my_popup.style.display = "none";
    }
    setTimeout(showPopUp,30000);
    document.getElementById("modalClose").addEventListener("click", hidePopUp);