function showOverlay(filters_overlay, sort_overlay){
    var overlay = document.getElementById(filters_overlay, sort_overlay);
    overlay.classList.add('active');
}

function hideOverlay(filters_overlay, sort_overlay) {
    var overlay = document.getElementById(filters_overlay, sort_overlay);
    if (overlay){
        overlay.classList.remove('active');
    }
    
}
